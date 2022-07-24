def image_reconstructor(img_shape, code_size):
    # The encoder
    encoder = Sequential()
    encoder.add(InputLayer(img_shape))
    encoder.add(Flatten())
    encoder.add(Dense(code_size))

    # The decoder
    decoder = Sequential()
    decoder.add(InputLayer((code_size,)))
    decoder.add(Dense(np.prod(img_shape)))
    decoder.add(Reshape(img_shape))

    return encoder, decoder
    
encoder, decoder = build_autoencoder((224,224,3), 64)

inp = Input(IMG_SHAPE)
code = encoder(inp)
reconstruction = decoder(code)

model = Model(inp,reconstruction)
model.compile(optimizer='adamax', loss='mse')

model.fit(X_destroyed, Y_reconstruct, epochs = 150)

model.save("Models/reconstructor")
