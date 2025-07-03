
# 🚗 Real-Time Vehicle Speed Monitor

This app uses computer vision to track vehicle speed and detect overspeeding using a traffic video. Built with OpenCV, YOLO, and Streamlit.

## Features
- Upload traffic video (.mp4)
- Detect vehicles and estimate speed
- Streamlit dashboard
- Overspeed alert system

## How to Run (Locally)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Cloud Deployment
1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud
3. Link your GitHub and choose this repo
4. Set `app.py` as the entry file
5. Deploy and get a public link
