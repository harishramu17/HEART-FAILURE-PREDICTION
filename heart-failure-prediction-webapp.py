# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 12:55:10 2023

@author: mdjit
"""

import numpy as np
import pandas as pd
import seaborn as sb
import pickle
import streamlit as st



header=st.container()
datasets=st.container()
features=st.container()
model_training=st.container()


#@st.cache
#def get_data():




with header:

    st.title("HEART FAILURE PREDICTION MODEL")
    st.text("In This Project I had trained the machine learning model using Navie Bayes Algorithm...!!!")
    st.text("to predict wheather your heart has got failure or not using features....!")

with datasets:
    st.header("HEART FAILURE PREDICTION DataSet")
    st.text("This dataset was created by combining different datasets already available independently  ")
    st.text("but not combined before. In this dataset, 5 heart datasets are combined over 11 common ")
    st.text("features which makes it the largest heart disease dataset available so far for research purposes.")

    heart_data=pd.read_csv("C:/Users/mdjit/Downloads/heart.csv")
    st.write(heart_data.head(11))


   # st.subheader("DISEASE BY AGE")
   # sb.lineplot(data=heart_data,x="Age",y="HeartDisease")


    st.text("The above visualization compares the which category Age of the people are Heart Failured")



    st.text("The DataSet Link ")



    url = "https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction"
    st.write("check out this [link](%s)" % url)
    st.markdown("check out this [link](%s)" % url)


    st.subheader("Creators :")
    st.text("         1.Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.")
    st.text("         2.University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.")
    st.text("         3.University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.")
    st.text("         4.V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.")



with features:


    st.subheader("FEATURES OF THE MODEL")

    st.markdown("1.Age: age of the patient [years]")
    st.markdown("2.Sex: sex of the patient [M: Male, F: Female]")
    st.markdown("3.ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]")
    st.markdown("4.RestingBP: resting blood pressure [mm Hg]")
    st.markdown("5.Cholesterol: serum cholesterol [mm/dl]")
    st.markdown("6.FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]")
    st.markdown("7.RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]")
    st.markdown("8.MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]")
    st.markdown("9.ExerciseAngina: exercise-induced angina [Y: Yes, N: No]")
    st.markdown("10.Oldpeak: oldpeak = ST [Numeric value measured in depression]")
    st.markdown("11.ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]")
    st.markdown("12.HeartDisease: output class [1: heart disease, 0: Normal]")




with model_training:
    
    loaded_model=pickle.load(open("C:/Users/mdjit/OneDrive/Desktop/devlop/Heart-Failure-Prediction/trained_model.sav",'rb'))

    
    


def heart_failure_prediction(input_data):
    
    input_arr=np.array(input_data)
    inputs_array=input_arr.reshape(1,-1)
    inputs_array
    if (loaded_model.predict(inputs_array))==1:
        return "YOUR HEART HAS GOT FAILURE"
    else:
        return "YOUR HEART IS NOT FAILURED"
    
    
def main():  
    
    st.title("HEART FAILURE PREDICTION ")
    
 
    
    Age=st.number_input("Your age")
    Sex=["MALE","FEMALE"]
    st.selectbox("SEX",Sex)
    ChestPainType=["ATA","TA","ASY","NAP"]
    st.selectbox("CHEST PAIN TYPE",ChestPainType)
    RestingBP=st.number_input("RESTING BLOOD PRESSURE")
    Cholesterol=st.number_input("Cholestrol Rate")
    FastingBS=st.number_input("Fasting Blood Sugar")
    RestingECG=["NORMAL","ST","LVH"]
    st.selectbox("RESTING ECG",RestingECG)
    MaxHR=st.number_input("MAX Heart Rate")
    ExerciseAngina=["YES","NO"]
    st.selectbox("EXERCISE ANGINA",ExerciseAngina)
    Oldpeak=st.number_input("Old peak")
    ST_Slope=["UP","DOWN","FLAT"]
    st.selectbox("ST SLOPE",ST_Slope)
    
    diagnosis=""
    

    if (Sex=='F'or'f'or'FEMALE'or'Female'):
        Sex=0
    elif(Sex=='M'or'MALE'or'm','Male'):
        Sex=1
    else:
        print("Invalid Input")
    

    if (ChestPainType=='ATA'or 'Atypical Angina'or'ATYPICAL ANGINA'):
        ChestPainType=1
    elif(ChestPainType=='NAP'or'Non-Anginal Pain'or'NON-ANGINAL PAIN'):
        ChestPainType=2
    elif(ChestPainType=='ASY'or'Asymptomatic'or'ASYMPTOMATIC'):
        ChestPainType=0
    elif(ChestPainType=='TA'or'ta'or'Typical Angina'or 'TYPICAL ANGINA'):
        ChestPainType=3
    else:
        print("Invalid Input")
        

    
    if(RestingECG=='normal'or'NORMAL'or'Normal'):
        RestingECG=1
    elif(RestingECG=="ST"or'st'):
        RestingECG=2
    elif(RestingECG=='lvh'or'LVH'or'left ventricular hypertrophy'or'LEFT VENTRICULAR HYPERTROPHY'):
        RestingECG=0
    else:
        print("Invalid Input")
    

    if(ExerciseAngina=='n'or'no'or'NO'or'N'):
        ExerciseAngina=0
    elif(ExerciseAngina=='y'or'yes'or'Y'or'YES'):
        ExerciseAngina=1
    else:
        print("Invalid Input")
    

    if(ST_Slope=='down'or'Down'or'DOWN'):
        ST_Slope=0
    elif(ST_Slope=='up'or'UP'or'Up'):
        ST_Slope=1
    elif(ST_Slope=='flat'or'FLAT'or'Flat'):
        ST_Slope=2
    else:
        print("Invalid Input")


    if st.button("Heart Failure Test Result"):
        diagnosis = heart_failure_prediction([Age, Sex, ChestPainType,RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()

    
