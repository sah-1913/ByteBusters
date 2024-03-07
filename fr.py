import cv2
import numpy as np
from datetime import datetime
import pandas as pd
import streamlit as st
import face_recognition
import os

def main():
    st.title("Real-Time Face Recognition Attendance System")

    # Check Webcam
    st.header("Webcam Check")
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Unable to access webcam.")
            return
        else:
            st.success("Webcam is working properly.")
            if st.button("Take Picture"):
                ret, frame = cap.read()
                if ret:
                    # Save the captured image
                    image_path = "captured_image.jpg"
                    cv2.imwrite(image_path, frame)
                    st.success("Picture captured successfully!")
                    # Display the captured image
                    st.image(image_path)

                    # Load known students
                    known_students = {
                        "01": {"name": "Dhruve", "image_path": r"content\Dhruve.jpg"},
                        "02": {"name": "Prasad", "image_path": r"content\Prasad.jpg"},
                        "03": {"name": "Sakshi", "image_path": r"content\Sakshi.jpg"},
                        "04": {"name": "Diya", "image_path": r"content\Diya.jpg"},
                    }
                    
                    stored_image = cv2.imread(image_path)
                    
                    # Encode known students
                    encoded_students = {}
                    for roll_number, student_info in known_students.items():
                        student_image = face_recognition.load_image_file(student_info["image_path"])
                        encoded_students[roll_number] = face_recognition.face_encodings(student_image)[0]
                    
                    # Perform face recognition on the stored image
                    face_locations = face_recognition.face_locations(stored_image)
                    face_encodings = face_recognition.face_encodings(stored_image, face_locations)
                    
                    # Load existing attendance records or create new DataFrame
                    if os.path.exists("face_recog_records.csv"):
                        df = pd.read_csv("face_recog_records.csv")
                    else:
                        df = pd.DataFrame(columns=["Roll Number", "Name", "Date", "Time", "Attendance"])

                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(list(encoded_students.values()), 
                                                                 face_encoding)
                        roll_number = ""
                        if True in matches:
                            match_index = matches.index(True)
                            roll_number = list(encoded_students.keys())[match_index]
                            current_date = datetime.now().strftime("%d-%m-%Y")
                            current_time = datetime.now().strftime("%H:%M:%S")
                            # Check if the entry already exists in the DataFrame
                            if not ((df["Roll Number"] == roll_number)
                                     & (df["Date"] == current_date)).any():
                                df = df.append({"Roll Number": roll_number, 
                                                "Name": known_students[roll_number]["name"], 
                                                "Date": current_date,
                                                "Time": current_time, 
                                                "Attendance": "Present"}, ignore_index=True)
                        else:
                            st.warning("Unknown face detected. Attendance not recorded.")
                    
                    # Save the DataFrame to a CSV file
                    df.to_csv("face_recog_records.csv", index=False)
                else:
                    st.error("Failed to capture picture.")
                    return
        cap.release()
    except Exception as e:
        st.error(f"Error: {e}")
        return

if __name__ == "__main__":
    main()