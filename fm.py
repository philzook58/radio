

import pyaudio
import wave
import time
import sys
import struct

from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import numpy as np

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 102.5e6     # Hz 101.3 had osmething interesteing
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'


p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    sample = np.fft.fft(sdr.read_samples(2048*4))
    #plt.plot( sample[1024*32:1024*32+256])
    val = struct.pack( 'h'  , np.argmax(np.abs(sample)) - 4150)
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
