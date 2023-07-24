from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from tqdm import tqdm
from keras.applications.resnet50 import preprocess_input, decode_predictions
from main import *

class dog_detection():
    def __init__(self):
        self.ResNet50_model = ResNet50(weights='imagenet')
    def path_to_tensor(self,img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        return np.expand_dims(x, axis=0)
    def paths_to_tensor(self,img_paths):
        list_of_tensors = [self.path_to_tensor(img_path) for img_path in tqdm(img_paths)]
        return np.vstack(list_of_tensors)
    def ResNet50_predict_labels(self,img_path):
        img = preprocess_input(self.path_to_tensor(img_path))
        return np.argmax(self.ResNet50_model.predict(img))
    def read_face_output(self,img_path):
        prediction = self.ResNet50_predict_labels(img_path)
        return ((prediction <= 268) & (prediction >= 151))

detector = dog_detection()
# print(detector.dog_detector('golden-retriever-royalty-free-image-506756303-1560962726.jpg'))
obj = ig_scrapper()
obj.scrapper(detector,'doglovers')