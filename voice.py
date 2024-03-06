import streamlit as st
import speech_recognition as sr
import csv

def recognize_present():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening for 'present'...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
    
    try:
        spoken_word = recognizer.recognize_google(audio_data)
        if "present" in spoken_word.lower():
            st.write("Student is present.")
            return "present"
        else:
            st.write("Did not recognize 'present'.")
            return None
    except sr.UnknownValueError:
        st.write("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        st.write("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def update_attendance(student_name, status, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_name, status])

if __name__ == "__main__":
    # Streamlit app
    st.title("Voice Recognition Roll Call")
    st.write("Press the button and say 'present' to mark your attendance.")

    student_name = st.text_input("Enter your name:")
    attendance_filename = "attendance.csv"
    
    if st.button("Record"):
        status = recognize_present()
        if status:
            update_attendance(student_name, status, attendance_filename)
