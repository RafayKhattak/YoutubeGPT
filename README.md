# YoutubeGPT

YoutubeGPT is a web application that utilizes OpenAI's state-of-the-art models to enhance the accessibility and comprehension of YouTube videos. By leveraging the power of Whisper, a general-purpose speech recognition model, and GPT-3, a language model capable of generating human-like text, YoutubeGPT extracts transcriptions from YouTube videos and provides users with concise and accurate summaries based on the video content.

## Features

- **Speech Recognition**: YoutubeGPT employs OpenAI's Whisper model to transcribe the audio content of YouTube videos, ensuring accurate and reliable speech-to-text conversion.

- **Summarization**: Leveraging GPT-3, YoutubeGPT generates concise summaries of the video content, enabling users to quickly grasp the main points without having to watch the entire video.

- **User-Friendly Interface**: The web application offers a user-friendly interface where users can simply enter the URL of the YouTube video they want to process and receive the transcription and summarized text promptly.

## Getting Started

To run YoutubeGPT locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Install ffmpeg, which is required for audio processing. You can download ffmpeg from the official website (https://ffmpeg.org/) and add it to the environment variable path.

4. Set up your OpenAI API key by following the instructions in the `.env.example` file.

5. Run the application using the command `streamlit run app.py`.

6. Access the web application in your browser at `http://localhost:8501`.

## Technologies Used

- Python
- OpenAI Whisper
- OpenAI GPT-3
- Streamlit

## Limitations

Please note the following limitations of YoutubeGPT:

- The accuracy of speech recognition may vary depending on the quality of audio in the YouTube video.
- GPT-3 summarization is based on the extracted transcription and may not capture all nuances or context from the video.
- Due to OpenAI API limits, there may be restrictions on the number of API calls that can be made.

## License

YoutubeGPT is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

- This project utilizes OpenAI's Whisper and GPT-3 models. Special thanks to OpenAI for providing access to these powerful AI technologies.

- The web application is built using Streamlit, a fantastic framework for creating interactive data applications in Python.

