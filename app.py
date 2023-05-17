# Import required libraries
import streamlit as st
import openai
from model import save_video, save_audio, audio_to_transcript, text_to_prompt

# Get API key 
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set page configuration and title for Streamlit
st.set_page_config(page_title="YoutubeGPT", page_icon="📼", layout="wide")

# Add header with title and description
st.markdown(
    '<p style="display:inline-block;font-size:40px;font-weight:bold;">📺YoutubeGPT</p> <p style="display:inline-block;font-size:16px;">YoutubeGPT is a webapp tool that utilizes OpenAI&#39;s Whisper model for speech recognition to extract transcriptions from YouTube videos. It also incorporates GPT-3 to provide users with summarized text based on the content of the video.<br><br></p>',
    unsafe_allow_html=True
)

# Get YouTube video URL from user
url = st.text_input('Enter URL of YouTube video:')

if url is not None:
    if st.button("Generate"):
        # Create columns for displaying video, transcription, and summarized text
        col1, col2, col3 = st.columns([1, 1, 1])
        
        # Column 1: Video display
        with col1:
            st.info("Video uploaded successfully")
            text = "It might take some time...."
            st.text(text)
            video_filename = save_video(url)
            st.video(video_filename)
        
        # Column 2: Video transcription
        with col2:
            st.info("Video Transcription:")
            save_audio(url, ".", "audio")
            transcript_result = audio_to_transcript()
            st.markdown(f"<div style='height: 200px; overflow-y: scroll;'>{transcript_result}</div>", unsafe_allow_html=True)
        
        # Column 3: Summarized text
        with col3:
            st.info("Summarized Text")
            result = text_to_prompt(transcript_result)
            st.success(result)

# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# Apply CSS code to hide header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)