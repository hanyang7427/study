import numpy as np
fv = np.fv(0.001, 5, -100, -1000)
print(round(fv, 2))
pv = np.pv(0.001, 5, -100, fv)
print(pv)
npv = np.npv(0.001, [-1000, -100, -100, -100, -100, -100])
print(round(npv, 2))
fv = np.fv(0.001, 5, 0, npv)
print(round(fv, 2))
irr = np.irr([-1000, 100, 200, 300, 400, 500])
print(irr)
npv = np.npv(irr, [-1000, 100, 200, 300, 400, 500])
print(npv)
nper = np.nper(0.001, -100, 1000)
print(nper)
pmt = np.pmt(0.001, 5, 1000)
print(pmt)
rate = np.rate(15, -100, 1000, 0)
print(rate)