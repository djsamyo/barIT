def get_classifier_model(): 
  return(tf.keras.applications.ResNet101V2(
    include_top=True,
    weights="imagenet",
    input_tensor=None,
    input_shape=None,
    pooling=None,
    classes=2,
    classifier_activation="softmax",
)

def retrain_classifier(): 
  X = np.load()#Figure out pathname
  Y_classifier = np.load() #Figure out pathname

  model = get_classifier_model()
  model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy')
  model.fit(X, Y_classifier, epochs = 150)

  model.save("Models/classifier")
