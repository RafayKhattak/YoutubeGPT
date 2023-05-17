# Import required libraries
import streamlit as st
import whisper
import os
import openai
from pytube import YouTube

@st.cache_resource
def load_model():
    # Load the Whisper model for speech recognition
    model = whisper.load_model("base")
    return model

def save_video(url):
    # Download the YouTube video
    youtube_obj = YouTube(url)
    youtube_obj = youtube_obj.streams.get_highest_resolution()
    try:
        video_path = youtube_obj.download()
    except:
        print("An error has occurred")
    print("Download completed successfully")
    
    # Rename and move the downloaded video file
    if os.path.exists("video.mp4"):
        os.remove("video.mp4")

    base_name, ext = os.path.splitext(video_path)
    old_name = base_name + ext
    new_name = "video.mp4"
    os.rename(old_name, new_name)
    return new_name


def save_audio(url, destination, file_name):
    # Download the audio from the YouTube video
    if os.path.exists("audio.mp3"):
        os.remove("audio.mp3")
        
    video = YouTube(url)
    audio = video.streams.filter(only_audio=True).first()
    output_path = audio.download(output_path=".")
    new_file_name = file_name + '.mp3'
    os.rename(output_path, new_file_name)


def audio_to_transcript():
    # Transcribe the audio using the Whisper model
    model = load_model()
    result = model.transcribe("audio.mp3")
    transcript = result["text"]
    return transcript

def text_to_prompt(query):
    # Generate a prompt using OpenAI's GPT-3 model
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Explain and summarize the following text as concisely as possible with minimal detail loss: " + query,
        temperature=0.7,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']
