
from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

application = Flask(__name__)
app = application

# Load the model and scaler
model = pickle.load(open('RandomForest_Customer_Churn_Prediction.pkl', 'rb'))
scaler = pickle.load(open('Scalar_Customer_Churn_Prediction.pkl', 'rb'))

# Define feature names in the order they were used for training the model
feature_names = ['age', 'subscription_type', 'num_subscription_pauses', 'customer_service_inquiries', 
                 'weekly_hours', 'song_skip_rate', 'weekly_unique_songs', 'notifications_clicked']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve and validate form data
            age = int(request.form['age'])
            weekly_hours = int(request.form['weekly_hours'])
            weekly_unique_songs = int(request.form['weekly_unique_songs'])
            notifications_clicked = int(request.form['notifications_clicked'])
            
            # Validate numerical ranges (example for age shown)
            if not (18 <= age <= 80):
                raise ValueError("Age must be between 18 and 80.")
            if not (0 <= weekly_hours <= 50):
                raise ValueError("Weekly Listening hours must be between 0 and 50.")
            if not (0 <= weekly_unique_songs <= 300):
                raise ValueError("Weekly Unique Songs must be between 0 and 300.")
            if not (0 <= notifications_clicked <= 50):
                raise ValueError("Notification Clicks must be between 0 and 50.")
            
            # Encoding for categorical features
            subscription_type = request.form['subscription_type']
            subs = {'Free': 0, 'Student': 1, 'Premium': 2, 'Family': 3}[subscription_type]
            
            num_subscription_pauses = request.form['num_subscription_pauses']
            pauses = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[num_subscription_pauses]
            
            song_skip_rate = request.form['song_skip_rate']
            skip_rate = {'No Skips': 0, 'Light Skips': 0.25, 'Average Skips': 0.5, 'High Skips': 1}[song_skip_rate]

            customer_service_inquiries = request.form['customer_service_inquiries']
            service = {'Low': 0, 'Medium': 1, 'High': 2}[customer_service_inquiries]

            # Prepare input data as a pandas DataFrame with feature names
            input_data_dict = {
                'age': [age],
                'subscription_type': [subs],
                'num_subscription_pauses': [pauses],
                'customer_service_inquiries': [service],
                'weekly_hours': [weekly_hours],
                'song_skip_rate': [skip_rate],
                'weekly_unique_songs': [weekly_unique_songs],
                'notifications_clicked': [notifications_clicked]
            }

            # Convert input data into a pandas DataFrame with correct column names
            input_data_df = pd.DataFrame(input_data_dict, columns=feature_names)

            # Debug: Print the input data to check it's in the correct format
            print(input_data_df)

            # Apply scaling - transform the input data using the same scaler used during training
            input_scaled = scaler.transform(input_data_df)

            # Debug: Print the scaled input data to ensure scaling works
            # print(input_scaled)

            # Make prediction
            prediction = model.predict(input_scaled)
            print(prediction)
            prediction_message = "Yay! The customer will Stay subscribed!" if prediction[0] == 0 else "So sorry, the customer will cancel the Subscription.."

            return render_template('prediction.html', prediction_message=prediction_message)
        
        except ValueError as e:
            return render_template('index.html', prediction_text=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7003)
