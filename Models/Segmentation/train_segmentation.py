def get_model_oxford_pets(img_size, num_classes = 2, num_chans = 3):

    if model_encoder == 'Xception Oxford Pets':

      print("TRUE")

      inputs = keras.Input(shape=img_size + (num_chans,))
      ### [First half of the network: downsampling inputs] ###

      # Entry block
      x = layers.Conv2D(32, 3, strides=2, padding="same")(inputs)
      x = layers.BatchNormalization()(x)
      x = layers.Activation("relu")(x)

      previous_block_activation = x  # Set aside residual

      

      # Blocks 1, 2, 3 are identical apart from the feature depth.
      for filters in [64, 128, 256]:
          x = layers.Activation("relu")(x)
          x = layers.SeparableConv2D(filters, 3, padding="same")(x)
          x = layers.BatchNormalization()(x)

          x = layers.Activation("relu")(x)
          x = layers.SeparableConv2D(filters, 3, padding="same")(x)
          x = layers.BatchNormalization()(x)

          x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

          # Project residual
          residual = layers.Conv2D(filters, 1, strides=2, padding="same")(
              previous_block_activation
          )
          x = layers.add([x, residual])  # Add back residual
          previous_block_activation = x  # Set aside next residual



      filters = 256
      x = layers.Activation("relu")(x)
      x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
      x = layers.BatchNormalization()(x)

      x = layers.Activation("relu")(x)
      x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
      x = layers.BatchNormalization()(x)

      x = layers.UpSampling2D(2)(x)

      # Project residual
      residual = layers.UpSampling2D(2)(previous_block_activation)
      residual = layers.Conv2D(filters, 1, padding="same")(residual)
      x = layers.add([x, residual])  # Add back residual
      previous_block_activation = x

    elif model_encoder == 'Xception': 
      backbone = Xceptionm(input_shape = img_size + (num_chans,), include_top = False)
      x = backbone.layers[121].output

      filters = 256

      xx = layers.Activation("relu")(x)
      x = layers.Conv2DTranspose(filters, 3, padding="same")(xx)
      x = layers.BatchNormalization()(x)

      x = layers.Activation("relu")(x)
      x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
      x = layers.BatchNormalization()(x)

      x = layers.UpSampling2D(2)(x)

      # Project residual
      residual = layers.UpSampling2D(2)(xx)
      residual = layers.Conv2D(filters, 1, padding="same")(residual)
      x = layers.add([x, residual])  # Add back residual
      previous_block_activation = x 





      ### [Second half of the network: upsampling inputs] ###

    for filters in [128, 64, 32]:
        x = layers.Activation("relu")(x)
        x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.Conv2DTranspose(filters, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.UpSampling2D(2)(x)

        # Project residual
        residual = layers.UpSampling2D(2)(previous_block_activation)
        residual = layers.Conv2D(filters, 1, padding="same")(residual)
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    # Add a per-pixel classification layer


    activation = "softmax"


    outputs = layers.Conv2D(num_classes, 3, activation=activation, padding="same")(x)

    # Define the model
    model = keras.Model(inputs, outputs)
    return model
    
X = np.load()#Figure out pathname
Y_segment = np.load() #Figure out pathname
    
model = get_model_oxford_pets((224, 224), num_classes = 2)
model.compile(optimizer="Adam", loss='sparse_categorical_crossentropy')
model.fit(x = X, y=Y_segmentation, epochs=150)

model.save("Models/segmentation")
