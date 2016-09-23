import numpy as np
filename = 'capture.bin'
rawdata = np.fromfile(filename,dtype=np.uint8)
floatdata = rawdata.astype(float)
floatdata.tofile('floatcap.bin')
