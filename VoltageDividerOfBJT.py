def VoltageDividerBJT(vcc,R1,R2,RE,RC,B,VBE,VCEsat):
    Rth=R1*R2/(R1+R2)
    vth=vcc*R2/(R1+R2)
    IB=(vth-VBE)/(Rth+(1+B)*RE)
    ICsat= (vcc-VCEsat) /(RC+RE)
    IC=B*IB
    if ((IC < ICsat) and (IC > 0)):
        IC=B*IB; VCE=vcc-IC*(RE+RC)
        print('The transistor is in the Active mode')
    elif( IC>=ICsat):
        IC=ICsat; VCE=VCEsat
        print('The transistor is in the Saturation mode')
    else:
        IB=0;IC=0; VCE=vcc
        print('The transistor is in the cut-off mode')
    Pc=IC*VCE
    return (IB,IC,VCE,Pc)
#Example
vcc = 20  #v
RB1 = 100  # Kohm
RB2 = 10  # Kohm
RC = 3   # Kohm
RE = 1   # Kohm
B = 100
VBE = 0.7  #v
VCEsat=0 #v

IB,IC,VCE,Pc = VoltageDividerBJT(vcc,RB1,RB2,RE,RC,B,VBE,VCEsat)
print('IB=',IB)
print('IC=',IC)
print('VCE=',VCE)
print('Pc=',Pc)
