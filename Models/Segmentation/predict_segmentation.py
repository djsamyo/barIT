from train_segmenter import *

def run_segmenter(image): 
  if not os.path.exists('Models/segmenter.h5'): 
    retrain_segmenter()
  model = keras.models.load_model('Models/segmenter.h5')
  
  pred = np.argmax(model.predict(image))
  
  return pred
