from train_classifier import *

def run_classifier(image): 
  if not os.path.exists('Models/classifier.h5'): 
    retrain_classifier()
  model = keras.models.load_model('Models/classifier.h5')
  
  pred = model.predict(image)
  if pred[1] > 0.5: 
    return True
  else: 
    return False
  
