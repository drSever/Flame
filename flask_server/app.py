from flask import Flask, request, render_template, jsonify

import tensorflow as tf
from tensorflow import keras

from util import base64_to_pil

# Declare a flask app
app = Flask(__name__)

MODEL_PATH = 'models/converted_model.tflite'

with open(MODEL_PATH, 'rb') as fid:
    tflite_model = fid.read()


def model_predict(img, model):
    """
    Runs model and predicts fire probability
    """
    # Resize to 256 x 256
    img = img.resize((256, 256))

    # Image to bitmap
    img_array = keras.preprocessing.image.img_to_array(img)

    # Expand dimension for set_tensor
    img_array = tf.expand_dims(img_array, 0)

    # Interpreter interface for running TensorFlow Lite models
    interpreter = tf.lite.Interpreter(model_content=model)
    interpreter.allocate_tensors()  # Needed before execution

    input_index = interpreter.get_input_details()[0]["index"]
    output_index = interpreter.get_output_details()[0]["index"]

    # Sets the value of the input tensor
    interpreter.set_tensor(input_index, img_array)
    interpreter.invoke()

    # Gets the value of the output tensor
    prediction = interpreter.get_tensor(output_index)
    return prediction


@app.route('/', methods=['GET'])
def index():
    """
    Main page
    """
    print(type(render_template('index.html')))
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Gets an image and outputs the result
    """
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Make prediction
        predict_proba = model_predict(img, tflite_model)

        # Process result for human
        probability = (100 * (1 - predict_proba[0]))[0]
        result = "This image is " + str(probability) + " percent Fire"

        return jsonify(result=result)

    return None


if __name__ == '__main__':
    app.run(port=5000, threaded=False)
