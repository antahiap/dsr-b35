import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models, layers

def encode(image, label, image_size=(128, 128)):
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, image_size)
    return image, label
dataset = dataset_train_original.map(lambda image, label: encode(image, label))

def augment(image, label):
    image_augmented = image
    image_augmented = tf.image.random_flip_left_right(image_augmented)
    image_augmented = tf.image.random_flip_up_down(image_augmented)
    return image_augmented, label



gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("Available GPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPUs available.")


(dataset_train_original, dataset_validate_original), infor = tfds.load(
    "cats_vs_dogs",
    split=["train[:10%]", "train[90%:]"], # pretending we don't have a big dataset
                                          # dataset is already shuffled
    as_supervised=True,
    with_info=True
)


dataset_train_augmented = dataset_train_original.map(lambda image, label: encode(image, label))
dataset_train_augmented = dataset_train_augmented.cache()
dataset_train_augmented = dataset_train_augmented.map(lambda image, label: augment(image, label))
dataset_train_augmented = dataset_train_augmented.shuffle(2500)
dataset_train_augmented = dataset_train_augmented.batch(128)

dataset_validate = dataset_validate_original.map(lambda image, label: encode(image, label))
dataset_validate = dataset_validate.cache()
dataset_validate = dataset_validate.batch(128)


base_net = tf.keras.applications.VGG16(
    input_shape = (128, 128, 3),# add the input layer, cant change input_shape without 
                                # include_top=False, due to FC layers number of parameters
    include_top = False,        # skip the input layer
)
base_net.trainable = False      # freezing the layers


model = models.Sequential([
    base_net,
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])


model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(    
    dataset_train_augmented,
    epochs=5,
    validation_data=dataset_validate
)

# Save the trained model
model.save('trained_model.h5')