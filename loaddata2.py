#rtl_sdr -f 101140000 -g 40 -n 20480000 ab120_10s.dat

from sys import argv
#This will allow a command line assignment of the filename
#script, filename = argv
import struct
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import scipy as sp

filename = "ab120_10s.dat"

rawdata = np.fromfile(filename,dtype=np.uint8)
real = rawdata[0::2]-127.5
imag = rawdata[1::2]-127.5
vals = real + 1.j * imag
T = 10 #seconds
fshift = -4.0e5 #-3.5e5
vals = vals * np.exp ( 1.j *2 * np.pi * np.linspace(0, fshift * T  ,vals.size)) # number of cycles
vals = sp.signal.decimate(vals,10)
f, t, Sxx = signal.spectrogram(vals, 2048000,nperseg=512)

#plt.pcolormesh(t[::100], np.fft.fftshift(f), np.fft.fftshift(Sxx[:,::100],axes=0))
#plt.pcolormesh(t[:1000], np.fft.fftshift(f), np.fft.fftshift(Sxx[:,:1000],axes=0))
#sig = np.argmax(Sxx, axis=0)

diff = vals[0:-1] * np.conj(vals[1:])
sig = np.arctan2(np.real(diff),np.imag(diff))
#plt.plot(sig[:30000])
#print sig.size
import pyaudio

p = pyaudio.PyAudio()

# open stream (2)
framerate = sig.size/10

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=framerate,
                output=True)
'''
for sample in sig:
    print sample
    stream.write(sample)
'''
stream.write(np.float32(sig/np.pi))
#plt.plot(sig[:300])
# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()


plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
#plt.show()
