import streamlit as st

# Default Admin Credentials
USERNAME = "admin"
PASSWORD = "admin123"


def login():
    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.success("✅ Login Successful")
            st.rerun()
        else:
            st.error("❌ Invalid Username or Password")


def logout():
    if st.sidebar.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.rerun()


def check_login():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    return st.session_state["logged_in"]
