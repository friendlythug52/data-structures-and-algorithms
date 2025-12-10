import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, regularizers
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

warnings.filterwarnings('ignore')

# ============== ПАРАМЕТРИЗИРОВАННЫЕ НАСТРОЙКИ ==============
# Гиперпараметры обучения
BATCH_SIZE = 64  # Увеличено для стабильности
EPOCHS = 50  # Уменьшено - достаточно для сходимости
LEARNING_RATE = 0.001
VALIDATION_SPLIT = 0.2
RANDOM_SEED = 42

# Архитектура сети (упрощена)
LAYER1_UNITS = 64  # Уменьшено
LAYER2_UNITS = 32  # Уменьшено
LAYER3_UNITS = 16  # Уменьшено

# Регуляризация
DROPOUT_RATE_1 = 0.2  # Снижен dropout
DROPOUT_RATE_2 = 0.1
L1_REG = 0.0
L2_REG = 0.00001  # Снижена регуляризация


# ============== ЗАГРУЗКА И ПОДГОТОВКА ДАННЫХ ==============
print("=" * 60)
print("ЗАГРУЗКА ДАТАСЕТА")
print("=" * 60)

# Загрузка датасета
df = pd.read_csv('star_classification 3.csv')
print(f"✓ Датасет загружен: {df.shape[0]} строк, {df.shape[1]} столбцов")
print(f"✓ Классы: {df['class'].unique()}")
print(f"✓ Распределение классов:\n{df['class'].value_counts()}\n")


# ============== ПРЕДВАРИТЕЛЬНАЯ ОБРАБОТКА ==============
print("=" * 60)
print("ПРЕДВАРИТЕЛЬНАЯ ОБРАБОТКА ДАННЫХ")
print("=" * 60)

# Удаление дублирующихся столбцов и неиспользуемых признаков
features_to_use = [
    'alpha',
    'delta',
    'u',
    'g',
    'r',
    'i',
    'z',
    'redshift',
]

# Проверка наличия признаков
features_available = [f for f in features_to_use if f in df.columns]
print(f"✓ Используются признаки: {features_available}")

# Подготовка признаков и целевой переменной
X = df[features_available].copy()
y = df['class'].copy()

# Обработка пропущенных значений
print(f"✓ Пропущенные значения в X: {X.isnull().sum().sum()}")
print(f"✓ Пропущенные значения в y: {y.isnull().sum()}")

# Удаление строк с пропущенными значениями
X = X.dropna()
y = y[X.index]
print(f"✓ Размер датасета после очистки: {X.shape[0]} образцов")

# Кодирование целевой переменной
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# One-hot encoding для многоклассовой классификации
y_onehot = keras.utils.to_categorical(y_encoded, num_classes=3)
print(
    f"✓ Классы закодированы: "
    f"{dict(zip(le.classes_, range(len(le.classes_))))}"
)
print(f"✓ One-hot encoding применён\n")


# ============== РАЗДЕЛЕНИЕ ДАННЫХ ==============
print("=" * 60)
print("РАЗДЕЛЕНИЕ ДАННЫХ")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_onehot,
    test_size=0.2,
    random_state=RANDOM_SEED,
    stratify=y,
)

print(f"✓ Обучающий набор: {X_train.shape[0]} образцов")
print(f"✓ Тестовый набор: {X_test.shape[0]} образцов\n")


# ============== НОРМАЛИЗАЦИЯ ДАННЫХ ==============
print("=" * 60)
print("НОРМАЛИЗАЦИЯ ДАННЫХ")
print("=" * 60)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"✓ StandardScaler применён")
print(
    f"✓ Среднее значение (обучающий): "
    f"{X_train_scaled.mean(axis=0).round(4)}"
)
print(
    f"✓ Стандартное отклонение: "
    f"{X_train_scaled.std(axis=0).round(4)}\n"
)


# ============== ПОСТРОЕНИЕ МОДЕЛИ ==============
print("=" * 60)
print("ПОСТРОЕНИЕ НЕЙРОННОЙ СЕТИ")
print("=" * 60)

# Инициализация модели
model = keras.Sequential()

