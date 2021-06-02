# -*- coding: utf-8 -*-
'''
Proyecto: Caracterización de osciladores RTWO
Librería para obtener parametros RLC
Instituto Nacional de Astrofísica, Óptica y Electrónica (INAOE)
Tecnológico Nacional de México, campus Ixtapaluca (TECNM)
Academia de ingeniería electrónica
@author: M. en C. Rogelio Manuel Higuera Gonzalez
'''
import numpy as np
def complejo (SX,SY):
    n = len(SX)
    Sj = np.complex64(np.zeros((n)))
    for i in range (0,n):
        Sj[i] = complex(SX[i],0)+complex(0,SY[i])
    return Sj
def conversionj(Data):
    Freq = Data[:,0]
    S11M = Data[:,1];  S11A = Data[:,2] 
    S12M = Data[:,3];  S12A = Data[:,4]
    S13M = Data[:,5];  S13A = Data[:,6]
    S14M = Data[:,7];  S14A = Data[:,8]
    S21M = Data[:,9];  S21A = Data[:,10]
    S22M = Data[:,11]; S22A = Data[:,12]
    S23M = Data[:,13]; S23A = Data[:,14]
    S24M = Data[:,15]; S24A = Data[:,16]
    S31M = Data[:,17]; S31A = Data[:,18]
    S32M = Data[:,19]; S32A = Data[:,20]
    S33M = Data[:,21]; S33A = Data[:,22]
    S34M = Data[:,23]; S34A = Data[:,24]
    S41M = Data[:,25]; S41A = Data[:,26]
    S42M = Data[:,27]; S42A = Data[:,28]
    S43M = Data[:,29]; S43A = Data[:,30]
    S44M = Data[:,31]; S44A = Data[:,32]
    S11X = S11M*np.cos(np.radians(S11A)); S11Y = S11M*np.sin(np.radians(S11A))
    S12X = S12M*np.cos(np.radians(S12A)); S12Y = S12M*np.sin(np.radians(S12A))
    S13X = S13M*np.cos(np.radians(S13A)); S13Y = S13M*np.sin(np.radians(S13A))
    S14X = S14M*np.cos(np.radians(S14A)); S14Y = S14M*np.sin(np.radians(S14A))
    S21X = S21M*np.cos(np.radians(S21A)); S21Y = S21M*np.sin(np.radians(S21A))
    S22X = S22M*np.cos(np.radians(S22A)); S22Y = S22M*np.sin(np.radians(S22A))
    S23X = S23M*np.cos(np.radians(S23A)); S23Y = S23M*np.sin(np.radians(S23A))
    S24X = S24M*np.cos(np.radians(S24A)); S24Y = S24M*np.sin(np.radians(S24A))
    S31X = S31M*np.cos(np.radians(S31A)); S31Y = S31M*np.sin(np.radians(S31A))
    S32X = S32M*np.cos(np.radians(S32A)); S32Y = S32M*np.sin(np.radians(S32A))
    S33X = S33M*np.cos(np.radians(S33A)); S33Y = S33M*np.sin(np.radians(S33A))
    S34X = S34M*np.cos(np.radians(S34A)); S34Y = S34M*np.sin(np.radians(S34A))
    S41X = S41M*np.cos(np.radians(S41A)); S41Y = S41M*np.sin(np.radians(S41A))
    S42X = S42M*np.cos(np.radians(S42A)); S42Y = S42M*np.sin(np.radians(S42A))
    S43X = S43M*np.cos(np.radians(S43A)); S43Y = S43M*np.sin(np.radians(S43A))
    S44X = S44M*np.cos(np.radians(S44A)); S44Y = S44M*np.sin(np.radians(S44A))
    S11j = complejo(S11X,S11Y); S12j = complejo(S12X,S12Y)
    S13j = complejo(S13X,S13Y); S14j = complejo(S14X,S14Y)
    S21j = complejo(S21X,S21Y); S22j = complejo(S22X,S22Y)
    S23j = complejo(S23X,S23Y); S24j = complejo(S24X,S24Y)
    S31j = complejo(S31X,S31Y); S32j = complejo(S32X,S32Y)
    S33j = complejo(S33X,S33Y); S34j = complejo(S34X,S34Y)
    S41j = complejo(S41X,S41Y); S42j = complejo(S42X,S42Y)
    S43j = complejo(S43X,S43Y); S44j = complejo(S44X,S44Y)
    Data1 = (np.array([Freq,S11j,S12j,S13j,S14j,S21j,S22j,S23j,S24j,S31j,S32j,S33j,S34j,S41j,S42j,S43j,S44j])).T
    return Data1 
