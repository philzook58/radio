

import pyaudio
import wave
import time
import sys
import struct

from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import numpy as np




p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    sample = np.fft.fft(sdr.read_samples(2048*4))
    #plt.plot( sample[1024*32:1024*32+256])
    val = struct.pack( 'h'  , np.sin(frame_count))
    print val
    return (val,pyaudio.paContinue)


stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=22000,
                output=True,
                stream_callback=callback)

stream.start_stream()


time.sleep(5)

stream.stop_stream()
stream.close()
#wf.close()

p.terminate()