# Входной слой
model.add(
    layers.Dense(
        LAYER1_UNITS,
        input_dim=X_train_scaled.shape[1],
        activation='relu',
        kernel_regularizer=regularizers.L1L2(l1=L1_REG, l2=L2_REG),
        kernel_initializer='he_normal',
    )
)
model.add(layers.BatchNormalization())
model.add(layers.Dropout(DROPOUT_RATE_1))

# Второй слой
model.add(
    layers.Dense(
        LAYER2_UNITS,
        activation='relu',
        kernel_regularizer=regularizers.L1L2(l1=L1_REG, l2=L2_REG),
        kernel_initializer='he_normal',
    )
)
model.add(layers.BatchNormalization())
model.add(layers.Dropout(DROPOUT_RATE_2))

# Третий слой
model.add(
    layers.Dense(
        LAYER3_UNITS,
        activation='relu',
        kernel_regularizer=regularizers.L1L2(l1=L1_REG, l2=L2_REG),
        kernel_initializer='he_normal',
    )
)
model.add(layers.Dropout(DROPOUT_RATE_2))

# Выходной слой
model.add(layers.Dense(3, activation='softmax'))

print("✓ Архитектура модели:")
model.summary()


# ============== КОМПИЛЯЦИЯ МОДЕЛИ ==============
print("\n" + "=" * 60)
print("КОМПИЛЯЦИЯ МОДЕЛИ")
print("=" * 60)

# Создание оптимизатора Adam с пользовательской скоростью обучения
optimizer = keras.optimizers.Adam(learning_rate=LEARNING_RATE)
model.compile(
    optimizer=optimizer,
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

print(f"✓ Оптимизатор: Adam (LR={LEARNING_RATE})")
print(f"✓ Функция потерь: categorical_crossentropy")
print(f"✓ Метрика: accuracy\n")


# ============== CALLBACKS ДЛЯ СТАБИЛЬНОГО ОБУЧЕНИЯ ==============
print("=" * 60)
print("НАСТРОЙКА CALLBACKS")
print("=" * 60)

# Early Stopping - остановка при отсутствии улучшений
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True,
    verbose=1
)

# ReduceLROnPlateau - снижение learning rate при плато
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=1e-7,
    verbose=1
)

print("✓ EarlyStopping настроен (patience=10)")
print("✓ ReduceLROnPlateau настроен (factor=0.5, patience=5)\n")


# ============== ОБУЧЕНИЕ МОДЕЛИ ==============
print("=" * 60)
print("ОБУЧЕНИЕ НЕЙРОННОЙ СЕТИ")
print("=" * 60)

history = model.fit(
    X_train_scaled,
    y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_split=VALIDATION_SPLIT,
    callbacks=[early_stopping, reduce_lr],
    verbose=1,
    shuffle=True,
)

print("\n✓ Обучение завершено!\n")


# ============== ОЦЕНКА МОДЕЛИ ==============
print("=" * 60)
print("ОЦЕНКА ПРОИЗВОДИТЕЛЬНОСТИ")
print("=" * 60)

# Оценка на обучающем наборе
train_loss, train_accuracy = model.evaluate(
    X_train_scaled,
    y_train,
    verbose=0,
)
print(
    f"✓ Обучающий набор - "
    f"Loss: {train_loss:.4f}, Accuracy: {train_accuracy:.4f}"
)

# Оценка на тестовом наборе
test_loss, test_accuracy = model.evaluate(
    X_test_scaled,
    y_test,
    verbose=0,
)
print(
    f"✓ Тестовый набор - "
    f"Loss: {test_loss:.4f}, Accuracy: {test_accuracy:.4f}\n"
)


# ============== ПРЕДСКАЗАНИЯ ==============
print("=" * 60)
print("ГЕНЕРАЦИЯ ПРЕДСКАЗАНИЙ")
print("=" * 60)

y_pred_prob = model.predict(X_test_scaled, verbose=0)
y_pred = np.argmax(y_pred_prob, axis=1)
y_test_labels = np.argmax(y_test, axis=1)

print(f"✓ Предсказания выполнены для {len(y_pred)} образцов\n")


# ============== МЕТРИКИ КЛАССИФИКАЦИИ ==============
print("=" * 60)
print("КЛАССИФИКАЦИОННЫЕ МЕТРИКИ")
print("=" * 60)

