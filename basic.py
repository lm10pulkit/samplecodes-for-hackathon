import numpy as np
from flask import Flask, request, jsonify,  render_template,Response
import pickle
import cv2
import jsonify
import jsonpickle

app = Flask(__name__)
# Load the model
@app.route('/api',methods=['POST'])
def predict():
	r=request
	print(r.data)
	output={'messsi':"legend", "great":'eyo'}
	return jsonify(output)

@app.route('/api/test', methods=['POST'])
def test():
	r = request
	# convert string of image data to uint8
	nparr = np.fromstring(r.data, np.uint8)
    # decode image
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
	 # build a response dict to send back to client
	response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
    # encode response using jsonpickle
	response_pickled = jsonpickle.encode(response)

	return Response(response=response_pickled, status=200, mimetype="application/json")



if __name__ == '__main__':
	app.run(port=5000, debug=True)