#from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def VIPDataset(batch_size,image_size,data_dir):


    #train_size = 83484
    #test_size = 1000

    train_datagen = ImageDataGenerator(rescale=1.0/255)
    test_datagen = ImageDataGenerator(rescale=1.0/255)

    train_path = data_dir+'/Train'
    test_path = data_dir+'/Test'

    classes = ['0', '1','2']

    train_batches = train_datagen.flow_from_directory(train_path, target_size=(image_size,image_size),color_mode='rgb', classes=classes, batch_size=batch_size,class_mode='categorical')
    test_batches = test_datagen.flow_from_directory(test_path, target_size=(image_size,image_size),color_mode='rgb', classes=classes, batch_size=batch_size, class_mode='categorical')

    return train_batches, test_batches

train_batches, test_batches=VIPDataset(8,224,'processed_dataset')
print(train_batches)