print(f"\nОбщая точность: {accuracy_score(y_test_labels, y_pred):.4f}\n")
print("Детальный отчёт по классам:")
print(
    classification_report(
        y_test_labels,
        y_pred,
        target_names=le.classes_,
        digits=4,
    )
)


# ============== МАТРИЦА ОШИБОК ==============
print("=" * 60)
print("МАТРИЦА ОШИБОК (CONFUSION MATRIX)")
print("=" * 60)

cm = confusion_matrix(y_test_labels, y_pred)
print("\nМатрица ошибок:")
print(cm)


# ============== ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ (ИСПРАВЛЕНО) ==============
print("\n" + "=" * 60)
print("ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# График 1: История обучения (Accuracy) - ГЛАДКИЙ
axes[0].plot(
    history.history['accuracy'],
    label='Обучающая точность',
    linewidth=2,
    color='#1f77b4'
)
axes[0].plot(
    history.history['val_accuracy'],
    label='Валидационная точность',
    linewidth=2,
    color='#ff7f0e'
)
axes[0].set_title(
    'Точность обучения и валидации',
    fontsize=12,
    fontweight='bold',
)
axes[0].set_xlabel('Эпоха')
axes[0].set_ylabel('Точность')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# График 2: История обучения (Loss) - ГЛАДКИЙ
axes[1].plot(
    history.history['loss'],
    label='Обучающая функция потерь',
    linewidth=2,
    color='#1f77b4'
)
axes[1].plot(
    history.history['val_loss'],
    label='Валидационная функция потерь',
    linewidth=2,
    color='#ff7f0e'
)
axes[1].set_title(
    'Функция потерь обучения и валидации',
    fontsize=12,
    fontweight='bold',
)
axes[1].set_xlabel('Эпоха')
axes[1].set_ylabel('Функция потерь')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
print("✓ Графики обучения успешно отображены!\n")

# Отдельная визуализация для матрицы ошибок и распределения
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

# График 3: Матрица ошибок
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    ax=axes2[0],
    xticklabels=le.classes_,
    yticklabels=le.classes_,
    cbar_kws={'label': 'Количество'},
)
axes2[0].set_title('Матрица ошибок', fontsize=12, fontweight='bold')
axes2[0].set_ylabel('Истинные значения')
axes2[0].set_xlabel('Предсказания')

# График 4: Распределение классов в тестовом наборе
unique, counts = np.unique(y_test_labels, return_counts=True)
axes2[1].bar(
    le.classes_[unique],
    counts,
    color=['#FF6B6B', '#4ECDC4', '#95E1D3'],
)
axes2[1].set_title(
    'Распределение классов в тестовом наборе',
    fontsize=12,
    fontweight='bold',
)
axes2[1].set_ylabel('Количество образцов')
axes2[1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
print("✓ Дополнительные графики успешно отображены!\n")


# ============== СОХРАНЕНИЕ МОДЕЛИ ==============
print("=" * 60)
print("СОХРАНЕНИЕ МОДЕЛИ")
print("=" * 60)

model.save('star_classification_model.h5')
print("✓ Модель сохранена как 'star_classification_model.h5'")

np.save('scaler_mean.npy', scaler.mean_)
np.save('scaler_std.npy', scaler.scale_)
print("✓ Параметры скейлера сохранены\n")


# ============== ПРИМЕРЫ ПРЕДСКАЗАНИЙ ==============
print("=" * 60)
print("ПРИМЕРЫ ПРЕДСКАЗАНИЙ")
print("=" * 60)

# Выбираем несколько примеров из тестового набора
example_indices = np.random.choice(len(X_test_scaled), 5, replace=False)
print("\nПримеры предсказаний:\n")

for idx in example_indices:
    print(f"Образец {idx}:")
    print(f"  Истинный класс: {le.classes_[y_test_labels[idx]]}")
    print(f"  Предсказанный класс: {le.classes_[y_pred[idx]]}")
    print(
        f"  Вероятности: "
        f"{dict(zip(le.classes_, y_pred_prob[idx].round(4)))}"
    )
    print()

print("=" * 60)
print("ОБУЧЕНИЕ ЗАВЕРШЕНО!")
print("=" * 60)
