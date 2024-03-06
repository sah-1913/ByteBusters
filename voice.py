import streamlit as st
import speech_recognition as sr
import csv
import pyttsx3
from datetime import datetime
import pandas as pd

# Function to recognize speech
def recognize_present(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.write(f"Listening for 'present' for {timeout} seconds...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=timeout)
    
    try:
        spoken_word = recognizer.recognize_google(audio_data)
        if "present" in spoken_word.lower():
            st.sidebar.success("Student is present.")
            return "present"
        else:
            st.sidebar.error("Did not recognize 'present'.")
            return None
    except sr.UnknownValueError:
        st.sidebar.error("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        st.sidebar.error(f"Could not request results from Google Speech Recognition service: {e}")
        return None

# Function to update attendance
def update_attendance(roll_number, status, df):
    df.loc[len(df)] = [roll_number, status]
    df.to_csv('Roll_call.csv', index=False)

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit app
def main():
    st.set_page_config(page_title="Voice Recognition Roll Call", page_icon="🎤")
    st.title("Voice Recognition Roll Call")

    # Sidebar
    st.sidebar.header("Settings")
    if st.sidebar.button("Start Roll Call"):
        st.sidebar.success("Roll Call Started...")

        enrolled_students = {"1": "Dhruve", "2": "Prasad", "3": "Sakshi", "4": "Diya"}
        Roll_call_df = pd.read_csv('Roll_call.csv')
        face_recog = pd.read_csv('attendance_records.csv')
        attendance = pd.read_csv('attendance.csv')
        roll_call_output = []  # List to store roll call results
        
        for roll_number in enrolled_students.keys():
            st.sidebar.write(f"### Roll Number: {roll_number}")
            speak(f"Roll Number {roll_number}")
            student_name = enrolled_students[roll_number]
            st.write(f"Calling {student_name}...")
            st.sidebar.write("Please say 'present' when called.")
            st.sidebar.write("Listening...")
            status = recognize_present(timeout=5)  # Increase timeout to 10 seconds
            if status:
                update_attendance(roll_number, status, Roll_call_df)
                roll_call_output.append(f"{student_name}: present")
                st.success("Attendance marked.")

                current_date = datetime.now().strftime("%d-%m-%Y")
                for index, row in face_recog.iterrows():
                    if int(roll_number) == row[0]:
                        if current_date in attendance["Date"].values:
                            attendance.loc[attendance['Date'] == current_date, roll_number] = 'Present'
                        else:
                            new_row = {'Date': current_date, roll_number: 'Present'}
                            attendance = attendance.append(new_row, ignore_index=True)
                        attendance.to_csv('attendance.csv', index=False)
                        break
                    # print(row[0], roll_number)
                    # if current_date in attendance["Date"].values:
                    #     attendance.loc[attendance['Date'] == current_date, roll_number] = 'Present'
                    #     attendance.to_csv('attendance.csv', index=False)
                    #     break
                    # else:
                    #     new_row = {'Date': current_date, roll_number: 'Present'}
                    #     attendance = attendance.append(new_row, ignore_index=True)
                    #     attendance.to_csv('attendance.csv', index=False)
                    #     break
            else:
                current_date = datetime.now().strftime("%d-%m-%Y")
                roll_call_output.append(f"{student_name}: not present")
                st.error("Attendance not marked.")
                if current_date in attendance["Date"].values:
                    attendance.loc[attendance['Date'] == current_date, roll_number] = 'Absent'
                else:
                    new_row = {'Date': current_date, roll_number: 'Absent'}
                    attendance = attendance.append(new_row, ignore_index=True)
                attendance.to_csv('attendance.csv', index=False)
        
        # Display the entire roll call process
        st.sidebar.header("Roll Call Summary")
        for output in roll_call_output:
            st.sidebar.write(output)
        
        st.sidebar.success("Roll Call Completed.")
        empty_roll_call = pd.DataFrame(columns=["Roll Number", "Attendance"])
        empty_roll_call.to_csv('Roll_call.csv', index=False)

if __name__ == "__main__":
    main()