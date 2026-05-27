import pickle
import pandas

with open("model.pkl",'rb') as file:

    modle_data = pickle.load(file)

model = modle_data['modle']
features_names = modle_data["feature_names"]

