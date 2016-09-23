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
#filename = "testfile.txt"
'''
f = open(filename, 'r')

byte = f.read(1)
while byte:
    # Do stuff with byt.
    real = struct.unpack('B',byte)
    byte = f.read(1)
    imag = struct.unpack('B',byte)
    byte = f.read(1)
'''
rawdata = np.fromfile(filename,dtype=np.uint8)
real = rawdata[0::2]-127.5
imag = rawdata[1::2]-127.5
vals = real + 1.j * imag
print vals.size
print vals[:200]

f, t, Sxx = signal.spectrogram(vals, 2048000,nperseg=512)
#f, t, Sxx = signal.spectrogram(real, 2048000,nperseg=512)
#
#f, t, Sxx = signal.spectrogram(imag[0:512*60], 2048000,nperseg=512)
#plt.pcolormesh(t, f, Sxx,vmin=0.,vmax=.01)

print f.size
print t.size
print Sxx.shape
#print f
#print Sxx[0,1000]
plt.pcolormesh(t[::100], np.fft.fftshift(f), np.fft.fftshift(Sxx[:,::100],axes=0))
#plt.pcolormesh(t[10:30], f, Sxx[:,10:30],vmin=0.,vmax=.1)
"""
spect = np.zeros((10,512))
for i in range(10):
    spect[i,:] = np.abs(np.fft.fftshift(np.fft.fft(vals[i*512:(i+1)*512])))
    #np.fft.fftfreq()
plt.pcolormesh(np.arange(512),np.arange(10), spect)
"""

'''
#custom spectrogram
windowsize = 512
blockedvals = np.reshape(vals, (vals.size/windowsize,windowsize))
spectrum =  np.fft.fftshift(np.abs(np.fft.fft(blockedvals)))
print spectrum.shape
times = np.linspace(0,10,vals.size/windowsize)
freqs =np.fft.fftshift(np.fft.fftfreq(windowsize,1./2048000))
#plt.plot(spectrum[0,:])
plt.pcolormesh(freqs, times[::100], np.log(spectrum[::100,:]))
'''
#plt.plot(Sxx[:,3000])
#plt.colorbar()
#plt.plot(Sxx[400,:])
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
#plt.savefig("power.png")
"""
#freq = np.fft.freq(2048)
spect = np.fft.fftshift(np.fft.fft(vals[0:2048]))
plt.plot(spect)
plt.show()
"""
