import numpy as np
import matplotlib.pyplot as plt

def half_wave_rectifier(input_signal, threshold_voltage):
    output_signal = np.where(input_signal > threshold_voltage, input_signal - threshold_voltage, 0)
    return output_signal

t = np.linspace(0, 2*np.pi, 1000)  
v_in = 10* np.sin(t) 
V_threshold = 0.7
R=5
v_out = half_wave_rectifier(v_in, V_threshold)
I_out = v_out/R
#Plot of signals
plt.plot(t, I_out, label='Current Signal')
plt.plot(t, v_in, label='Input Voltage Signal')
plt.plot(t, v_out, label='Output Voltage Signal')
plt.xlabel('Time(s)')
plt.title('Half Wave Rectifier Circuit Simulation')
plt.legend()
plt.show()
