# Forest Cover Type Prediction - Multiclass Classification 🌳

## 🚀 Streamlit Demo
[You can try it here 🍀](https://forest-cover-type-classification-juzxaqiwvjsxtdyr5pd5ii.streamlit.app/)

## 📂 Project Structure
```
Students-Scores-Prediction/
├── README.md
├── model.ipynb
├── app.py
├── requirements.txt
├── model.pkl
├── runtime.txt
```
## 🧩 Features
- Elevation
- Aspect
- Slope
- Horizontal Distance To Hydrology
- Vertical Distance To Hydrology
- Horizontal Distance To Roadways
- Hillshade at 9 AM
- Hillshade at Noon
- Hillshade at 3 PM
- Horizontal Distance To Fire Points
- Soil Type
- Wilderness Area
- 
## 🔧 Technologies Used
- Python 3.10
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- joblib

## 📓 Notebook Content
- Data Exploration & Cleaning
- Data Visualization 
- Data Preprocessing (Reverse One-Hot Encoding)
- Random Forest model: Training, Testing, Evaluation (Confusion Matrix and Classification Report), and Tuning
- Decision Tree model: Training, Testing, Evaluation (Confusion Matrix and Classification Report), and Tuning
- XGBoost Classifier: Training, Testing, Evaluation (Confusion Matrix and Classification Report), and Tuning

## 🚀 Summary
- XGBoost Classifier model with 0.01 Learning Rate, Number of Estimators = 300, and Max Depth = 25, performs best in terms of Precision, Recall, and F1-Score

## NOTE 🚨
- The model in model.pkl was tuned for deployment (size and speed optimizations).
- The original notebook contains the full training, testing, tuning, and evaluation
- The model used in model.pkl is a Decision Tree model with max_depth = 35
