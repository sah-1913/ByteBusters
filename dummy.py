import streamlit as st
import pandas as pd
import datetime

# Function to mark attendance
def mark_attendance(name):
    with open("attendance.csv", "a") as f:
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{name},{date_time}\n")

# Function to display attendance
def display_attendance():
    df = pd.read_csv("attendance.csv", names=["Name", "Time"])
    st.write(df)

# Main function
def main():
    st.title("Attendance System")

    # Sidebar
    st.sidebar.title("Menu")
    menu_selection = st.sidebar.radio("Select Option", ("Mark Attendance", "View Attendance"))

    if menu_selection == "Mark Attendance":
        st.header("Mark Attendance")
        name = st.text_input("Enter your name")
        if st.button("Mark"):
            mark_attendance(name)
            st.success(f"{name} marked attendance successfully!")

    elif menu_selection == "View Attendance":
        st.header("View Attendance")
        display_attendance()

if __name__ == "__main__":
    main()
