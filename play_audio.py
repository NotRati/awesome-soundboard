import pyaudio
import wave
from pydub import AudioSegment
import os
def play_audio(file_path):
    # Open the audio file
    sound = AudioSegment.from_mp3(file_path)
    sound.export("ias.wav", format="wav")

    wf = wave.open("ias.wav", 'rb')

    # Create a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream with the appropriate settings
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=wf.getframerate(),
                     output=True)

    # Read data in chunks and play
    chunk_size = 1024
    data = wf.readframes(chunk_size)

    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Clean up
    os.remove(file_path)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
    os.remove("ias.wav")

