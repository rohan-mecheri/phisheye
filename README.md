# PhishEye - Phishing Detection Using NLP and Machine Learning

## Introduction

PhishEye is a phishing detection framework built using Natural Language Processing (NLP) and machine learning models to classify URLs as either "phishing" or "legitimate." The project leverages features extracted from URL structures, including text-based patterns, special character counts, and entropy, to improve cybersecurity by identifying phishing attempts in real-time.

## Project Structure

### Data Ingestion and Preprocessing

- **Data Loading**: The dataset, containing various URL features and labels, is loaded from an Excel file.
- **Cleaning**: Rows with missing or invalid values in critical columns are removed.
- **Feature Engineering**: Extracted features such as URL length, special character counts (dots, hyphens, slashes), entropy, and presence of suspicious keywords (e.g., "login," "secure").
  
### Exploratory Data Analysis (EDA)

EDA was performed to better understand the dataset and guide feature engineering:

- **Univariate Analysis**: Distribution of key numeric features like URL length and character counts.
- **Bivariate Analysis**: Relationship between features and the target variable (phishing or legitimate).
- **Correlation Heatmap**: Analyzed correlations between numeric features to detect multicollinearity.

### Model Development

The project uses multiple machine learning models to classify URLs:

- **Logistic Regression**: A linear classifier trained to predict whether a URL is phishing or legitimate.
- **Support Vector Machine (SVM)**: A non-linear classifier used to capture more complex relationships.
- **Random Forest**: A decision-tree-based ensemble model used to improve prediction accuracy.

### Model Training and Evaluation

Each model was trained using the engineered features and evaluated using accuracy, precision, recall, F1-score, and confusion matrices.

- **Best Model**: The Random Forest classifier provided the best performance, with balanced precision and recall for both phishing and legitimate URLs.
- **Confusion Matrices**: Displayed to assess the model’s ability to distinguish between phishing and legitimate URLs.

### Flask Deployment

PhishEye is deployed as a web application using Flask:

- **User Input**: Users input a URL into the web interface.
- **Prediction**: The model predicts whether the URL is phishing or legitimate, displaying the result to the user.
- **Frontend**: A simple HTML form allows for easy interaction with the backend model.

## Results

The trained model achieves over 81% accuracy in detecting phishing URLs. Results are visualized through confusion matrices and classification reports for each model, demonstrating its effectiveness in real-world phishing detection.