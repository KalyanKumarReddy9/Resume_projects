import numpy as np
import pickle
import streamlit as st
from sklearn.base import BiclusterMixin

#loading the saved model
loaded_model=pickle.load(open("C:/kalyan projects/machine learning/deploying machine learning modedl/trained_model.sav",'rb'))

def diabetes_prediction(input_data):

# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return  'The person is not diabetic'
    else:
        return  'The person is diabetic'

def main():

    #giving a title for webpage
    st.title('Diabeted prediction web app')
    #getting the input data from the user
    Pregnancies=st.text_input('Number of pregnancies')
    Glucose=st.text_input('glucose level')
    BloodPressure=st.text_input("blood pressure value")
    SkinThickness=st.text_input("skin thickness value")
    Insulin=st.text_input("enter insulin value")
    BMI=st.text_input("bmi value")
    DiabetesPedigreeFunction=st.text_input("diabetes pedigre function value")
    Age=st.text_input("age value")

    #code for prediction
    diagnosis=''
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([ Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__=='__main__':
    main()
