def main():

    import numpy as np
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Convolution2D
    from tensorflow.keras.layers import MaxPooling2D
    from tensorflow.keras.layers import Flatten
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras import optimizers
    
    basepath="D:/Final code/crop+soil detection/crop+soil detection/crop_plant"
    
    # Initialing the CNN
    classifier = Sequential()
    
    # Step 1 - Convolutio Layer 
    classifier.add(Convolution2D(32, 1,  1, input_shape = (100, 100, 3), activation = 'relu'))
    
    #step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    # Adding second convolution layer
    classifier.add(Convolution2D(32, 1,  1, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    #Adding 3rd Concolution Layer
    classifier.add(Convolution2D(64, 1,  1, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    #Adding 4rd Concolution Layer
    classifier.add(Convolution2D(64, 1,  1, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    #Adding 5rd Concolution Layer
    classifier.add(Convolution2D(64, 1,  1, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    #Adding 6rd Concolution Layer
    classifier.add(Convolution2D(64, 1,  1, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size =(2,2)))
    
    #Step 3 - Flattening
    classifier.add(Flatten())
    
    #Step 4 - Full Connection
    classifier.add(Dense(256, activation = 'relu'))
    classifier.add(Dropout(0.5))
    classifier.add(Dense(5, activation = 'softmax'))  #change class no.
    
    #Compiling The CNN
    classifier.compile(
                  optimizer = optimizers.SGD(lr = 0.01),
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])
    
    #Part 2 Fittting the CNN to the image
    from keras.preprocessing.image import ImageDataGenerator
    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)
    
    test_datagen = ImageDataGenerator(rescale=1./255)
    
    training_set = train_datagen.flow_from_directory(
            basepath + '/train',
            target_size=(100, 100),
            batch_size=32,
            class_mode='categorical')
    
    test_set = test_datagen.flow_from_directory(
            basepath + '/test',
            target_size=(100, 100),
            batch_size=32,
            class_mode='categorical')
    
    steps_per_epoch = int( np.ceil(training_set.samples / 32) )
    val_steps = int( np.ceil(test_set.samples / 32) )
    
    model = classifier.fit_generator(
            training_set,
            steps_per_epoch=steps_per_epoch,
            epochs=100,
            validation_data = test_set,
            validation_steps =val_steps
          )
    
    #Saving the model
    #import h5py
    classifier.save(basepath + '/soil_model_cnn.h5')
    
    
    scores = classifier.evaluate(test_set, verbose=1)
    B="Testing Accuracy: %.2f%%" % (scores[1]*100)
    print(B)
    scores =  classifier.evaluate(training_set, verbose=1)
    C="Training Accuracy: %.2f%%" % (scores[1]*100)
    print(C)
    
    
    msg=B+'\n'+ C 
    
    
    import matplotlib.pyplot as plt
    # summarize history for accuracy
    plt.plot(model.history['accuracy'])
    plt.plot(model.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(basepath + "/accuracy.png",bbox_inches='tight')

    plt.show()
    # summarize history for loss
    
    plt.plot(model.history['loss'])
    plt.plot(model.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(basepath + "/loss.png",bbox_inches='tight')
    
    plt.show()

    
    return msg
