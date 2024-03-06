import streamlit as st
import speech_recognition as sr
import csv
import pyttsx3

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
def update_attendance(roll_number, status, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_number, status])

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

        enrolled_students = {"1": "John", "2": "Alice", "3": "Bob", "4": "Emma"}
        attendance_filename = "attendance.csv"
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
                update_attendance(roll_number, status, attendance_filename)
                roll_call_output.append(f"{student_name}: present")
                st.success("Attendance marked.")
            else:
                roll_call_output.append(f"{student_name}: not present")
                st.error("Attendance not marked.")
        
        # Display the entire roll call process
        st.sidebar.header("Roll Call Summary")
        for output in roll_call_output:
            st.sidebar.write(output)
        
        st.sidebar.success("Roll Call Completed.")

if __name__ == "__main__":
    main()





