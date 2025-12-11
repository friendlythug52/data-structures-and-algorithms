import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# ==================== 1. Загрузка и подготовка данных ====================
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Нормализация и изменение формы
x_train = x_train.reshape(-1, 784).astype('float32') / 255.0
x_test = x_test.reshape(-1, 784).astype('float32') / 255.0

# One-hot кодирование меток
y_train_onehot = keras.utils.to_categorical(y_train, 10)
y_test_onehot = keras.utils.to_categorical(y_test, 10)

print(f"Тренировочные данные: {x_train.shape}")
print(f"Тестовые данные: {x_test.shape}")

# ==================== 2. Реализация нейронной сети ====================
class DigitClassifier:
    def __init__(self):
        # Инициализация весов методом Xavier
        self.W1 = np.random.randn(784, 128) * np.sqrt(2.0 / 784)
        self.b1 = np.zeros((1, 128))
        self.W2 = np.random.randn(128, 64) * np.sqrt(2.0 / 128)
        self.b2 = np.zeros((1, 64))
        self.W3 = np.random.randn(64, 10) * np.sqrt(2.0 / 64)
        self.b3 = np.zeros((1, 10))
        
    def relu(self, x):
        return np.maximum(0, x)
    
    def relu_derivative(self, x):
        return (x > 0).astype(float)
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = self.relu(self.z2)
        self.z3 = self.a2 @ self.W3 + self.b3
        self.a3 = self.softmax(self.z3)
        return self.a3
    
    def backward(self, X, y, learning_rate):
        m = X.shape[0]
        
        # Ошибка на выходном слое
        dz3 = self.a3 - y
        dW3 = (self.a2.T @ dz3) / m
        db3 = np.sum(dz3, axis=0, keepdims=True) / m
        
        # Обратное распространение на второй слой
        dz2 = (dz3 @ self.W3.T) * self.relu_derivative(self.a2)
        dW2 = (self.a1.T @ dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        
        # Обратное распространение на первый слой
        dz1 = (dz2 @ self.W2.T) * self.relu_derivative(self.a1)
        dW1 = (X.T @ dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        
        # Обновление весов
        self.W3 -= learning_rate * dW3
        self.b3 -= learning_rate * db3
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
    
    def train(self, X_train, y_train, X_val, y_val, epochs=10, learning_rate=0.01, batch_size=64):
        train_losses = []
        val_losses = []
        train_accs = []
        val_accs = []
        
        n_samples = X_train.shape[0]
        
        for epoch in range(epochs):
            # Перемешивание данных
            indices = np.random.permutation(n_samples)
            X_shuffled = X_train[indices]
            y_shuffled = y_train[indices]
            
            epoch_loss = 0
            correct = 0
            
            for i in range(0, n_samples, batch_size):
                X_batch = X_shuffled[i:i+batch_size]
                y_batch = y_shuffled[i:i+batch_size]
                
                # Forward pass
                outputs = self.forward(X_batch)
                
                # Вычисление потерь (cross-entropy)
                loss = -np.sum(y_batch * np.log(outputs + 1e-8)) / batch_size
                epoch_loss += loss * X_batch.shape[0]
                
                # Точность
                predictions = np.argmax(outputs, axis=1)
                true_labels = np.argmax(y_batch, axis=1)
                correct += np.sum(predictions == true_labels)
                
                # Backward pass
                self.backward(X_batch, y_batch, learning_rate)
            
            # Метрики на тренировочных данных
            train_loss = epoch_loss / n_samples
            train_acc = correct / n_samples
            
            # Валидация
            val_outputs = self.forward(X_val)
            val_loss = -np.sum(y_val * np.log(val_outputs + 1e-8)) / X_val.shape[0]
            val_predictions = np.argmax(val_outputs, axis=1)
            val_true = np.argmax(y_val, axis=1)
            val_acc = np.mean(val_predictions == val_true)
            
            train_losses.append(train_loss)
            val_losses.append(val_loss)
            train_accs.append(train_acc)
            val_accs.append(val_acc)
            
            if (epoch + 1) % 2 == 0:
                print(f"Эпоха {epoch+1}/{epochs} | "
                      f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} | "
                      f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
        
        return train_losses, val_losses, train_accs, val_accs
    
    def predict(self, X):
        outputs = self.forward(X)
        return np.argmax(outputs, axis=1)
    
    def evaluate(self, X, y):
        predictions = self.predict(X)
        true_labels = np.argmax(y, axis=1)
        accuracy = np.mean(predictions == true_labels)
        return accuracy, predictions, true_labels

# ==================== 3. Обучение модели ====================
# Разделение на тренировочную и валидационную выборки
val_size = 10000
x_val = x_train[:val_size]
y_val_onehot = y_train_onehot[:val_size]
x_train_final = x_train[val_size:]
y_train_final_onehot = y_train_onehot[val_size:]

# Создание и обучение модели
model = DigitClassifier()
train_losses, val_losses, train_accs, val_accs = model.train(
    x_train_final, y_train_final_onehot, 
    x_val, y_val_onehot, 
    epochs=15, 
    learning_rate=0.01, 
    batch_size=64
)

# ==================== 4. Визуализация процесса обучения ====================
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# График потерь
axes[0].plot(train_losses, label='Train Loss', linewidth=2)
axes[0].plot(val_losses, label='Val Loss', linewidth=2)
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('Training and Validation Loss')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# График точности
axes[1].plot(train_accs, label='Train Accuracy', linewidth=2)
axes[1].plot(val_accs, label='Val Accuracy', linewidth=2)
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy')
axes[1].set_title('Training and Validation Accuracy')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==================== 5. Оценка на тестовых данных ====================
test_accuracy, test_predictions, test_true = model.evaluate(x_test, y_test_onehot)
print(f"\nТочность на тестовых данных: {test_accuracy:.4f}")

# Матрица ошибок
cm = confusion_matrix(test_true, test_predictions)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=range(10), yticklabels=range(10))
plt.xlabel('Предсказанные метки')
plt.ylabel('Истинные метки')
plt.title('Матрица ошибок на тестовых данных')
plt.show()

# Отчет по классификации
print("\nОтчет по классификации:")
print(classification_report(test_true, test_predictions, digits=4))

# ==================== 6. Визуализация примеров ====================
fig, axes = plt.subplots(3, 5, figsize=(12, 8))
axes = axes.ravel()

misclassified = np.where(test_predictions != test_true)[0]
if len(misclassified) > 0:
    for i in range(15):
        idx = misclassified[i] if i < len(misclassified) else i
        axes[i].imshow(x_test[idx].reshape(28, 28), cmap='gray')
        axes[i].set_title(f"True: {test_true[idx]}, Pred: {test_predictions[idx]}")
        axes[i].axis('off')
else:
    for i in range(15):
        axes[i].imshow(x_test[i].reshape(28, 28), cmap='gray')
        axes[i].set_title(f"True: {test_true[i]}, Pred: {test_predictions[i]}")
        axes[i].axis('off')

plt.suptitle('Примеры предсказаний модели', fontsize=16)
plt.tight_layout()
plt.show()

# ==================== 7. Вывод весов первого слоя ====================
fig, axes = plt.subplots(8, 16, figsize=(16, 8))
for i in range(128):
    row, col = divmod(i, 16)
    axes[row, col].imshow(model.W1[:, i].reshape(28, 28), cmap='coolwarm')
    axes[row, col].axis('off')
plt.suptitle('Визуализация весов первого слоя (128 нейронов)', fontsize=16)
plt.tight_layout()
plt.show()
