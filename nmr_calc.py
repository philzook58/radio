gamma = 20e6
B0 = 0.5
D = 0.07
I = 0.01
hbar = 1.05e-34
rho = 33e27 * 2
N1 = 10
N2 = 100
A = 0.01**2
T = 300
kb = 1.38e-23
T2 = 1.
mu0 = 4 * 3.14 * 10e-7
B1 = mu0 * I * N1 / D
w0 = gamma * B0
w1 = B1 * gamma
Mz = hbar * gamma * B0 * gamma * hbar * rho / kb / T
My = w1 * T2 * Mz
V = mu0 * w0 * My * A * N2
print V
# 0.015 V is calculated
#7 dBm  at no gain reception of rtl.
#Has 50dbm of gain
#0.01V is -27dbm
