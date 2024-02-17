
import joblib
import streamlit as st
import category_encoders
import pandas as pd
import sklearn

Model= joblib.load("Model_Loan_Det_Final.pkl")
Inputs= joblib.load("Inputs_Loan_Det_Final.pkl")

def Gend(Gender):
    if Gender == 'Female':
        return int(0)
    else:
        return int(1)
    
def Marr(Married):
    if Married == 'No':
        return int(0)
    else:
        return int(1)
    
def Dep(Dependents):
    if Dependents == '3+':
        return int(3)
    else:
        return int(Dependents)

def Educ(Education):
    if Education == 'Graduate':
        return int(0)
    else:
        return int(1)

def Emp(Self_Employed):
    if Self_Employed == 'No':
        return int(0)
    else:
        return int(1)

def prediction(Gender,Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
               LoanAmount, Loan_Amount_Term, Credit_History, Property_Area ):
    gender=Gend(Gender)
    married=Marr(Married)
    dependents=Dep(Dependents)
    education=Educ(Education)
    employed=Emp(Self_Employed)
    test_df=pd.DataFrame(columns=Inputs)
    test_df.loc[0,'Gender']= gender
    test_df.loc[0,'Married']= married
    test_df.loc[0,'Dependents']= dependents
    test_df.loc[0,'Education']= education
    test_df.loc[0,'Self_Employed']= employed
    test_df.loc[0,'ApplicantIncome']= ApplicantIncome
    test_df.loc[0,'CoapplicantIncome']= CoapplicantIncome
    test_df.loc[0,'LoanAmount']= LoanAmount
    test_df.loc[0,'Loan_Amount_Term']= Loan_Amount_Term
    test_df.loc[0,'Credit_History']= Credit_History
    test_df.loc[0,'Property_Area']= Property_Area
    
    result= Model.predict(test_df)
    if result[0]== 0 :
        return st.text("Please,Don't Accept on Loan")
    else:
         return st.text("Please, Accept on Loan") 
        
def main():
    
    ## Setting up the page title
    st.set_page_config(page_title= 'Loan Detection Prediction')
    
     # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center;text-decoration: underline;color:GoldenRod'>Loan Detection Prediction</h1>", unsafe_allow_html=True)
    
    Gender=st.selectbox('Insert Gender',  ['Male','Female'])
    
    Married=st.selectbox('Are you married?',['Yes','No'])
    
    Dependents=st.selectbox('Select how many Dependents', ['0' ,'1' ,'2' ,'3+'])
    
    Education =st.selectbox('Select Education', ['Graduate','Not Graduate'])

    Self_Employed =st.selectbox('Are you employed', ['Yes', 'No'])

    ApplicantIncome=st.number_input('Insert ApplicantIncome in Thousands',min_value=100, max_value=30000, value=5000,step=500)
    
    CoapplicantIncome=st.number_input('Insert CoapplicantIncome in Thousands',min_value=0, max_value=40000, value=5000,step=500)
    
    LoanAmount=st.number_input('Insert LoanAmount in Thousands',min_value=9, max_value=1000, value=500,step=10)

    Loan_Amount_Term=st.slider('Choose Loan Amount Term in Months', min_value=10, max_value=400, value=12,step=10)

    Credit_History=st.radio(' Insert Credit_History', ['1', '0'])

    Property_Area=st.selectbox('Select Property Area', ['Urban', 'Rural', 'Semiurban'])
  
    
    if st.button('predict'):
        results= prediction(Gender,Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
               LoanAmount, Loan_Amount_Term, Credit_History, Property_Area )

if __name__ == '__main__':
    main()
