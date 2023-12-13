import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

V_t = 1.6

data = pd.read_csv('V0vsGate.csv')

x = []
y = []
for i in range(len(data)-1):
    if float(data['CH1'][i+1]) > V_t:
        x.append(float(data['CH1'][i+1]))
        y.append(float(data['CH2'][i+1]))

def objective(x, k):
    return 100*(k/2)*(x-V_t)**2

k, _ = curve_fit(objective, x, y)
k = k[0]

x = np.array(x)
plt.scatter(x,y)

x_line = np.linspace(min(x), max(x), 1000)
y_line = objective(x_line,k)

legend = f'k = {k}'
plt.plot(x_line, y_line, color='r', label=legend)

plt.xlabel('Gate Voltage (V)')
plt.ylabel('Drive Current * 100 Ohms (V)')

plt.legend()


plt.show()