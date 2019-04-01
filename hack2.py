
import pickle
import pandas as pd
filename = 'finalized_model.sav'


def acute_predict(b):
	loaded_model = pickle.load(open(filename, 'rb'))
	result = loaded_model.predict(b)
	return result[0:2]
