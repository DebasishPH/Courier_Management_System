from google.protobuf.descriptor import DescriptorBase
from numpy import object_
import streamlit as st
from PIL import Image
from streamlit.proto.RootContainer_pb2 import DESCRIPTOR
import ddl
import dml
import dql 
import login_sys as ls
import random
import pandas as pd
from plotly import graph_objects as go
from streamlit import caching
ddl.create_data()

def emp_login():
    caching.clear_cache()
    list = ['Update Data', 'Delete Data', 'Show Data', 'Search Data']
    typ = ['Heavy', 'Medium', 'Light']
    s = st.selectbox("Choose ",list)
    if s=='Update Data':
        i=st.text_input("Enter ID of Courier : ")
        if len(i)==0:
            st.write("")
        elif len(i)!=0 and dml.check_courier(i)==0:
            st.write("ID DOES NOT EXISTS")
        else:
            with st.form(key='courier_form'):
                og = st.text_input("Enter New Origin ")
                ds = st.text_input("Enter New Destination ")
                dt = st.text_input("Enter New Date in YYYY-MM-DD")
                t = st.selectbox("Select New Package Type", typ)
                s_b=st.form_submit_button(label='Submit')
                if s_b==True:
                    if dml.updt_courier(i,og,ds,dt,t):
                        st.write("Successfully Updated")
                    else:
                        st.write("Update Couldnt Be Made")
               

    elif s=='Show Data':
       caching.clear_cache()
       try:
        res=dql.show_c_det()
        df=pd.DataFrame(res)
        df.columns=['ID','From','To','Booked','Expected','Name','Number']
        st.write(df)
       except:
           st.write("No Data Found")

    elif s=='Search Data':
        caching.clear_cache()
        i=st.text_input("Enter ID of Courier : ")
        b = st.button(label="Submit")
        if b == True:
            if len(i)!=0 and dml.check_courier(i)==0:
                st.write("ID DOES NOT EXISTS")
            else:
                og, d, dt, nm, ph = dql.show_r_details(i)
                t=[{str(nm)},{str(ph)},{str(d)},{str(og)},{str(dt)}]
                df=pd.DataFrame(t)
                df.columns=['Value']
                df.index=['Name of Receiver','Phone of Receiver','Destination','Origin','Expected Date']
                st.table(df)
        

    elif s=='Delete Data':
            caching.clear_cache()
            i=st.text_input("Enter ID of Courier : ")  
            if len(i)==0:
                st.write("")
            elif len(i)!=0 and dml.check_courier(i)==0:
                st.write("ID DOES NOT EXISTS")
            else:
                o, d, dt, nm, ph = dql.show_r_details(i)
                t=[{str(nm)},{str(ph)},{str(d)},{str(o)},{str(dt)}]
                df=pd.DataFrame(t)
                df.columns=['Value']
                df.index=['Name of Receiver','Phone of Receiver','Destination','Origin','Expected Date']
                st.write("Following Data Will Be Deleted")
                st.write(df)
                b_s=st.button(label="CONFIRM")
                if b_s==True:
                    val=dml.del_data(i)
                    if val==1:
                        st.write("Deleted Successfully")
                    else:
                        st.write("Could not Delete Data")

def user_login():
    caching.clear_cache()
    list = ['New Courier', 'Check Status']
    typ = ['Heavy', 'Medium', 'Light']
    s = st.selectbox('Please Choose', list)
    if s == 'New Courier':
        caching.clear_cache()
        with st.form(key='courier_form'):
            nm = st.text_input("Enter Receiver's Name ")
            ph = st.text_input("Enter Receiver Phone ")
            og = st.text_input("Enter Origin ")
            ds = st.text_input("Enter Destination ")
            dt = st.text_input("Enter Date in YYYY-MM-DD")
            t = st.selectbox("Enter Package Type", typ)
            st.write("Heavy Package >15kg ")
            st.write("Medium Package >=5kg and <=15kg ")
            st.write("Light Package <5kg")
            s_b = st.form_submit_button(label='Submit')
            if(s_b == True):
                id = dml.insert_data_c_details(og, ds)
                dml.insert_data_c_og(id, dt, t)
                dml.insert_data_c_receiver(id, nm, ph)
                st.write("YOUR TRACKING ID : ", id)

    if s == 'Check Status':
        caching.clear_cache()
        i = st.text_input("Enter Tracking ID")
        b = st.button(label="Submit")
        if b == True:
            o, d, dt, nm, ph = dql.show_r_details(i)
            st.write("Name of Receiver :", nm)
            st.write("Phone of Receiver :", ph)
            st.write("Destination :", d)
            st.write("Origin  :", o)
            st.write("Estimated Delivery Date :",dt)


