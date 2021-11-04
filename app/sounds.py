from threading import Thread, main_thread
import pyaudio, glob, os, wave 

class Sounds():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 
    RATE = 44100 # Частота дискретизации
    
    themes = glob.glob(f"{os.getcwd()}\\audio\\themes\\*.wav")
    effects = glob.glob(f"{os.getcwd()}\\audio\\effects\\*.wav")


    def __init__(self):

        self.pyaudio_effect = pyaudio.PyAudio()
        
        self.listen_Theard = Thread(target=self.play_theme)
        self.listen_Theard.start()
        

    def play_effect(self, effect):
        try:
            wf = wave.open(f"{os.getcwd()}\\audio\\effects\\{effect}.wav", 'r')
            stream = self.rec.open( format=self.pyaudio_effect.get_format_from_width(wf.getsampwidth()),
                                    channels=wf.getnchannels(),
                                    rate=wf.getframerate(),
                                    output=True)

            data = wf.readframes(self.CHUNK)

            while len(data) > 0:
                if (main_thread().is_alive() is not True):
                    return 0
                stream.write(data)
                data = wf.readframes(self.CHUNK)

            stream.stop_stream()
            stream.close()
            self.pyaudio_effect.terminate()
        except Exception as e:
            print(f'Audio effects doesn`t work: {e}')

    

    def play_theme(self): 
   
        while True:
            for theme in self.themes:
                try:
                    self.pyaudio_theme = pyaudio.PyAudio()
                    
                    wf = wave.open(theme, 'r')
                    stream = self.pyaudio_theme.open( 
                                                format=self.pyaudio_theme.get_format_from_width(wf.getsampwidth()),
                                                channels = wf.getnchannels(),
                                                rate = wf.getframerate(),
                                                output = True
                                            )

                    data = wf.readframes(self.CHUNK)
                    while len(data) > 0:
                        
                        if (main_thread().is_alive() is not True):
                            return 0

                        stream.write(data)
                        data = wf.readframes(self.CHUNK)
                    
                    
                    stream.stop_stream()
                    stream.close()
                    self.pyaudio_theme.terminate()
                except Exception as e:
                    print(f'Soundtracks aren`t playing: {e}')
            