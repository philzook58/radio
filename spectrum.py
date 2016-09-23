from rtlsdr import RtlSdr
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq, fftshift

sdr = RtlSdr()

samprate = 2.048e6
# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
#sdr.gain = 'auto'
sdr.gain = 10


sampsize=2048
steps = 10


samples = np.empty((steps,sampsize), 'complex')
power = np.zeros((steps,sampsize))
freqstart = 100e6
freqstop = 120e6

#freqstep = (freqstop-freqstart) / steps
#cfreqs = np.linspace(freqstop, freqstart, steps)
cfreqs = np.arange(freqstart,freqstop, 2.048e6)
for a in range(10):
    for i in range(steps):
        sdr.center_freq = cfreqs[i]
        samples[i,:] = sdr.read_samples(sampsize)

    samplesfft = fft(samples,axis=1)
    samplesfft[:,0:2]=samplesfft[:,3:5]
    samplesfft[:,-3:-1]=samplesfft[:,-7:-5]
    power = power + np.abs(samplesfft)**2


power = fftshift(power,axes=(1,))
db = np.ravel(np.log(power))
freq = np.linspace(freqstart-samprate/2,freqstop+samprate/2,db.size )
#freq = fftfreq(n, d=timestep)

plt.figure()
#plt.psd(samples[0,:], NFFT=sampsize, Fc=sdr.fc/1e6, Fs=sdr.rs/1e6)
#plt.plot(np.log(np.abs(samplesfft[0,:])))
plt.plot(freq,db)
plt.show()
