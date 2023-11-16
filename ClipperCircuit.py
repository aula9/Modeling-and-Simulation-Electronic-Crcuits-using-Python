import numpy as np
import matplotlib.pyplot as plt

def diode_clipper(input_signal, V_clip, Vk):
    output_signal = input_signal.copy()
    for i in range(len(output_signal)):
        if output_signal[i] > V_clip+Vk:
            output_signal[i] = V_clip+Vk
        elif output_signal[i] < -V_clip -Vk:
            output_signal[i] = -V_clip -Vk
    return output_signal

t = np.linspace(0, 2*np.pi, 1000)  
v_in = 10*np.sin(t)  
v_out = diode_clipper(v_in, 3,0.7) 

plt.plot(t, v_in, label='Input Signal')
plt.plot(t, v_out, label='Output Signal')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Diode Clipper Circuit Simulation')
plt.legend()
plt.show()
