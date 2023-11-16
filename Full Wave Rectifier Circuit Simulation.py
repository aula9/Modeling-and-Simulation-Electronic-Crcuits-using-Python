import numpy as np
import matplotlib.pyplot as plt

def FR(input_signal, vk):
    output_signal = input_signal.copy()
    for i in range(len(output_signal)):
        if output_signal[i] > 2*vk:
            output_signal[i] =  output_signal[i]- 2*vk
        elif output_signal[i] < - 2*vk:
            output_signal[i] = - output_signal[i] - 2*vk
        else:
            output_signal[i] =0
    return output_signal


Rl= 5
vk = 0.7
t = np.linspace(0, 2*np.pi, 1000) 
v_in = 10*np.sin(t) 
v_out = FR(v_in,vk) 
Io= v_out/Rl

plt.plot(t, Io,'b', label='Current(A)')
plt.plot(t, v_in,'g', label='Input Voltage Signal (V)')
plt.plot(t, v_out,'r', label='Output Voltage Signal (V)')
plt.legend()
plt.xlabel('Time(s)')
plt.title('Full Wave Rectifier Circuit Simulation')
plt.show()
