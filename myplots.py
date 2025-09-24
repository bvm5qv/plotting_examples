import random
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(57837594)

def CalcErrorBars(ax, dist, Bins):
  yb, xb, _ = ax.hist(dist, bins = Bins)
  err = np.sqrt(yb)
  bc = (xb[1:]-xb[:-1])/2+xb[:-1]
  ax.errorbar(bc, yb, yerr = err, fmt = ".", color = 'b')
  print(f"mean = {np.mean(dist)}")
  print(f"stddev = {np.std(dist)}")

def RandDistFromFcn(fcn, domain, nSamples, fcnMax):
  samples = []
  while len(samples) < nSamples:
    x = np.random.uniform(domain[0],domain[1])
    y = np.random.uniform(0, fcnMax)
    if y < fcn(x):
      samples.append(x)
  return np.array(samples)

nPts = 10000
nBins = 100

#First Graph
dist1 = rng.standard_normal(nPts)*6 + 100
plt.title("Random Gauss")
plt.xlabel('x')
plt.ylabel("frequency")
plt.xlim(50,150)
bins1 = plt.hist(dist1, bins = nBins)
yb = bins1[0]
xb = bins1[1]
err = np.sqrt(yb)
bc = (xb[1:]-xb[:-1])/2+xb[:-1]
plt.errorbar(bc, yb, yerr = err, fmt = ".", color = 'b')
print(f"mean = {np.mean(dist1)}")
print(f"stddev = {np.std(dist1)}")

#Multiplot Graph
fig, axs = plt.subplots(2,2)
for ax in axs.flat:
  ax.set(xlabel = 'x', ylabel = "frequency")
  ax.set_xlim(50,150)

#First
axs[0,0].set_title("Random Gauss")
CalcErrorBars(axs[0,0], dist1, nBins)

#Second
axs[0,1].set_title("Gauss Offset")
dist2 = dist1
for i in range((int)(nPts/3)):
  dist2 = np.append(dist2, random.uniform(50,150))
CalcErrorBars(axs[0,1], dist2, nBins)

#Third
axs[1,0].set_title("Gauss Offset2")
dist3 = dist1
base2 = RandDistFromFcn(lambda x: 1/x**2, [1,11], nPts, 1)
for i in range(nPts*30):
  x = np.random.choice(base2)*10 + 40
  dist3 = np.append(dist3, x)
CalcErrorBars(axs[1,0], dist3, nBins)

#Fourth
axs[1,1].set_title("Double Gaussian")
dist4 = dist1
secondGauss = rng.standard_normal(nPts)*20 + 1
for i in range((int)(nPts/2)):
  x = np.random.choice(secondGauss)
  dist4 = np.append(dist4, x)
CalcErrorBars(axs[1,1], dist4, nBins)


plt.show()


















