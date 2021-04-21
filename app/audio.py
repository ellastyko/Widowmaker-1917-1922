from config import *
import pyaudio
import wave
import sys


tracks = ['hellobestie', 'farewell', 'k19',  'sadsong']

class Audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 
    RATE = 44100 # Частота дискретизации
    RECORD_SECONDS = 5 

    def __init__(self):
        pass

    def record(self):
        global KEYS
        self.message = pyaudio.PyAudio()
        stream = self.message.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        input_device_index = 1, 
                        frames_per_buffer = self.CHUNK)

        outstream = self.message.open(format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                output=True)

        print("* recording")

        while KEYS['F'] == True:
            data = stream.read(self.CHUNK)
            # Голосовое эхо
            outstream.write(data)
        
        print("* done recording")
        stream.stop_stream()
        stream.close()
        self.message.terminate()





    def play(self, effect):

        self.message = pyaudio.PyAudio()
        wf = wave.open(f"../assets/audio/tracks/{effect}.wav", 'rb')
        stream = self.message.open(format=self.message.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(self.CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)
        stream.stop_stream()
        stream.close()
        self.message.terminate()



    def theme(self):   
        for i in tracks:
            try:
                self.message = pyaudio.PyAudio()
                wf = wave.open(f"../assets/audio/tracks/{i}.wav", 'r')
                stream = self.message.open( format=self.message.get_format_from_width(wf.getsampwidth()),
                                            channels = wf.getnchannels(),
                                            rate = wf.getframerate(),
                                            output = True)
                data = wf.readframes(self.CHUNK)
                while len(data) > 0:
                    stream.write(data)
                    data = wf.readframes(self.CHUNK)
                stream.stop_stream()
                stream.close()
                self.message.terminate()
            except Exception:
                print(f'Soundtracks isn`t playing: {Exception}')
            
        



        

