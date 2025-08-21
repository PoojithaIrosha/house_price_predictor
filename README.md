🏡 House Price Predictor

This project is a machine learning application that predicts house prices based on input features such as location, size, and number of rooms. It is built with a clear separation between model development and deployment:

Model Creation: A Jupyter Notebook (notebooks/model_training.ipynb) is used to explore the dataset, preprocess data, train a regression model, and evaluate its performance. The trained model is exported and stored in the models/ directory.

Flask Application: A lightweight web service (app/) built with Flask loads the trained model and exposes prediction functionality via REST API endpoints or a simple web interface.

Data Management: All datasets are organized under the data/ folder, separating raw and processed data.

Testing: Unit and integration tests are included in the tests/ directory to ensure the model and API work as expected.

Key Features

End-to-end workflow: from data preprocessing → model training → model deployment.

REST API for serving predictions in real-time.

Modular and extensible folder structure for future improvements.

Easy setup with requirements.txt.
