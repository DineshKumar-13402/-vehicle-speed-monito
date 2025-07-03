
import streamlit as st
import cv2
from speed_estimation import estimate_speed

st.set_page_config(page_title='Vehicle Speed Monitor', layout='wide')
st.title("🚗 Vehicle Speed Tracking and Overspeed Detection")
st.markdown("Upload a traffic video to detect vehicles, estimate speed, and flag overspeeding.")

video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video_file:
    st.video(video_file)
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.read())
    st.write("Processing video...")
    result = estimate_speed("temp_video.mp4")
    st.write(result)
