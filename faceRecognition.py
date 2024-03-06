import face_recognition
import cv2
import streamlit as st
import os
import numpy as np
from datetime import datetime

# Video capture
cap = cv2.VideoCapture(0)

# Load known students
known_students = {
    "Dhruve": face_recognition.load_image_file(r"content\Dhruve.jpg"),
    "Prasad": face_recognition.load_image_file(r"content\Prasad.jpg"),
    "Diya": face_recognition.load_image_file(r"content\Diya.jpg"),
    "Sakshi": face_recognition.load_image_file(r"content\Sakshi.jpg")
}