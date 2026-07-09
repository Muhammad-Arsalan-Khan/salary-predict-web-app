# 💰 Salary Prediction App

A machine learning web application that predicts salary based on **years of experience** and **education level**, built with **scikit-learn** and **Streamlit**.

## 📌 Overview

This project uses a **Linear Regression** model trained on historical salary data to predict expected salary given a person's years of experience and highest education level (Bachelor's, Master's, or PhD). The model is served through an interactive Streamlit web interface.

## 🚀 Demo

Live app: *https://salary-predict-web-app-israbkz6wuqo48xts8crdf.streamlit.app/*

## ✨ Features

- Predicts salary from experience and education level
- Simple, interactive web UI (no coding required to use it)
- Trained using Linear Regression on real salary data
- Model persistence with `pickle` for fast predictions (no retraining needed on each run)

## 🛠️ Tech Stack

| Component        | Technology        |
|-------------------|-------------------|
| Language          | Python            |
| ML Library        | scikit-learn      |
| Data Handling     | pandas, numpy     |
| Web UI            | Streamlit         |
| Visualization     | matplotlib        |

## 📁 Project Structure

```
salary-prediction-app/
│
├── app.py               # Streamlit web application
├── train_model.py       # Script to train and save the ML model
├── requirements.txt     # Python dependencies
├── Salary Data.csv      # Training dataset
├── salary_model.pkl     # Saved trained model (generated after training)
└── README.md            # Project documentation
```

## ⚙️ Installation & Setup (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muhammad-Arsalan-Khan/salary-predict-web-app.git
   cd salary-prediction-web-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**
   ```bash
   python train_model.py
   ```
   This generates a `salary_model.pkl` file used by the app for predictions.

4. **Run the app**
   ```bash
   streamlit run app.py
   ```
   The app will open automatically in your browser at `http://localhost:8501`.

## 📊 Model Details

- **Algorithm:** Linear Regression
- **Input Features:**
  - `Years of Experience` (numeric)
  - `Education Level` (encoded: Bachelor's = 1, Master's = 2, PhD = 3)
- **Target Variable:** `Salary`
- **Evaluation Metrics:**
  - Mean Absolute Error (MAE) 11,739.81 
  - Mean Squared Error (MSE) 260,169,645.15
  - Root Mean Squared Error (RMSE) 16,129.78
  - R² Score  0.888

## 🌐 Deployment

This app can be deployed for free using:
- [Streamlit Community Cloud](https://share.streamlit.io)

## 🔮 Future Improvements

- Add more features (e.g., job title, location, industry)
- Try advanced models (Random Forest, XGBoost) for better accuracy
- Add data visualization dashboard within the app
- Add input validation and error handling in the UI

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋 Author

*Muhammad Arsalan khan linkedin: www.linkedin.com/in/arsalan-webdev*
