import os
import pyaudio 
import wave
from engine import TTSEngine

class TTSInterface:
    def __init__(self, input_text):
        self.input_text = input_text 
    def talk(self):
        chunk = 1024
        engine = TTSEngine("sounds/sounds.csv")
        engine.make_sounds(self.input_text)

        wave_file = wave.open("temp.wav", "rb")
        player = pyaudio.PyAudio()

        stream = player.open(
            format = player.get_format_from_width(wave_file.getsampwidth()),
            channels = wave_file.getnchannels(), 
            rate = wave_file.getframerate(),
            output = True
        )

        data = wave_file.readframes(chunk) 

        while data != b'':
            stream.write(data)
            data = wave_file.readframes(chunk)
        
        stream.close()
        player.terminate()

        os.remove("temp.wav")

if __name__ == '__main__':
    while True:
        text = input("Enter something: ")
        talk = TTSInterface(text)
        talk.talk()
