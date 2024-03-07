import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display real-time attendance dashboard
def attendance_dashboard(attendance_df, face_recog_record_df, show_class_attendance):
    st.title("Real-Time Attendance Dashboard")

    attendance_summary = attendance_df[attendance_df.columns[3:]].apply(lambda col: col.str.upper())
    attendance_summary = attendance_summary.apply(pd.Series.value_counts).transpose()
    present_counts = attendance_summary.get('P', pd.Series([0] * len(attendance_summary)))

    if show_class_attendance:
        # Analyze attendance trends for the whole class
        st.write("### Class Attendance Analysis")

        # Plot a bar graph for the whole class attendance
        fig, ax = plt.subplots()
        index = range(1, len(attendance_summary) + 1)
        bar_width = 0.35
        opacity = 0.8

        rects = ax.bar(index, present_counts, bar_width, alpha=opacity, color='b', label='Present')

        ax.set_xlabel('Roll Number')
        ax.set_ylabel('Number of Lectures')
        ax.set_title('Class Attendance')
        ax.set_xticks(index)
        ax.set_yticks(range(int(max(present_counts)) + 2))
        ax.legend()

        st.write("#### Attendance Graph for the Whole Class")
        st.pyplot(fig)
    else:
        # Display search bar for roll number
        roll_number_search = st.text_input("Enter roll number to search:")

        if roll_number_search:
            roll_number_search = int(roll_number_search)

            # Total number of lectures attended
            lectures_attended = present_counts[roll_number_search-1]

            # Attendance percentage
            total_lectures = len(attendance_df)
            attendance_percentage = (lectures_attended / total_lectures) * 100

            # Display total lectures attended and attendance percentage for the specified roll number
            st.write(f"### Roll Number: {roll_number_search}")
            st.write(f"Total Lectures Attended: {lectures_attended}")
            st.write(f"Attendance Percentage: {attendance_percentage:.2f}%")

            # Display all data for the specified roll number from face_recog_record.csv
            st.write("### Roll Number Data from face_recog_record.csv")
            roll_data = face_recog_record_df[face_recog_record_df["Roll Number"] == roll_number_search]
            st.write(roll_data)

# Main function
def main():
    st.set_page_config(page_title="Real-Time Attendance Dashboard", page_icon="📊")

    # Sidebar
    st.sidebar.title("Dashboard Settings")
    uploaded_attendance_file = st.sidebar.file_uploader("Upload attendance data (CSV)", type="csv")
    show_class_attendance = st.sidebar.radio("Show:", ("Class Attendance", "Individual Roll Number"))

    # Load attendance data
    if uploaded_attendance_file is not None:
        attendance_df = pd.read_csv(uploaded_attendance_file)
        face_recog_record_df = pd.read_csv("face_recog_records.csv")
        attendance_dashboard(attendance_df, face_recog_record_df, show_class_attendance == "Class Attendance")

if __name__ == "__main__":
    main()
