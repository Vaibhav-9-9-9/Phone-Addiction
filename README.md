📱 Phone Addiction Prediction

📌 Project Overview

Smartphones have become an essential part of daily life, but excessive usage can lead to phone addiction, negatively impacting mental health, productivity, sleep patterns, and social interactions.

This project aims to predict the level of smartphone addiction based on various behavioral, psychological, and smartphone usage patterns using machine learning algorithms.

The project analyzes factors such as daily phone usage, sleep hours, social interaction levels, mental health indicators, and app usage patterns to build predictive models that estimate a user's addiction level.

🎯 Problem Statement

The objective of this project is to develop a machine learning model that predicts the level of phone addiction using user behavior, smartphone usage statistics, and psychological factors. Early detection of addiction patterns can help individuals and researchers better understand unhealthy smartphone usage habits.

📂 Dataset

The dataset contains information about users' smartphone usage behavior and psychological indicators.

Features in the dataset include:

Age

Gender

Location

Daily Usage Hours

Sleep Hours

Intellectual Performance

Social Interactions

Exercise Hours

Anxiety Level

Depression Level

Self Esteem

Screen Time Before Bed

Phone Checks Per Day

Apps Used Daily

Time on Social Media

Time on Gaming

Time on Education

Phone Usage Purpose

Family Communication

Weekend Usage Hours

Target Variable

Addiction Level

🧪 Exploratory Data Analysis (EDA)

During EDA, the following steps were performed:

Data cleaning and preprocessing

Handling missing values

Outlier detection using boxplots

Feature scaling using RobustScaler

Data visualization for understanding feature distributions

🤖 Machine Learning Models Used

Multiple machine learning algorithms were implemented and compared:

Linear Regression

K-Nearest Neighbors (KNN)

Decision Tree

Random Forest

Gradient Boosting

AdaBoost

XGBoost

Stacking Regressor

Voting Regressor

Hyperparameter tuning was performed for several models to improve performance.

📊 Model Evaluation

Models were evaluated using:

R² Score

Train vs Test Score Comparison

Model Performance Visualization

The goal was to identify the model that generalizes best without overfitting.

📈 Results

The performance of different models was compared using training and testing scores, and ensemble models such as Stacking and XGBoost showed strong predictive performance.

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

XGBoost

Jupyter Notebook

📁 Project Structure

Phone-Addiction
│

├── phone_addiction_dataset.csv
├── Phone_Addiction_Prediction.ipynb
├── README.md
🚀 How to Run the Project

1️⃣ Clone the repository

git clone https://github.com/Vaibhav-9-9-9/Phone-Addiction.git

2️⃣ Navigate to the project folder

cd Phone-Addiction

3️⃣ Install required libraries

pip install -r requirements.txt

4️⃣ Run the Jupyter Notebook

jupyter notebook
📌 Future Improvements

Deploy the model using Streamlit or Flask

Build a web application for addiction prediction

Add more behavioral and psychological features

Improve model performance using advanced tuning

👨‍💻 Author

Vaibhav M

GitHub:
https://github.com/Vaibhav-9-9-9
