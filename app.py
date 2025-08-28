from flask import Flask, render_template, request
import librosa
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
import os
from skimage.transform import resize 

# Initialize the Flask app
app = Flask(__name__)

# Set up upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the trained model
model = load_model('Model 2.h5')

# Define the target shape for input spectrograms
target_shape = (128, 128)

# Define class labels
classes = ['Angklung', 'Gamelan', 'Sape', 'Seruling']

def test_audio(file_path, model):
    """
    Preprocess and classify an audio file.
    """
    try:
        # Load the audio file
        audio_data, sample_rate = librosa.load(file_path, sr=None)

        # Generate the mel spectrogram
        mel_spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate)

        # Resize and reshape to the required input shape for the model
        mel_spectrogram = resize(np.expand_dims(mel_spectrogram, axis=-1), target_shape)
        mel_spectrogram = tf.reshape(mel_spectrogram, (1,) + target_shape + (1,))

        # Make predictions
        prediction = model.predict(mel_spectrogram)

        # Get the class probabilities
        class_probabilities = prediction[0]

        # Get the predicted class index
        predicted_class_index = np.argmax(class_probabilities)

        return class_probabilities, predicted_class_index
    except Exception as e:
        print(f"Error processing audio file: {e}")
        return None, None

@app.route("/", methods=['GET', 'POST'])
def main():
    """
    Render the main page.
    """
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def get_output():
    """
    Handle the audio file upload and return predictions.
    """
    if 'fileInput' not in request.files:
        return render_template("index.html", prediction=None)
    
    audio = request.files['fileInput']

    if audio.filename == '':
        return render_template("index.html", prediction=None)


    if audio:
        # Save the audio file to the upload folder
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio.filename)
        audio.save(audio_path)

        # Use the test_audio function to classify the uploaded file
        class_probabilities, predicted_class_index = test_audio(audio_path, model)

        if class_probabilities is None:
            return render_template("index.html", prediction=None, error="Error processing audio file.")

        # Map probabilities to class labels
        predictions = {classes[i]: round(prob, 4) for i, prob in enumerate(class_probabilities)}
        predicted_class = classes[predicted_class_index]
        confidence = class_probabilities[predicted_class_index]

        # Render the result
        return render_template(
            "index.html",
            prediction=predictions,
            predicted_class=predicted_class,
            confidence=round(confidence, 4),
            audio_path=audio.filename
        )

if __name__ == '__main__':
    app.run(debug=True)
