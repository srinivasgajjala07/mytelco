from flask import Flask, render_template, request
import pickle
import pandas as pd
# from pymongo import MongoClient
from imblearn.combine import SMOTEENN
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('modell.pkl', 'rb'))


# app.config['MONGO_URI'] = 'mongodb://localhost:27017'  # Use the default MongoDB URI

# mongo = MongoClient(app.config['MONGO_URI'])
# db = mongo['churn_prediction']

# @app.route('/check_mongodb')
# def check_mongodb():
#     try:
#         # Try to query a collection in MongoDB to check connection
#         collection_names = db.list_collection_names()
#         return f"Connected to MongoDB. Available collections: {', '.join(collection_names)}"
#     except Exception as e:
#        return f"Failed to connect to MongoDB. Error: {str(e)}"
    
@app.route('/')
def design():
    return render_template('design.html')
@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/exit.html')
def exit():
    return render_template('exit.html')


@app.route('/project.html')
def home():
    return render_template('project.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method =='POST':
        tenure = int(request.form.get('tenure', 0))
        monthly_charges = float(request.form.get('MonthlyCharges', 0))
        total_charges = float(request.form.get('TotalCharges', 0))
        contract = int(request.form.get('Contract', 0))
        online_security = int(request.form.get('OnlineSecurity', 0))
        tech_support = int(request.form.get('TechSupport', 0))
        device_protection = int(request.form.get('DeviceProtection', 0))
        internet_service = int(request.form.get('InternetService', 0))

        input_data = pd.DataFrame([[tenure, monthly_charges, total_charges, contract, online_security, tech_support, device_protection, internet_service]],
                              columns=['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'OnlineSecurity', 'TechSupport', 'DeviceProtection', 'InternetService'])

        prediction = model.predict(input_data)

        if prediction[0] == 0:
            result = "This customer is Not Churned (it means continue the service)"
        else:
            result = "This customer is likely to be Churned (it means left or stopped the service)"

        # prediction_collection = db['predictions']
        # prediction_data = {
        # 'tenure': tenure,
        # 'MonthlyCharges': monthly_charges,
        # 'TotalCharges': total_charges,
        # 'Contract': contract,
        # 'OnlineSecurity': online_security,
        # 'TechSupport': tech_support,
        # 'DeviceProtection': device_protection,
        # 'InternetService': internet_service,
        # 'Prediction': result
        # }
        # prediction_collection.insert_one(prediction_data)
        try:
         return render_template('result.html', result=result)  
        except Exception as e:
            print(f"Error: {str(e)}")
            return "An error occurred while making predictions."
if __name__ == "__main__":
    app.run()
# if __name__ == '__main__':
#     app.run(debug=True)













  








