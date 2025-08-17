# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 03:01:09 2025

@author: likit
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))
heart_model=pickle.load(open('heart.sav','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))


#sidebar for navigation

with st.sidebar:
    
    selected= option_menu('Multiple Disease prediction system using ML',
                          ['Diabetes prediction',
                           'Heart disease prediction',
                           'Parkinsons prediction'],
                          
                          
                          icons=['bandaid','heart','person'],
                          
                          
                          default_index=0)
    
#diabetes prediction page
if(selected=='Diabetes prediction'):
    #page title
    st.title('Diabetes prediction using ML')
    
    
    #getting the input data from user 
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of pregnencies')
    with col2:
        Glucose=st.text_input('Glucose level of patient')
    with col3:
        BloodPreassure=st.text_input('Blood preassure of patient')
    with col1:
        Skinthickness=st.text_input('Skin thickness of patient')
    with col2:
        Insulin=st.text_input('Insulin value')
    with col3:
        BMI=st.text_input('BMI  value')
    with col1:
        DiabetesPedigreefunction=st.text_input('DIabetes pedigree fucntion value')
    with col2:
        Age=st.text_input('Age of patient')

    
    
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes test result'):
        diab_prediction=diabetes_model.predict([[float(Pregnancies),float(Glucose),float(BloodPreassure),float(Skinthickness),float(Insulin),float(BMI),float(DiabetesPedigreefunction),float(Age)]])
    
        if (diab_prediction[0]==1):
            diab_diagnosis='person is diabetic'
        else:
            diab_diagnosis='person is NOT diabetic'
            
    st.success(diab_diagnosis)
    
    
    
if(selected == 'Heart disease prediction'):
    st.title('Heart disease prediction using ML')
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('Age of patient')
    with col2:
        sex=st.text_input('sex of patient')
    with col3:
        cp=st.text_input('Chest pain value')
    with col1:
        trestbps=st.text_input('resting blood preassure')
    with col2:
        chol=st.text_input('serum cholestoral in mg/dl ')
    with col3:
        fbs=st.text_input('fasting blood sugar > 120 mg/dl')
    with col1:
        restecg=st.text_input('resting electrocardiographic results (values 0,1,2)')
    with col2:
        thalach=st.text_input('maximum heart rate achieved ')
    with col3:
        exang=st.text_input('exercise induced angina ')
    with col1:
        oldpeak=st.text_input('oldpeak = ST depression induced by exercise relative to rest ')
    with col2:
        slope =st.text_input('the slope of the peak exercise ST segment ')
    with col3:
        ca=st.text_input('number of major vessels (0-3) colored by flourosopy')     
    with col1:
        thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
        heart_diag=''
    if st.button('Heart disease test result'):
    
        heart_prediction=heart_model.predict([[float(age), float(sex), float(cp), float(trestbps),float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])
    
        if(heart_prediction[0]==1):
            heart_diag='person has heart disease'
        else:
            heart_diag='person has no heart disease'
        
    st.success(heart_diag)
    
if(selected == 'Parkinsons prediction'):
    st.title('Parkinsons prediction using ML')
    
    
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        Fo=st.text_input('Average vocal fundamental frequency value')
    with col2:
        Fhi=st.text_input('Maximum vocal fundamental frequency')
    with col3:
        Flo=st.text_input('Minimum vocal fundamental frequency')
    with col4:
        Jitter=st.text_input('Jitter(%)')
    with col5:
        Jitter_abs=st.text_input('Jitter(Abs)')
    with col1:
        RAP=st.text_input('RAP')
    with col2:
        PPQ=st.text_input('PPQ')
    with col3:
        jitter_DDP=st.text_input('Jitter:DDP')
    with col4:
        Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_db=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input('MDVP:APQ')
    with col4:
        DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')
        
        
    parkinsons_diag=''
        
    if st.button('parkinsons test result'):
        parkinsons_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter,Jitter_abs,RAP,PPQ,jitter_DDP,Shimmer,Shimmer_db,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(parkinsons_prediction[0]==0):
            parkinsons_diag='person does not have parkinsons disease'
        else:
            parkinsons_diag='person has parkinsons disease'
        
    st.success(parkinsons_diag)
    
    
    
    
    
    
    

    