def Sdd (Data):
    PS = conversionj(Data)
    Freq = PS[:,0].real
    S11 = PS[:,1];  S12 = PS[:,2];  S13 = PS[:,3];  S14 = PS[:,4]
    S21 = PS[:,5];  S22 = PS[:,6];  S23 = PS[:,7];  S24 = PS[:,8]
    S31 = PS[:,9];  S32 = PS[:,10]; S33 = PS[:,11]; S34 = PS[:,12]
    S41 = PS[:,13]; S42 = PS[:,14]; S43 = PS[:,15]; S44 = PS[:,16]
    S11dd = (S11-S13-S31+S33)/2
    S21dd = (S21-S23-S41+S43)/2
    S22dd = (S22-S24-S42+S44)/2
    S12dd = (S12-S32-S14+S34)/2
    return Freq,S11dd,S12dd,S21dd,S22dd
def Scc (Data):
    PS = conversionj(Data)
    Freq = PS[:,0].real
    S11 = PS[:,1];  S12 = PS[:,2];  S13 = PS[:,3];  S14 = PS[:,4]
    S21 = PS[:,5];  S22 = PS[:,6];  S23 = PS[:,7];  S24 = PS[:,8]
    S31 = PS[:,9];  S32 = PS[:,10]; S33 = PS[:,11]; S34 = PS[:,12]
    S41 = PS[:,13]; S42 = PS[:,14]; S43 = PS[:,15]; S44 = PS[:,16]
    S11cc = (S11+S13+S31+S33)/2
    S21cc = (S21+S23+S41+S43)/2
    S22cc = (S22+S24+S42+S44)/2
    S12cc = (S12+S32+S14+S34)/2
    return Freq,S11cc,S12cc,S21cc,S22cc
def ABCDdd (Data):
    Z0 = 50
    Freq,S11dd,S12dd,S21dd,S22dd = Sdd(Data)
    DS = S11dd*S22dd-S21dd*S12dd
    Add = (1+S11dd-S22dd-DS)/(2*S21dd)
    Bdd = ((1+S11dd+S22dd+DS)*Z0)/(2*S21dd)
    Cdd = (1-S11dd-S22dd+DS)/(2*S21dd*Z0)
    Ddd = (1-S11dd+S22dd-DS)/(2*S21dd)
    return Freq,Add,Bdd,Cdd,Ddd
def ABCDcc (Data):
    Z0 = 50
    Freq,S11cc,S12cc,S21cc,S22cc = Scc(Data)
    DS = S11cc*S22cc-S21cc*S12cc
    Acc = (1+S11cc-S22cc-DS)/(2*S21cc)
    Bcc = ((1+S11cc+S22cc+DS)*Z0)/(2*S21cc)
    Ccc = (1-S11cc-S22cc+DS)/(2*S21cc*Z0)
    Dcc = (1-S11cc+S22cc-DS)/(2*S21cc)
    return Freq,Acc,Bcc,Ccc,Dcc
def Zcc (Data):
    Freq,Acc,Bcc,Ccc,Dcc = ABCDcc(Data)
    Zccc = np.sqrt(Bcc/Ccc)
    return Freq,Zccc
def Zdd (Data):
    Freq,Add,Bdd,Cdd,Ddd = ABCDdd(Data)
    Zcdd = np.sqrt(Bdd/Cdd)
    return Freq,Zcdd
def gammac (Data,l):
    Freq,Acc,Bcc,Ccc,Dcc = ABCDcc(Data)
    gammacc = np.arccosh(Acc)/l
    return Freq,gammacc
def gammad (Data,l):
    Freq,Add,Bdd,Cdd,Ddd = ABCDdd(Data)
    gammadd = np.arccosh(Add)/l
    return Freq,gammadd
def RLCcc (Data,l):
    Freq,gammacc = gammac(Data,l)
    Freq,Zccc    = Zcc(Data)
    Rcc = (gammacc*Zccc).real
    Lcc = ((gammacc*Zccc).imag)/(2*np.pi*Freq)
    Ccc = ((gammacc/Zccc).imag)/(2*np.pi*Freq)
    return Freq,Rcc,Lcc,Ccc
def RLCdd (Data,l):
    Freq,gammadd = gammad(Data,l)
    Freq,Zcdd    = Zdd(Data)
    Rdd = (gammadd*Zcdd).real
    Ldd = ((gammadd*Zcdd).imag)/(2*np.pi*Freq)
    Cdd = ((gammadd/Zcdd).imag)/(2*np.pi*Freq)
    return Freq,Rdd,Ldd,Cdd
def C11C12 (Data,l):
    Freq,Rcc,Lcc,Ccc = RLCcc(Data,l)
    Freq,Rdd,Ldd,Cdd = RLCdd(Data,l)
    C11 = Ccc
    C12 = (Cdd-Ccc)/2
    return Freq,C11,C12
def L11Km (Data,l):
    Freq,Rcc,Lcc,Ccc = RLCcc(Data,l)
    Freq,Rdd,Ldd,Cdd = RLCdd(Data,l)
    L12 = (Lcc-Ldd)/2
    L11 = Ldd+L12
    L22 = L11
    Km = L12/(np.sqrt(L11*L22))
    return Freq,L11,Km




