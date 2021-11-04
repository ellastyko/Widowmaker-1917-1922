from config import *


class Audio():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 
    RATE = 44100 # Частота дискретизации

    def __init__(self, client=None, status=None):
        
        if status == 0:
            self.theme()
        elif status == 1:
            self.client = client

        # Record and listen
        self.rec = pyaudio.PyAudio()
        self.instream = self.rec.open(  format = self.FORMAT,
                                        channels = self.CHANNELS,
                                        rate = self.RATE,
                                        input = True,
                                        input_device_index = 1, 
                                        frames_per_buffer = self.CHUNK)
                                        
        self.outstream = self.rec.open( format=self.FORMAT,
                                        channels=self.CHANNELS,
                                        rate=self.RATE,
                                        output=True)
        


    def __del__(self):
        self.instream.stop_stream()
        self.instream.close()
        self.outstream.stop_stream()
        self.outstream.close()
        
        self.rec.terminate()     


    def record(self):

        global KEYS
        
        print("* recording")
        while KEYS['F'] == True:
            data = self.instream.read(self.CHUNK) 
            # print(type(data))
            self.client.send(data)

        print("* done recording")
        

    def hear(self, data):
        self.outstream.write(data) # data['voice']

        



        

