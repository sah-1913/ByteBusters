# import streamlit as st
# import cv2
# import numpy as np

# def detect_faces(image):
#     # Load pre-trained face detection model
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Detect faces
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw rectangles around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     return image

# def main():
#     st.title("Face Detection using OpenCV in Streamlit")

#     # Open webcam
#     cap = cv2.VideoCapture(0)

#     # Display webcam feed
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             st.error("Failed to capture video.")
#             break

#         # Convert frame to RGB for Streamlit
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Detect faces
#         frame_with_faces = detect_faces(frame)

#         # Display the frame with faces
#         st.image(frame_with_faces, channels="RGB", use_column_width=True)

#         # Close webcam when 'Stop' button is clicked
#         if st.button("Stop"):
#             break

#     # Release the webcam and close the window
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()


# 

# import cv2
# import numpy as np
# from datetime import datetime
# import pandas as pd
# import streamlit as st
# import face_recognition

# def main():
#     st.title("Real-Time Face Recognition Attendance System")

#     # Check Webcam
#     st.header("Webcam Check")
#     try:
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             st.error("Unable to access webcam.")
#             return
#         else:
#             st.success("Webcam is working properly.")
#             if st.button("Take Picture"):
#                 ret, frame = cap.read()
#                 if ret:
#                     # Save the captured image
#                     image_path = "captured_image.jpg"
#                     cv2.imwrite(image_path, frame)
#                     st.success("Picture captured successfully!")
#                     # Display the captured image
#                     st.image(image_path)
#                 else:
#                     st.error("Failed to capture picture.")
#         cap.release()
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return
    
#     # Load known students
#     known_students = {
#         "01": {"name": "Dhruve", "image_path": r"content\Dhruve.jpeg"},
#         "02": {"name": "Prasad", "image_path": r"content\Prasad.jpeg"},
#         "03": {"name": "Sakshi", "image_path": r"content\Sakshi.jpeg"},
#         "04": {"name": "Diya", "image_path": r"content\Diya.jpeg"},
#     }
    
#     # Load stored image for face recognition
#     image_path = "captured_image.jpg"
#     stored_image = cv2.imread(image_path)
    
#     # Encode known students
#     encoded_students = {}
#     for roll_number, student_info in known_students.items():
#         student_image = face_recognition.load_image_file(student_info["image_path"])
#         encoded_students[roll_number] = face_recognition.face_encodings(student_image)[0]
    
#     # Perform face recognition on the stored image
#     face_locations = face_recognition.face_locations(stored_image)
#     face_encodings = face_recognition.face_encodings(stored_image, face_locations)
    
#     # Create a pandas DataFrame to store face recognition results
#     df = pd.DataFrame(columns=["Roll Number", "Name", "Date", "Attendance"])

#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(list(encoded_students.values()), face_encoding)
#         roll_number = ""
#         if True in matches:
#             match_index = matches.index(True)
#             roll_number = list(encoded_students.keys())[match_index]
#             current_date = datetime.now().strftime("%Y-%m-%d")
#             df = df.append({"Roll Number": roll_number, "Name": known_students[roll_number]["name"], "Date": current_date, "Attendance": "Present"}, ignore_index=True)
#         else:
#             st.warning("Unknown face detected. Attendance not recorded.")
    
#     # Save the DataFrame to a CSV file
#     df.to_csv("attendance_records.csv", index=False)

#     # Display attendance analysis and reporting
#     st.header("Attendance Analysis and Reporting")
#     st.write("Attendance records saved successfully.")

#     # Generate attendance report
#     st.write("Download the attendance report:")
#     st.download_button(
#         label="Download Attendance Report",
#         data=df.to_csv(index=False).encode(),
#         file_name="attendance_report.csv",
#         mime="text/csv"
#     )

# if __name__ == "__main__":
#     main()
    
    
    

# import cv2
# import numpy as np
# from datetime import datetime
# import pandas as pd
# import streamlit as st
# import face_recognition
# import os

# def main():
#     st.title("Real-Time Face Recognition Attendance System")

#     # Check Webcam
#     st.header("Webcam Check")
#     try:
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             st.error("Unable to access webcam.")
#             return
#         else:
#             st.success("Webcam is working properly.")
#             if st.button("Take Picture"):
#                 ret, frame = cap.read()
#                 if ret:
#                     # Save the captured image
#                     image_path = "captured_image.jpg"
#                     cv2.imwrite(image_path, frame)
#                     st.success("Picture captured successfully!")
#                     # Display the captured image
#                     st.image(image_path)
#                 else:
#                     st.error("Failed to capture picture.")
#         cap.release()
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return
    
