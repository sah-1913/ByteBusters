# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Function to display real-time attendance dashboard
# def attendance_dashboard(attendance_df):
#     st.title("Real-Time Attendance Dashboard")

#     # Display search bar for roll number
#     roll_number_search = st.text_input("Enter roll number to search:")

#     if roll_number_search:
#         roll_number_search = int(roll_number_search)
#         student_data = attendance_df[attendance_df["ROLL NO"] == roll_number_search]

#         if not student_data.empty:
#             st.write(f"### Attendance Graph for Roll Number: {roll_number_search}")
#             attendance_status = ["PRESENT" if student_data[f"DAY{i}"].iloc[0] == "PRESENT" else "ABSENT" for i in range(1, 8)]
#             plt.bar(range(1, 8), [1 if status == 'PRESENT' else 0 for status in attendance_status], color=['green' if status == 'PRESENT' else 'red' for status in attendance_status])
#             plt.xlabel("Day")
#             plt.ylabel("Attendance Status")
#             plt.title("Attendance Graph")
#             plt.xticks(range(1, 8))
#             st.pyplot(plt)
#         else:
#             st.warning(f"No data found for roll number {roll_number_search}")

#     # Analyze attendance trends
#     st.write("### Attendance Analysis and Reporting")
#     attendance_summary = attendance_df.iloc[:, 2:].apply(pd.Series.value_counts)
#     st.write("#### Attendance Summary")
#     st.write(attendance_summary)

#     # Generate attendance report
#     st.write("#### Attendance Report")
#     st.write("Download the attendance report as CSV:")
#     st.download_button(
#         label="Download Attendance Report",
#         data=attendance_summary.to_csv(),
#         file_name="attendance_report.csv",
#         mime="text/csv"
#     )

# # Main function
# def main():
#     st.set_page_config(page_title="Real-Time Attendance Dashboard", page_icon="📊")

#     # Sidebar
#     st.sidebar.title("Dashboard Settings")
#     uploaded_file = st.sidebar.file_uploader("Upload attendance data (CSV)", type="csv")

#     # Load attendance data
#     if uploaded_file is not None:
#         attendance_df = pd.read_csv(uploaded_file)
#         attendance_dashboard(attendance_df)

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Function to display real-time attendance dashboard
# def attendance_dashboard(attendance_df):
#     st.title("Real-Time Attendance Dashboard")

#     # Display search bar for roll number
#     roll_number_search = st.text_input("Enter roll number to search:")

#     if roll_number_search:
#         roll_number_search = int(roll_number_search)
#         student_data = attendance_df[attendance_df["ROLL NO"] == roll_number_search]

#         if not student_data.empty:
#             st.write(f"### Attendance Summary for Roll Number: {roll_number_search}")
#             attendance_status = student_data.iloc[0, 2:].value_counts()
#             st.write(f"Days Present: {attendance_status.get('PRESENT', 0)}")
#             st.write(f"Days Absent: {attendance_status.get('ABSENT', 0)}")
#         else:
#             st.warning(f"No data found for roll number {roll_number_search}")

#     # Analyze attendance trends for the whole class
#     st.write("### Class Attendance Analysis")
#     class_attendance_summary = attendance_df.iloc[:, 2:].apply(pd.Series.value_counts).transpose()
#     st.write("#### Attendance Summary")
#     st.write(class_attendance_summary)

#     # Plot a bar graph for the whole class attendance
#     st.write("#### Attendance Graph for the Whole Class")
#     class_attendance_summary.plot(kind='bar', stacked=True)
#     plt.xlabel("Students")
#     plt.ylabel("Number of Days")
#     plt.title("Class Attendance")
#     st.pyplot(plt)

# # Main function
# def main():
#     st.set_page_config(page_title="Real-Time Attendance Dashboard", page_icon="📊")

#     # Sidebar
#     st.sidebar.title("Dashboard Settings")
#     uploaded_file = st.sidebar.file_uploader("Upload attendance data (CSV)", type="csv")

#     # Load attendance data
#     if uploaded_file is not None:
#         attendance_df = pd.read_csv(uploaded_file)
#         attendance_dashboard(attendance_df)

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display real-time attendance dashboard
def attendance_dashboard(attendance_df):
    st.title("Real-Time Attendance Dashboard")

    # Display search bar for roll number
    roll_number_search = st.text_input("Enter roll number to search:")

    if roll_number_search:
        roll_number_search = int(roll_number_search)
        student_data = attendance_df[attendance_df["ROLL NO"] == roll_number_search]

        if not student_data.empty:
            st.write(f"### Attendance Summary for Roll Number: {roll_number_search}")
            attendance_status = student_data.iloc[0, 2:].value_counts()
            st.write(f"Days Present: {attendance_status.get('PRESENT', 0)}")
            st.write(f"Days Absent: {attendance_status.get('ABSENT', 0)}")
        else:
            st.warning(f"No data found for roll number {roll_number_search}")

    # Analyze attendance trends for the whole class
    st.write("### Class Attendance Analysis")

    # Prepare data for plotting
    attendance_summary = attendance_df.iloc[:, 2:].apply(pd.Series.value_counts).transpose()
    present_counts = attendance_summary.get('PRESENT', pd.Series([0] * len(attendance_summary)))
    absent_counts = attendance_summary.get('ABSENT', pd.Series([0] * len(attendance_summary)))

    # Plot a bar graph for the whole class attendance
    fig, ax = plt.subplots()
    index = range(1, len(attendance_summary) + 1)
    bar_width = 0.35
    opacity = 0.8

    rects1 = ax.bar(index, present_counts, bar_width, alpha=opacity, color='b', label='Present')
    rects2 = ax.bar(index, absent_counts, bar_width, alpha=opacity, color='r', bottom=present_counts, label='Absent')

    ax.set_xlabel('Roll Number')
    ax.set_ylabel('Number of Days')
    ax.set_title('Class Attendance')
    ax.set_xticks(index)
    ax.legend()

    st.write("#### Attendance Graph for the Whole Class")
    st.pyplot(fig)

# Main function
def main():
    st.set_page_config(page_title="Real-Time Attendance Dashboard", page_icon="📊")

    # Sidebar
    st.sidebar.title("Dashboard Settings")
    uploaded_file = st.sidebar.file_uploader("Upload attendance data (CSV)", type="csv")

    # Load attendance data
    if uploaded_file is not None:
        attendance_df = pd.read_csv(uploaded_file)
        attendance_dashboard(attendance_df)

if __name__ == "__main__":
    main()