st.markdown("<h1 style='text-align: center; color: white;'>SHIPFAST</h1>",
            unsafe_allow_html=True)

option = st.sidebar.title("SHIPFAST")
original_list = ['HOME', 'LOGIN', 'EMPLOYEE LOGIN', 'REGISTER']
result = st.sidebar.selectbox('WELCOME', original_list)


if result == 'HOME':
    img = Image.open("img.jpg")
    st.image(img)
    st.write("India's Leading Courier Service")

if result == 'LOGIN':
    caching.clear_cache()
    with st.sidebar.form(key='my_form'):
        id = st.text_input(label='ENTER ID')
        pw = st.text_input(label='ENTER PASSWORD', type="password")
        s_b = st.form_submit_button(label='Submit')
    if len(id) != 0 and len(pw) != 0:
        text = ls.check_login(id, pw)
        if text == "ERROR":
            st.sidebar.write("Wrong Id or Password!!")
        else:
            st.write("Welcome ", text)
            user_login()


if result == 'EMPLOYEE LOGIN':
    caching.clear_cache()
    with st.sidebar.form(key='my_form'):
        id = st.text_input(label='ENTER ID')
        pw = st.text_input(label='ENTER PASSWORD', type="password")
        s_b = st.form_submit_button(label='Submit')
    if len(id) != 0 and len(pw) != 0:
        text = ls.check_login_emp(id, pw)
        if text == "ERROR":
            st.sidebar.write("Wrong Id or Password!!")
        else:
            st.write("Welcome ", text)
            emp_login()


if result == 'REGISTER':
    caching.clear_cache()
    list = ['CUSTOMER', 'EMPLOYEE']
    sel = st.selectbox("", list)
    if sel == 'CUSTOMER':
        caching.clear_cache()
        with st.form(key='my_form'):
            nm = st.text_input(label='ENTER NAME')
            id = st.text_input(label='ENTER ID')
            pw = st.text_input(label='ENTER PASSWORD', type="password")
            pw2 = st.text_input(label='RE ENTER PASSWORD', type="password")
            s_b = st.form_submit_button(label='Submit')
            if s_b == True and len(pw) != 0 and len(nm) != 0 and len(pw2) != 0:
                if pw == pw2:
                    if(dml.user_det(nm, id, pw)):
                        st.write("Successfully Registered")
                    else:
                        st.write("User Already Exists")
                else:
                    st.write("Passwords dont match")
    elif sel == 'EMPLOYEE':
        caching.clear_cache()
        sk = st.text_input("Enter Secret Key :", type="password")
        if sk == "#567@shipfast":
            nm = st.text_input(label='ENTER NAME')
            ph = st.text_input(label='ENTER PHONE')
            pw = st.text_input(label='ENTER PASSWORD', type="password")
            pw2 = st.text_input(label='RE ENTER PASSWORD', type="password")
            s_b = st.button(label='Submit')
            if s_b == True and len(pw) != 0 and len(nm) != 0 and len(pw2) != 0 and len(ph) != 0:
                if pw == pw2:
                    i = dml.staff_det(nm, pw, ph)
                    if i != 0:
                        st.write("Successfully Registered")
                        st.write("Generated ID :", i)
                    else:
                        st.write("Wrong Input")
                else:
                    st.write("Passwords dont match")
