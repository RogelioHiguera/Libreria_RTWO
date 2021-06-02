# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:25:11 2020
Parametros RLC de osciladores RTWO
Instituto Nacional de Astrofísica, Óptica y Electrónica (INAOE)
Tecnológico Nacional de México, campus Ixtapaluca (TECNM)
Academia de ingeniería electrónica
@author: M. en C. Rogelio Manuel Higuera Gonzalez
"""
import skrf as rf
import PSRLC as RLC
import matplotlib.pyplot as plt
import matplotlib as mpl
params = {'xtick.labelsize':14, 'ytick.labelsize':14}
mpl.rcParams.update(params)
GHz = 1e-9
pH = 1e12
fF = 1e15
Data1 = rf.Touchstone('A880umCVM2.s4p')
Data2 = rf.Touchstone('A880umCVM3.s4p')
Data3 = rf.Touchstone('A880umCVM4.s4p')
Data4 = rf.Touchstone('A880umCVM5.s4p')
Data1 = Data1.sparameters
Data2 = Data2.sparameters
Data3 = Data3.sparameters
Data4 = Data4.sparameters
l=880e-6
Freq1,Rdd1,Ldd1,Cdd1 = RLC.RLCdd(Data1,l)
Freq2,Rdd2,Ldd2,Cdd2 = RLC.RLCdd(Data2,l)
Freq3,Rdd3,Ldd3,Cdd3 = RLC.RLCdd(Data3,l)
Freq4,Rdd4,Ldd4,Cdd4 = RLC.RLCdd(Data4,l)
Freq1,Rcc1,Lcc1,Ccc1 = RLC.RLCcc(Data1,l)
Freq2,Rcc2,Lcc2,Ccc2 = RLC.RLCcc(Data2,l)
Freq3,Rcc3,Lcc3,Ccc3 = RLC.RLCcc(Data3,l)
Freq4,Rcc4,Lcc4,Ccc4 = RLC.RLCcc(Data4,l)
####################################################################################
fig,axes = plt.subplots(figsize=(11,5))
axes.plot(Freq1*GHz, Rdd1*l, label='Metal 2', linewidth=4)
axes.plot(Freq2*GHz, Rdd2*l, label='Metal 3', linewidth=4)
axes.plot(Freq3*GHz, Rdd3*l, label='Metal 4', linewidth=4)
axes.plot(Freq4*GHz, Rdd4*l, label='Metal 5', linewidth=4)
axes.set_xlabel('Frecuencia (GHz)', fontsize=22)
axes.set_ylabel('$R_{odd}$ ($\Omega$)', fontsize=22)
axes.tick_params(direction='out',length=2,width=1)
plt.legend(bbox_to_anchor=(1,0),loc='lower right',borderaxespad=0.1,fontsize=22)
plt.grid(True)
plt.savefig('Rdd.eps',dpi=1000)
###################################################################################
fig = plt.figure(figsize=(11, 6))
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.25, 0.58, 0.4, 0.3]) # inset axes
axes1.plot(Freq1*GHz, Ldd1*l*pH,  linewidth=4)
axes1.plot(Freq2*GHz, Ldd2*l*pH,  linewidth=4)
axes1.plot(Freq3*GHz, Ldd3*l*pH,  linewidth=4)
axes1.plot(Freq4*GHz, Ldd4*l*pH,  linewidth=4)
axes1.set_xlabel('Frecuencia (GHz)', fontsize=22)
axes1.set_ylabel('$L_{odd}$ ($pH$)', fontsize=22)
axes1.grid(True)
axes2.plot(Freq1*GHz, Ldd1*l*pH, label='Metal 2', linewidth=4)
axes2.plot(Freq2*GHz, Ldd2*l*pH, label='Metal 3', linewidth=4)
axes2.plot(Freq3*GHz, Ldd3*l*pH, label='Metal 4', linewidth=4)
axes2.plot(Freq4*GHz, Ldd4*l*pH, label='Metal 5', linewidth=4)
axes2.set_xlim([2,15])
axes2.set_ylim([245,275])
axes2.set_xlabel('Frecuencia (GHz)', fontsize=22)
axes2.set_ylabel('$L_{odd}$ ($pH$)', fontsize=22)
axes2.tick_params(direction='out',length=2,width=1)
plt.legend(bbox_to_anchor=(1.6,0),loc='lower right',borderaxespad=0.1,fontsize=22)
plt.grid(True)
plt.savefig('Ldd.eps',dpi=1000)
######################################################################################
fig2,axes3 = plt.subplots(figsize=(11,5))
axes3.plot(Freq1*GHz, Ccc1*l*fF, label='Metal 2', linewidth=4)
axes3.plot(Freq2*GHz, Ccc2*l*fF, label='Metal 3', linewidth=4)
axes3.plot(Freq3*GHz, Ccc3*l*fF, label='Metal 4', linewidth=4)
axes3.plot(Freq4*GHz, Ccc4*l*fF, label='Metal 5', linewidth=4)
axes3.set_xlabel('Frecuencia (GHz)', fontsize=22)
axes3.set_ylabel('$C_{even}$ ($fF$)', fontsize=22)
axes3.tick_params(direction='out',length=2,width=1)
plt.legend(bbox_to_anchor=(1,0.5),loc='lower right',borderaxespad=0.1,fontsize=22)
plt.grid(True)
plt.savefig('Ccc.eps',dpi=1000)
######################################################################################
Freq,C11,C12 = RLC.C11C12(Data3,l)
Freq,L11,Km = RLC.L11Km(Data3,l)
C11 = (C11*l)/8
C12 = (C12*l)/8
L11 = (L11*l)/8
R11 = (Rdd3*l)/8
Km = Km
print(C11[430],L11[430],R11[430],C12[430],Km[430])


 




