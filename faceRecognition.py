import face_recognition
import cv2
import numpy as np
from datetime import datetime
import csv
import streamlit as st

def main():
    st.title("Webcam and Microphone Checker")

    # Check Webcam
    st.header("Webcam Check")
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Unable to access webcam.")
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
                else:
                    st.error("Failed to capture picture.")
        cap.release()
    except Exception as e:
        st.error(f"Error: {e}")
    
    # Load the stored image for face recognition
    image_path = "captured_image.jpg"
    stored_image = cv2.imread(image_path)
    
    # Load known students
    known_students = {
        "01": face_recognition.load_image_file(r"content\Dhruve.jpg"),
        "02": face_recognition.load_image_file(r"content\Prasad.jpg"),
        "03": face_recognition.load_image_file(r"content\Sakshi.jpg"),
        "04": face_recognition.load_image_file(r"content\Diya.jpg"),
    }
    
    encoded_students = {
        "01": face_recognition.face_encodings(known_students["01"])[0],
        "02": face_recognition.face_encodings(known_students["02"])[0],
        "03": face_recognition.face_encodings(known_students["03"])[0],
        "04": face_recognition.face_encodings(known_students["04"])[0],
    }
    
    face_locations = []
    face_encodings = []
    face_names = [] 
    
    # Open CSV file for writing
    f = open("face_recog.csv", "w+", newline="")
    lnwriter = csv.writer(f)
    
    # Perform face recognition on the stored image
    face_locations = face_recognition.face_locations(stored_image)
    face_encodings = face_recognition.face_encodings(stored_image, face_locations)
    face_names = []
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(list(encoded_students.values()), face_encoding)
        name = ""
        face_distances = face_recognition.face_distance(list(encoded_students.values()), face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = list(encoded_students.keys())[best_match_index]
        
        face_names.append(name)
    
        if name in list(encoded_students.keys()):
            current_date = datetime.now().strftime("%Y-%m-%d")
            with open("face_recog.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == name and row[1] == current_date:
                        break
                else:
                    lnwriter.writerow([name, current_date])
    
    # Close CSV file
    f.close()

if __name__ == "__main__":
    main()