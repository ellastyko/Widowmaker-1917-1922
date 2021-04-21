
# Code with write and read .wav files
 
class Audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5

    def __init__(self):
        self.message = pyaudio.PyAudio()

    def record(self):
        # p = pyaudio.PyAudio()
        # for i in range(p.get_device_count()):
        #     print(i, p.get_device_info_by_index(i)['name'])
        WAVE_OUTPUT_FILENAME = "output.wav"
        stream = self.message.open(format = self.FORMAT,
                        channels = self.CHANNELS,
                        rate = self.RATE,
                        input = True,
                        input_device_index = 1, 
                        frames_per_buffer = self.CHUNK)
        print("* recording")
        self.frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):  
            data = stream.read(self.CHUNK)
            self.frames.append(data)

        print("* done recording")
        stream.stop_stream()
        stream.close()
        self.message.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.message.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()


    def play(self):

        self.message = pyaudio.PyAudio()
        wf = wave.open("output.wav", 'rb')
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
