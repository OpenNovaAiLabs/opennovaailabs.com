from flask import Flask, request, jsonify
from keras.models import model_from_json
import numpy as np
import cv2
import mediapipe as mp
from spellchecker import SpellChecker
import pickle

app = Flask(__name__)
spell = SpellChecker()

# Load the ASL recognition model from pickle
with open("model/cnn_model.p", "rb") as file:
    model_dict = pickle.load(file)
model = model_dict['model']

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Label dictionary
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
               12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
               23: 'X', 24: 'Y', 25: 'Z', 26: 'space'}

def predict_character(image):
    frame_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    if not results.multi_hand_landmarks:
        return 'NO HANDS'
    
    for hand_landmarks in results.multi_hand_landmarks:
        x_ = []
        y_ = []
        data_aux = []

        for i in range(len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y

            x_.append(x)
            y_.append(y)

        for i in range(len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y
            data_aux.append(x - min(x_))
            data_aux.append(y - min(y_))

        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]
        return predicted_character

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    predicted_character = predict_character(image)
    return jsonify({'predicted_character': predicted_character})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
