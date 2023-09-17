"""
Transcribes wav files to text.

Adapted from https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
"""

# importing libraries 
import speech_recognition as sr 
import os 
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence

# set language
lang = "zh-sg"

# create a speech recognition object
r = sr.Recognizer()

# a function to recognize speech in the audio file
# so that we don't repeat ourselves in in other functions
def transcribe_audio(path:str):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened, language=lang)
    return text

def transcribe_audio_safe(path:str):

    try:
        text = transcribe_audio(path)
    except sr.UnknownValueError as e:
        print("Error:", str(e))
    else:
        print(path, ":", text)

    return text

# a function that splits the audio file into chunks on silence
def save_chunks_on_silence(path:str):
    """Splitting the large audio file into wav chunks"""
    path = Path(path).resolve()
    folder_name = path.parent / path.stem / "audio-chunks"
    # create a directory to store the audio chunks
    if not folder_name.is_dir():
        folder_name.mkdir(parents=True)

    chunk_names = []
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)  
    # split audio sound where silence is 500 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    print("split ok")
    
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        chunk_names.append(chunk_filename)
    return chunk_names

