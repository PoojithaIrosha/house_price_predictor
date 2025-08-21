from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

pipeline = joblib.load('models/california_house_price_pipeline.joblib')
feature_names = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]

        final_features = np.array(features).reshape(1, -1)

        prediction = pipeline.predict(final_features)

        predicted_price = prediction[0] * 100000
        output = f"${predicted_price:,.2f}"

        return render_template('index.html', prediction_text=f"Predicted Median House Value: {output}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: Please ensure all fields are filled correctly. Details: {e}")

if __name__ == '__main__':
    app.run()
