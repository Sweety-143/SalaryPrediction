import pickle
import streamlit as st
pickle_in=open('SalaryPrediction.pkl','rb')
model=pickle.load(pickle_in)
e=st.number_input('Enter Expirence')
if st.button('PREDICT'):
  s=model.predict([[e]]).squeeze()
  st.success(f'Salary is {s}')
               
