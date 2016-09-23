from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 314.5e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

samples = 2e6
data = sdr.read_samples(samples)
