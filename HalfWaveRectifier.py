import numpy as np
import matplotlib.pyplot as plt

def half_wave_rectifier(input_signal,Vk):
    output_signal = input_signal.copy() -Vk
    for i in range(len(output_signal)):
        if output_signal[i] < 0:
            output_signal[i] = 0
    return output_signal

t = np.linspace(0, 2*np.pi, 1000)  
v_in = 10*np.sin(t)  
Vk=0.7
R=5
v_out = half_wave_rectifier(v_in,Vk)  
I_out = v_out/R

plt.plot(t, v_in, label='Input Signal')
plt.plot(t, v_out, label='Output Signal')
plt.plot(t, I_out, label='Current Signal')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Half Wave Rectifier Circuit Simulation')
plt.legend()
plt.show()
