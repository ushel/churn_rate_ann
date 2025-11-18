import streamlit as st 
import numpy as np  
import tensorflow as tf   
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder 
import pandas as pd   
import pickle

# load the trained model
model = tf.keras.model.load_model('model.h5')

# Load the encoders and scaler
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)
    
with open('onehot_encoder_gro.pkl','rb') as file:
    onehot_encoder_gro = pickle.load(file)
    
with open('scalar.pkl','rb') as file:
    scaler = pickle.load(file)
    
# streamlit app as dont have to worry about html and all

st.title('Customer churn prediction')

# user input

geography = st.selectbox('Geography',onehot_encoder_gro.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age',18, 92)
balance = st.number_input('Balance')
credit_score= st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure',0,10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.slectbox('Is Active Member', [ 0, 1])


input_data = pd.DataFrame({
    'CreditScore':[credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [ balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [ is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = onehot_encoder_gro.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_gro.get_feature_names_out(['Geography']))