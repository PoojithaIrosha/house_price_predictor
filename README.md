# 🏡 House Price Predictor

This project is a **machine learning application** that predicts house prices based on features like location, size, and number of rooms. It contains two parts:

1. **Model Creation (Jupyter Notebook)** – preprocessing, training, and saving the model pipeline.  
2. **Flask Application** – loads the trained model and serves predictions via REST API or web form.  

---

## 📂 Project Structure

```
house-price-predictor/
│── data/                     # Raw and processed datasets
│── notebooks/                # Jupyter notebooks (model training, experiments)
│── models/                   # Saved trained models (joblib/pickle)
│── app/                      # Flask application
│── tests/                    # Unit and integration tests
│── requirements.txt          # Python dependencies
│── README.md                 # Documentation
│── .gitignore
```

---

## ⚙️ Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/house-price-predictor.git
   cd house-price-predictor
   ```

2. Create a virtual environment and install dependencies:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

### 1️⃣ Train the Model  
Open the notebook and run all cells:  
```bash
jupyter notebook notebooks/model_training.ipynb
```

- This will train the regression pipeline and save the model as `models/house_price_pipeline.joblib`.  

### 2️⃣ Start the Flask App  
Run the Flask application to serve predictions:  
```bash
cd app
python main.py
```

- By default, the app runs on **http://127.0.0.1:5000/**.  
- You can send prediction requests via API or use the web interface (if included in templates).  

---

## 🧪 Testing  
Run unit and integration tests:  
```bash
pytest tests/
```

---

## 🔮 Future Improvements  
- Add Docker support for easier deployment.  
- Integrate CI/CD for automated testing.  
- Enhance the model with more features and data sources.  