import tensorflow as tf
mnist = tf.keras.datasets.mnist

# Configuration
optimizer = 'adam'
epochs = 1

# Loading MNIST dataset
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Creating model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Training model with 5 epochs
model.fit(x_train, y_train, epochs=epochs)


# Performing evaluation using test split
model.evaluate(x_test, y_test)

# Save entire model to HDF5 file
model.save('./models/trained_model_ds_2.h5')
