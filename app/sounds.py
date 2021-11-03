from config import *

class Sounds():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 
    RATE = 44100 # Частота дискретизации

    def __init__(self):
        self.tracks = os.listdir(f'{os.getcwd()}\\audio\\tracks')

        self.listen_Theard = Thread(target=self.theme)
        self.listen_Theard.start()
        

    def effect(self, effect):
        try:
            self.rec = pyaudio.PyAudio()
            wf = wave.open(f"{os.getcwd()}\\audio\\effects\\{effect}.wav", 'r')
            stream = self.rec.open( format=self.rec.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)
            data = wf.readframes(self.CHUNK)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(self.CHUNK)
            stream.stop_stream()
            stream.close()
            self.rec.terminate()
        except Exception as e:
            print(f'Audio effect isn`t working: {e}')

    

    def theme(self): 
        
        while True:
            for i in self.tracks:
                try:
                    self.rec = pyaudio.PyAudio()
                    wf = wave.open(f"{os.getcwd()}\\audio\\tracks\\{i}", 'r')
                    stream = self.rec.open( format=self.rec.get_format_from_width(wf.getsampwidth()),
                                            channels = wf.getnchannels(),
                                            rate = wf.getframerate(),
                                            output = True)

                    data = wf.readframes(self.CHUNK)
                    while len(data) > 0:
                        
                        if (main_thread().is_alive() is not True):
                            return 0

                        stream.write(data)
                        data = wf.readframes(self.CHUNK)
                    
                    
                    stream.stop_stream()
                    stream.close()
                    self.rec.terminate()
                except Exception as e:
                    print(f'Soundtracks aren`t playing: {e}')
            