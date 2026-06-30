import streamlit as st, pandas as pd
from database import *
create_table()
st.title("Student Record Management System")
m=st.sidebar.selectbox("Menu",["Add","View"])
if m=="Add":
 n=st.text_input("Name");r=st.text_input("Roll");d=st.text_input("Department");y=st.selectbox("Year",["I","II","III","IV"]);e=st.text_input("Email");p=st.text_input("Phone")
 if st.button("Save"):
  add_student(n,r,d,y,e,p);st.success("Saved")
else:
 data=view_students()
 if data:
  df=pd.DataFrame(data,columns=["ID","Name","Roll","Department","Year","Email","Phone"])
  st.dataframe(df)
  st.download_button("Download CSV",df.to_csv(index=False),"students.csv","text/csv")
