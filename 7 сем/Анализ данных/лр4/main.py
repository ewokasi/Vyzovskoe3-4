import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

# Параметры
target_size = (150, 150)  # Размер изображений
batch_size = 32
epochs = 50
num_classes = 5

# Путь к данным (предполагается, что изображения находятся в папках с именами классов)
data_dir = './flowers'  # Путь к главной папке с подкаталогами цветов

# Список классов
classes = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# Инициализация списков для хранения данных
data = []
labels = []

# Загрузка изображений
for label, class_name in enumerate(classes):
    class_dir = os.path.join(data_dir, class_name)
    for img_name in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_name)
        
        # Загружаем изображение и изменяем его размер
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img) / 255.0  # Нормализация
        data.append(img_array)
        labels.append(label)

# Преобразуем данные в numpy массивы
data = np.array(data)
labels = np.array(labels)

# Разделение на тренировочную и валидационную выборки
X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, stratify=labels)

# Преобразование меток в one-hot кодировку
y_train = tf.keras.utils.to_categorical(y_train, num_classes=num_classes)
y_val = tf.keras.utils.to_categorical(y_val, num_classes=num_classes)

# Проверка формы меток
print("Shape of y_train:", y_train.shape)
print("Shape of y_val:", y_val.shape)

# Строим сверточную нейронную сеть
model = models.Sequential([
    # Сверточные слои и слои подвыборки
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(target_size[0], target_size[1], 3)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Выпрямление
    layers.Flatten(),
    
    # Полносвязные слои
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),  # Дропаут для борьбы с переобучением
    layers.Dense(num_classes, activation='softmax')
])

# Компиляция модели
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),  # Передаем валидационные данные для оценки на каждом шаге
    epochs=100,
    batch_size=16
)

# Построение графиков точности и ошибки
plt.figure(figsize=(12, 4))

# График точности
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# График ошибки потерь
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
