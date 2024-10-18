from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and scaler (if applicable)
model = joblib.load('model/phishing_model.pkl')

# Uncomment if using a scaler
# scaler = joblib.load('model/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url_input = request.form['url']  # Get the input URL from the form
        
        # Feature engineering based on the input URL
        input_data = pd.DataFrame({
            'length_url': [len(url_input)],
            'count_hyphens': [url_input.count('-')],
            'count_dots': [url_input.count('.')],
            'count_slashes': [url_input.count('/')],
            'url_entropy': [calculate_entropy(url_input)]
        })

        # If you are using a scaler, scale the input data
        # input_data_scaled = scaler.transform(input_data)
        
        # Make the prediction (0 = legitimate, 1 = phishing)
        prediction = model.predict(input_data)[0]
        
        # Convert prediction to a readable format
        result = 'Phishing URL' if prediction == 1 else 'Legitimate URL'
        
        return render_template('index.html', prediction_text=f'This URL is likely a {result}')
        
# Function to calculate URL entropy (same as in the training script)
def calculate_entropy(url):
    from scipy.stats import entropy
    import collections
    counter = collections.Counter(url)
    probs = [count / len(url) for count in counter.values()]
    return entropy(probs, base=2)

if __name__ == "__main__":
    app.run(debug=True)