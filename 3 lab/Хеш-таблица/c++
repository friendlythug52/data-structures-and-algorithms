#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <functional>

template<typename K, typename V>
class HashTable {
private:
    std::vector<std::list<std::pair<K, V>>> table;
    size_t capacity;

    size_t hash(const K& key) {
        return std::hash<K>{}(key) % capacity;
    }

public:
    HashTable(size_t size = 10) : capacity(size) {
        table.resize(capacity);
    }

    void put(const K& key, const V& value) {
        size_t index = hash(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        table[index].emplace_back(key, value);
    }

    V get(const K& key) {
        size_t index = hash(key);
        for (const auto& pair : table[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        throw std::runtime_error("Key not found");
    }

    void remove(const K& key) {
        size_t index = hash(key);
        auto& bucket = table[index];
        for (auto it = bucket.begin(); it != bucket.end(); ++it) {
            if (it->first == key) {
                bucket.erase(it);
                return;
            }
        }
        throw std::runtime_error("Key not found");
    }

    bool contains(const K& key) {
        try {
            get(key);
            return true;
        } catch (const std::runtime_error&) {
            return false;
        }
    }

    void display() {
        for (size_t i = 0; i < capacity; ++i) {
            std::cout << "Bucket " << i << ": ";
            for (const auto& pair : table[i]) {
                std::cout << "(" << pair.first << ", " << pair.second << ") ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    std::cout << "Хеш-таблица (C++):" << std::endl;
    HashTable<std::string, std::string> ht;
    
    ht.put("Alice", "January");
    ht.put("Bob", "May");
    ht.put("Charlie", "August");
    
    std::cout << "Alice: " << ht.get("Alice") << std::endl;
    ht.remove("Bob");
    ht.display();
    
    return 0;
}
