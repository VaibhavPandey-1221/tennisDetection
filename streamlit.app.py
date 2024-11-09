import streamlit as st
import tempfile

st.title("Tennis Game Tracking")

# Layout: 2 columns - Column 1 for video, Column 2 for buttons
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Video")
    if "uploaded_video" in st.session_state:
        # If video is uploaded, display it
        st.video(st.session_state.uploaded_video)

with col2:
    st.subheader("Controls")
    
    # Button to trigger file selection
    if st.button("Select Input File"):
        st.session_state.show_uploader = True  # Display the uploader if the button is clicked
    
    # Conditionally display the file uploader
    if st.session_state.get("show_uploader", False):
        uploaded_video = st.file_uploader("Browse and select a video", type=["mp4", "mov", "avi", "mkv"], key="video_uploader")
        if uploaded_video:
            # Save the uploaded video in session state to display in the first column
            temp_video = tempfile.NamedTemporaryFile(delete=False)
            temp_video.write(uploaded_video.read())
            st.session_state.uploaded_video = temp_video.name
    
    st.button("Preview Video")
    progress = st.slider("Progress", min_value=0, max_value=100, value=20)
    st.button("Process Video")
    st.button("Show Output")
    st.button("Download Output")
