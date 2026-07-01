import streamlit as st
import pandas as pd

from database import (
    create_table,
    add_student,
    get_students,
    search_student,
    update_student,
    delete_student,
    total_students,
    export_csv,
    export_excel,
)

from auth import login, logout, check_login


# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Student Record Management System",
    page_icon="🎓",
    layout="wide"
)

create_table()


# ------------------------------
# Login Check
# ------------------------------
if not check_login():
    login()
    st.stop()

logout()


# ------------------------------
# Title
# ------------------------------
st.title("🎓 Student Record Management System")
st.write("Manage student records easily using Streamlit & SQLite")


# ------------------------------
# Sidebar
# ------------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Student",
        "View Students",
        "Search Student",
        "Update Student",
        "Delete Student",
        "Export Data",
    ],
)


# ------------------------------
# Dashboard
# ------------------------------
if menu == "Dashboard":

    st.header("📊 Dashboard")

    total = total_students()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Students", total)

    with col2:
        st.info("Welcome Admin 👋")

    df = get_students()

    if not df.empty:
        st.subheader("Recent Records")
        st.dataframe(df.head(10), use_container_width=True)
    else:
        st.warning("No student records found.")


# ------------------------------
# Add Student
# ------------------------------
elif menu == "Add Student":

    st.header("➕ Add Student")

    name = st.text_input("Student Name")

    roll = st.text_input("Roll Number")

    department = st.selectbox(
        "Department",
        [
            "CSE",
            "IT",
            "ECE",
            "EEE",
            "MECH",
            "CIVIL",
        ],
    )

    year = st.selectbox(
        "Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year",
        ],
    )

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    if st.button("Save Student"):

        try:

            add_student(
                name,
                roll,
                department,
                year,
                email,
                phone,
            )

            st.success("✅ Student Added Successfully")

        except Exception as e:

            st.error(str(e))
         # ------------------------------
# View Students
# ------------------------------
elif menu == "View Students":

    st.header("👨‍🎓 Student Records")

    df = get_students()

    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No records found.")


# ------------------------------
# Search Student
# ------------------------------
elif menu == "Search Student":

    st.header("🔍 Search Student")

    roll = st.text_input("Enter Roll Number")

    if st.button("Search"):

        df = search_student(roll)

        if not df.empty:
            st.success("Student Found")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("Student Not Found")


# ------------------------------
# Update Student
# ------------------------------
elif menu == "Update Student":

    st.header("✏️ Update Student")

    roll = st.text_input("Enter Roll Number")

    if st.button("Load Student"):

        df = search_student(roll)

        if not df.empty:

            row = df.iloc[0]

            with st.form("update_form"):

                name = st.text_input("Student Name", row["name"])

                department = st.selectbox(
                    "Department",
                    ["CSE", "IT", "ECE", "EEE", "MECH", "CIVIL"],
                    index=["CSE","IT","ECE","EEE","MECH","CIVIL"].index(row["department"])
                    if row["department"] in ["CSE","IT","ECE","EEE","MECH","CIVIL"] else 0
                )

                year = st.selectbox(
                    "Year",
                    ["1st Year", "2nd Year", "3rd Year", "4th Year"],
                    index=["1st Year","2nd Year","3rd Year","4th Year"].index(row["year"])
                    if row["year"] in ["1st Year","2nd Year","3rd Year","4th Year"] else 0
                )

                email = st.text_input("Email", row["email"])

                phone = st.text_input("Phone", row["phone"])

                submit = st.form_submit_button("Update")

                if submit:

                    update_student(
                        name,
                        department,
                        year,
                        email,
                        phone,
                        roll,
                    )

                    st.success("✅ Student Updated Successfully")

        else:
            st.error("Student Not Found")


# ------------------------------
# Delete Student
# ------------------------------
elif menu == "Delete Student":

    st.header("🗑 Delete Student")

    roll = st.text_input("Enter Roll Number")

    if st.button("Delete"):

        df = search_student(roll)

        if not df.empty:

            delete_student(roll)

            st.success("Student Deleted Successfully")

        else:

            st.error("Student Not Found")


# ------------------------------
# Export Data
# ------------------------------
elif menu == "Export Data":

    st.header("📥 Export Student Data")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Export CSV"):

            export_csv()

            with open("students.csv", "rb") as file:
                st.download_button(
                    "⬇ Download CSV",
                    file,
                    file_name="students.csv",
                    mime="text/csv",
                )

    with col2:

        if st.button("Export Excel"):

            export_excel()

            with open("students.xlsx", "rb") as file:
                st.download_button(
                    "⬇ Download Excel",
                    file,
                    file_name="students.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
