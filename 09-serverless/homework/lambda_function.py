import tflite_runtime.interpreter as tflite
import numpy as np

from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(200, 200))

interpreter = tflite.Interpreter(model_path='model_2024_hairstyle_v2.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)

    return float(preds[0, 0])


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }

    return result