#     # Load known students
#     known_students = {
#         "01": {"name": "Dhruve", "image_path": r"content\Dhruve.jpeg"},
#         "02": {"name": "Prasad", "image_path": r"content\Prasad.jpeg"},
#         "03": {"name": "Sakshi", "image_path": r"content\Sakshi.jpeg"},
#         "04": {"name": "Diya", "image_path": r"content\Diya.jpeg"},
#     }
    
#     # Load stored image for face recognition
#     image_path = "captured_image.jpg"
#     stored_image = cv2.imread(image_path)
    
#     # Encode known students
#     encoded_students = {}
#     for roll_number, student_info in known_students.items():
#         student_image = face_recognition.load_image_file(student_info["image_path"])
#         encoded_students[roll_number] = face_recognition.face_encodings(student_image)[0]
    
#     # Perform face recognition on the stored image
#     face_locations = face_recognition.face_locations(stored_image)
#     face_encodings = face_recognition.face_encodings(stored_image, face_locations)
    
#     # Load existing attendance records or create new DataFrame
#     if os.path.exists("attendance_records.csv"):
#         df = pd.read_csv("attendance_records.csv")
#     else:
#         df = pd.DataFrame(columns=["Roll Number", "Name", "Date", "Attendance"])

#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(list(encoded_students.values()), face_encoding)
#         roll_number = ""
#         if True in matches:
#             match_index = matches.index(True)
#             roll_number = list(encoded_students.keys())[match_index]
#             current_date = datetime.now().strftime("%Y-%m-%d")
#             # Check if the entry already exists in the DataFrame
#             if not ((df["Roll Number"] == roll_number) & (df["Date"] == current_date)).any():
#                 df = df.append({"Roll Number": roll_number, "Name": known_students[roll_number]["name"], "Date": current_date, "Attendance": "Present"}, ignore_index=True)
#         else:
#             st.warning("Unknown face detected. Attendance not recorded.")
    
#     # Save the DataFrame to a CSV file
#     df.to_csv("attendance_records.csv", index=False)

#     # Display attendance analysis and reporting
#     st.header("Attendance Analysis and Reporting")
#     st.write("Attendance records saved successfully.")

#     # Generate attendance report
#     st.write("Download the attendance report:")
#     st.download_button(
#         label="Download Attendance Report",
#         data=df.to_csv(index=False).encode(),
#         file_name="attendance_report.csv",
#         mime="text/csv"
#     )

# if __name__ == "__main__":
#     main()


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
                else:
                    st.error("Failed to capture picture.")
        cap.release()
    except Exception as e:
        st.error(f"Error: {e}")
        return
    
    # Load known students
    known_students = {
        "01": {"name": "Dhruve", "image_path": r"content\Dhruve.jpeg"},
        "02": {"name": "Prasad", "image_path": r"content\Prasad.jpeg"},
        "03": {"name": "Sakshi", "image_path": r"content\Sakshi.jpeg"},
        "04": {"name": "Diya", "image_path": r"content\Diya.jpeg"},
    }
    
    # Load stored image for face recognition
    image_path = "captured_image.jpg"
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
    if os.path.exists("attendance_records.csv"):
        df = pd.read_csv("attendance_records.csv")
    else:
        df = pd.DataFrame(columns=["Roll Number", "Name", "Date", "Attendance"])

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(list(encoded_students.values()), face_encoding)
        roll_number = ""
        if True in matches:
            match_index = matches.index(True)
            roll_number = list(encoded_students.keys())[match_index]
            current_date = datetime.now().strftime("%Y-%m-%d")
            # Check if the entry already exists in the DataFrame
            if not ((df["Roll Number"] == roll_number) & (df["Date"] == current_date)).any():
                df = df.append({"Roll Number": roll_number, "Name": known_students[roll_number]["name"], "Date": current_date, "Attendance": "Present"}, ignore_index=True)
        else:
            st.warning("Unknown face detected. Attendance not recorded.")
    
    # Save the DataFrame to a CSV file
    df.to_csv("attendance_records.csv", index=False)

    # Display attendance analysis and reporting
    st.header("Attendance Analysis and Reporting")
    st.write("Attendance records saved successfully.")

    # Generate attendance report
    st.write("Download the attendance report:")
    st.download_button(
        label="Download Attendance Report",
        data=df.to_csv(index=False).encode(),
        file_name="attendance_report.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()
