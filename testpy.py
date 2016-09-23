from rtlsdr import RtlSdr
import matplotlib.pyplot as plt
import numpy as np

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 102.5e6     # Hz 101.3 had osmething interesteing
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

#print(sdr.read_samples(512))
for i in range(20):
    sample = np.fft.fft(sdr.read_samples(2048*4))
    #plt.plot( sample[1024*32:1024*32+256])
    print(np.argmax(np.abs(sample)))
    #print(np.max(sample))


plt.plot(np.abs(sample))
#plt.plot(np.fft.fftshift(np.abs(sample)))
plt.show()
