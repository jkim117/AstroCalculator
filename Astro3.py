#Astro Calculator 3.0
#Jason Kim

from __future__ import division
from math import*
import numpy as np
from copy import copy, deepcopy

#allObjs is a list with three dimensions, each for either object 1, 2, or both. Within each, there are 7 dimensions for types of units, within each of those are a various number of spots for different types of values.
lengthNames1 = ["Distance to Star 1", "Stellar Radius 1", "Maximum Wavelength 1", "Semi-Major Axis 1", "Distance to Center of Mass 1", "Wavelength of Still Source 1", "Observed Shifted Wavelength 1"]
angleNames1 = ["Parallax Angle 1", "Angular Size of Object 1", "Inclination 1"]
timeNames1= ["Period of Orbit 1"]
massNames1= ["Mass 1"]
velocityNames1= ["Escape Velocity 1", "Radial Velocity 1", "Orbital Velocity 1"]
luminNames1= ["Luminosity 1"]
miscNames1 = ["Brightness 1", "Apparent Magnitude 1", "Absolute Magnitude 1", "Surface Temperature 1", "Force of Gravity on Object 1", "Gravitational Acceleartion 1", "Kinetic Energy 1", "Potential Energy 1", "Angular Momentum 1", "Flux 1"]

bothNames = ["Total Mass of System", "Distance Between Objects", "Period of Orbit", "Force of Gravity between Objects", "Potential Energy of System"]

lengthNames2 = ["Distance to Star 2", "Stellar Radius 2", "Maximum Wavelength 2", "Semi-Major Axis 2", "Distance to Center of Mass 2", "Wavelength of Still Source 2", "Observed Shifted Wavelength 2"]
angleNames2 = ["Parallax Angle 2", "Angular Size of Object 2", "Inclination 1"]
timeNames2= ["Period of Orbit 2"]
massNames2= ["Mass 2"]
velocityNames2= ["Escape Velocity 2", "Radial Velocity 2", "Orbital Velocity 2"]
luminNames2= ["Luminosity 2"]
miscNames2 = ["Brightness 2", "Apparent Magnitude 2", "Absolute Magnitude 2", "Surface Temperature 2", "Force of Gravity on Object 2", "Gravitational Acceleartion 2", "Kinetic Energy 2", "Potential Energy 2", "Angular Momentum 2", "Flux 2"]

obj1Names= [lengthNames1, angleNames1, timeNames1, massNames1, velocityNames1, luminNames1, miscNames1]
obj2Names= [lengthNames2, angleNames2, timeNames2, massNames2, velocityNames2, luminNames2, miscNames2]
allObjsNames= [obj1Names, obj2Names, bothNames]

lengthUnits= ["m", "au", "ly", "pc", "a", "nm", "rs"]
angleUnits= ["deg", "as", "rad"]
timeUnits= ["s", "min", "hr", "day", "yr"]
massUnits= ["kg", "sm"]
velUnits= ["m/s", "km/s"]
luminUnits= ["w", "sl"]
miscUnits= ["w/m2", "magnitudes", "magnitudes", "K", "N", "m/s2", "J", "J", "kg*m^2/s", "w/m2"]
unitsArray=[lengthUnits, angleUnits, timeUnits, massUnits, velUnits, luminUnits, miscUnits]

lengths1= ["j"]*7
angles1= ["j", "j", "j"]
times1= ["j"]
mass1= ["j"]
vel1= ["j"]*3
luminNames1= ["j"]
misc1= ["j"]*10

both= ["j", "j", "j", "j", "j"]

lengths2= ["j"]*7
angles2= ["j", "j", "j"]
times2= ["j"]
mass2= ["j"]
vel2= ["j"]*3
luminNames2= ["j"]
misc2= ["j"]*10

obj1= [lengths1, angles1, times1, mass1, vel1, luminNames1, misc1]
obj2= [lengths2, angles2, times2, mass2, vel2, luminNames2, misc2]
#For allObjs:
#first dimensinon refers to obj1, obj2, both.
#second dimension for obj1 and obj2 refer to length, angles, etc
#second dimension for both refers to either total mass or distance between
#third dimension for obj1 and obj2 refer to distance to star, mass, escape velocity, etc
allObjs= [obj1, obj2, both]


#Each conversion function takes in a number and a unit in the form of a string. Outputs a list with the same value in different units.
def lengthConvert(l, unit):
    if unit=="m":
        return [l, 6.6846e-12*l, 1.057e-16*l, 3.24078e-17*l, 1e+10*l, 1e+9*l, 1.43740118e-9*l]
    if unit=="au":
        return [1.496e+11*l, l, 1.58125e-5*l, 4.84814e-6*l, 1.496e+21*l, 1.496e+20*l, 214.939469384*l]
    if unit=="ly":
        return [9.461e+15*l, 63241.1*l, l, 0.306601*l, 9.461e+25*l, 9.461e+24*l, 13598874.0132*l]
    if unit=="pc":
        return [3.086e+16*l, 206265*l, 3.26156*l, l, 3.086e+26*l, 3.086e+25*l, 44353568.9099*l]
    if unit=="a":
        return [1e-10*l, 6.68459e-22*l, 1.057e-26*l, 3.24078e-27*l, l, 0.1*l, 1.43740118e-19*l]
    if unit=="nm":
        return [1e-9*l, 6.68459e-21*l, 1.057e-25*l, 3.24078e-26*l, 10*l, l, 1.43740118e-18*l]
    if unit=="rs":
        return [6.957e8*l, 0.00465047*l, 7.35355e-8*l, 2.25461e-8*l, 6.957e18*l, 6.957e17*l, l]

def angleConvert(a, unit):
    if unit=="deg":
        return [a, 3600*a, 0.0174533*a]
    if unit=="as":
        return [a/3600, a, 4.84814e-6*a]
    if unit=="rad":
        return [57.2958*a, 206265*a, a]
    
def timeConvert(t, unit):
    if unit=="s":
        return [t, t/60, t/3600, t/86400, t/31536000]
    if unit=="min":
        return [t*60, t, t/60, t/1440, t/525600]
    if unit=="hr":
        return [t*3600, t*60, t, t/24, t/8760]
    if unit=="day":
        return [t*86400, t*1440, t*24, t, t/365]
    if unit=="yr":
        return [31536000*t, 525600*t, 8760*t, 365*t, t]

def massConvert(m, unit):
    if unit=="kg":
        return [m, m/1.989e30]
    if unit=="sm":
        return [m*(1.989e30), m]

def velConvert(v, unit):
    if unit=="m/s":
        return [v, v/1000]
    if unit=="km/s":
        return [1000*v, v]

def luminConvert(l, unit):
    if unit=="w":
        return [l, l/(3.828e26)]
    if unit=="sl":
        return [3.828e26*l, l]

#Formulas begin here
#Every Formula takes in the allObjs array as the argument and spits out the allObjs array as the return but with updated values
def Aa1(arr):
    if arr[0][1][0]=="j"or not arr[0][0][0]=="j":
        return arr, ""
    p=arr[0][1][0][1]
    d=lengthConvert(1/p, "pc")
    arr[0][0][0]=d
    return arr, "d=1/p"

def Ab1(arr):
    if arr[0][0][0]=="j"or not arr[0][1][0]=="j":
        return arr, ""
    d=arr[0][0][0][3]
    p=angleConvert(1/d, "as")
    arr[0][1][0]=p
    return arr, "d=1/p"

def Aa2(arr):
    if arr[1][1][0]=="j"or not arr[1][0][0]=="j":
        return arr, ""
    p=arr[1][1][0][1]
    d=lengthConvert(1/p, "pc")
    arr[1][0][0]=d
    return arr, "d=1/p"

def Ab2(arr):
    if arr[1][0][0]=="j"or not arr[1][1][0]=="j":
        return arr, ""
    d=arr[1][0][0][3]
    p=angleConvert(1/d, "as")
    arr[1][1][0]=p
    return arr, "d=1/p"

def Ba1(arr):
    if arr[0][0][0]=="j" or arr[0][6][0]=="j"or not arr[0][5][0]=="j":
        return arr, ""
    d=arr[0][0][0][0]
    b=arr[0][6][0][0]
    l=luminConvert(4*pi*(d**2)*b, "w")
    arr[0][5][0]=l
    return arr, "L=4pi(d^2)b"

def Bb1(arr):
    if arr[0][6][0]=="j" or arr[0][5][0]=="j"or not arr[0][0][0]=="j":
        return arr, ""
    b=arr[0][6][0][0]
    l=arr[0][5][0][0]
    d=lengthConvert(sqrt(l/(4*pi*b)),"m")
    arr[0][0][0]=d
    return arr, "L=4pi(d^2)b"

def Bc1(arr):
    if arr[0][0][0]=="j" or arr[0][5][0]=="j"or not arr[0][6][0]=="j":
        return arr, ""
    d=arr[0][0][0][0]
    l=arr[0][5][0][0]
    b=[l/(4*pi*(d**2))]
    arr[0][6][0]=b
    return arr, "L=4pi(d^2)b"

def Ba2(arr):
    if arr[1][0][0]=="j" or arr[1][6][0]=="j"or not arr[1][5][0]=="j":
        return arr, ""
    d=arr[1][0][0][0]
    b=arr[1][6][0][0]
    l=luminConvert(4*pi*(d**2)*b, "w")
    arr[1][5][0]=l
    return arr, "L=4pi(d^2)b"

def Bb2(arr):
    if arr[1][6][0]=="j" or arr[1][5][0]=="j"or not arr[1][0][0]=="j":
        return arr, ""
    b=arr[1][6][0][0]
    l=arr[1][5][0][0]
    d=lengthConvert(sqrt(l/(4*pi*b)),"m")
    arr[1][0][0]=d
    return arr, "L=4pi(d^2)b"

def Bc2(arr):
    if arr[1][0][0]=="j" or arr[1][5][0]=="j"or not arr[1][6][0]=="j":
        return arr, ""
    d=arr[1][0][0][0]
    l=arr[1][5][0][0]
    b=[l/(4*pi*(d**2))]
    arr[1][6][0]=b
    return arr, "L=4pi(d^2)b"

def Ca3(arr):
    if arr[0][6][1]=="j" or arr[1][6][1]=="j" or arr[0][6][0]=="j"or not arr[1][6][0]=="j":
        return arr,""
    m1=arr[0][6][1][0]
    m2=arr[1][6][1][0]
    b1=arr[0][6][0][0]
    b2=[(10**((m2-m1)/-2.5))*b1]
    arr[1][6][0]=b2
    return arr, "m2-m1=-2.5log(b2/b1)"

def Cb3(arr):
    if arr[0][6][1]=="j" or arr[1][6][1]=="j" or arr[1][6][0]=="j"or not arr[0][6][0]=="j":
        return arr,""
    m1=arr[0][6][1][0]
    m2=arr[1][6][1][0]
    b2=arr[1][6][0][0]
    b1=[b2/(10**((m2-m1)/-2.5))]
    arr[0][6][0]=b1
    return arr, "m2-m1=-2.5log(b2/b1)"

def Cc3(arr):
    if arr[1][6][1]=="j" or arr[0][6][0]=="j" or arr[1][6][0]=="j"or not arr[0][6][1]=="j":
        return arr,""
    m2=arr[1][6][1][0]
    b1=arr[0][6][0][0]
    b2=arr[1][6][0][0]
    m1=[-(-2.5*log(b2/b1,10)-m2)]
    arr[0][6][1]=m1
    return arr, "m2-m1=-2.5log(b2/b1)"

def Cd3(arr):
    if arr[0][6][1]=="j" or arr[0][6][0]=="j" or arr[1][6][0]=="j"or not arr[1][6][1]=="j":
        return arr,""
    m1=arr[0][6][1][0]
    b1=arr[0][6][0][0]
    b2=arr[1][6][0][0]
    m2=[-2.5*log(b2/b1,10)+m1]
    arr[1][6][1]=m2
    return arr, "m2-m1=-2.5log(b2/b1)"

def Da1(arr):
    if arr[0][6][2]=="j"or not arr[0][5][0]=="j":
        return arr,""
    M=arr[0][6][2][0]
    L=luminConvert(10**((M-4.8)/-2.5), "sl")
    arr[0][5][0]=L
    return arr, "M=4.8-2.5log(Lstar/Lsun)"

def Db1(arr):
    if arr[0][5][0]=="j"or not arr[0][6][2]=="j":
        return arr,""
    L=arr[0][5][0][1]
    M=[4.8-2.5*log(L,10)]
    arr[0][6][2]=M
    return arr, "M=4.8-2.5log(Lstar/Lsun)"

def Da2(arr):
    if arr[1][6][2]=="j"or not arr[1][5][0]=="j":
        return arr,""
    M=arr[1][6][2][0]
    L=luminConvert(10**((M-4.8)/-2.5), "sl")
    arr[1][5][0]=L
    return arr, "M=4.8-2.5log(Lstar/Lsun)"

def Db2(arr):
    if arr[1][5][0]=="j"or not arr[1][6][2]=="j":
        return arr,""
    L=arr[1][5][0][1]
    M=[4.8-2.5*log(L,10)]
    arr[1][6][2]=M
    return arr, "M=4.8-2.5log(Lstar/Lsun)"

def Ea1(arr):
    if arr[0][0][1]=="j" or arr[0][6][3]=="j" or not arr[0][5][0]=="j":
        return arr,""
    R=arr[0][0][1][0]
    T=arr[0][6][3][0]
    L=luminConvert(4*pi*(R**2)*5.67e-8*(T**4),"w")
    arr[0][5][0]=L
    return arr, "L=4piR^2(5.67e-8)T^4"

def Eb1(arr):
    if arr[0][6][3]=="j" or arr[0][5][0]=="j" or not arr[0][0][1]=="j":
        return arr, ""
    T=arr[0][6][3][0]
    L=arr[0][5][0][0]
    R=lengthConvert(sqrt(L/(4*pi*5.67e-8*(T**4))), "m")
    arr[0][0][1]=R
    return arr, "L=4piR^2(5.67e-8)T^4"

def Ec1(arr):
    if arr[0][0][1]=="j" or arr[0][5][0]=="j" or not arr[0][6][3]=="j":
        return arr, ""
    R=arr[0][0][1][0]
    L=arr[0][5][0][0]
    T=[(L/(4*pi*(R**2)*5.67e-8))**(1/4)]
    arr[0][6][3]=T
    return arr, "L=4piR^2(5.67e-8)T^4"

def Ea2(arr):
    if arr[1][0][1]=="j" or arr[1][6][3]=="j" or not arr[1][5][0]=="j":
        return arr,""
    R=arr[1][0][1][0]
    T=arr[1][6][3][0]
    L=luminConvert(4*pi*(R**2)*5.67e-8*(T**4),"w")
    arr[1][5][0]=L
    return arr, "L=4piR^2(5.67e-8)T^4"

def Eb2(arr):
    if arr[1][6][3]=="j" or arr[1][5][0]=="j" or not arr[1][0][1]=="j":
        return arr, ""
    T=arr[1][6][3][0]
    L=arr[1][5][0][0]
    R=lengthConvert(sqrt(L/(4*pi*5.67e-8*(T**4))), "m")
    arr[1][0][1]=R
    return arr, "L=4piR^2(5.67e-8)T^4"

def Ec2(arr):
    if arr[1][0][1]=="j" or arr[1][5][0]=="j" or not arr[1][6][3]=="j":
        return arr, ""
    R=arr[1][0][1][0]
    L=arr[1][5][0][0]
    T=[(L/(4*pi*(R**2)*5.67e-8))**(1/4)]
    arr[1][6][3]=T
    return arr, "L=4piR^2(5.67e-8)T^4"

def Fa1(arr):
    if arr[0][6][3]=="j" or not arr[0][0][2]=="j":
        return arr, ""
    T=arr[0][6][3][0]
    w=lengthConvert(0.0029/T, "m")
    arr[0][0][2]=w
    return arr, "Max Wavelength=0.0029/T"

def Fb1(arr):
    if arr[0][0][2]=="j" or not arr[0][6][3]=="j":
        return arr, ""
    w=arr[0][0][2][0]
    T=[0.0029/w]
    arr[0][6][3]=T
    return arr, "Max Wavelength=0.0029/T"

def Fa2(arr):
    if arr[1][6][3]=="j" or not arr[1][0][2]=="j":
        return arr, ""
    T=arr[1][6][3][0]
    w=lengthConvert(0.0029/T, "m")
    arr[1][0][2]=w
    return arr, "Max Wavelength=0.0029/T"

def Fb2(arr):
    if arr[1][0][2]=="j" or not arr[1][6][3]=="j":
        return arr, ""
    w=arr[1][0][2][0]
    T=[0.0029/w]
    arr[1][6][3]=T
    return arr, "Max Wavelength=0.0029/T"

def Ga1(arr):
    if arr[0][3][0]=="j" or not arr[0][5][0]=="j":
        return arr,""
    M=arr[0][3][0][1]
    L=luminConvert(M**3.5,"sl")
    arr[0][5][0]=L
    return arr, "L=M^3.5"

def Gb1(arr):
    if arr[0][5][0]=="j" or not arr[0][3][0]=="j":
        return arr,""
    L=arr[0][5][0][1]
    M=massConvert(L**(1/3.5),"sm")
    arr[0][3][0]=M
    return arr, "L=M^3.5"

def Ga2(arr):
    if arr[1][3][0]=="j" or not arr[1][5][0]=="j":
        return arr,""
    M=arr[1][3][0][1]
    L=luminConvert(M**3.5,"sl")
    arr[1][5][0]=L
    return arr, "L=M^3.5"

def Gb2(arr):
    if arr[1][5][0]=="j" or not arr[1][3][0]=="j":
        return arr,""
    L=arr[1][5][0][1]
    M=massConvert(L**(1/3.5),"sm")
    arr[1][3][0]=M
    return arr, "L=M^3.5"

def Ia3(arr):
    if arr[2][1]=="j" or arr[2][0]=="j" or not arr[2][2]=="j":
        return arr,""
    a=arr[2][1][1]
    M=arr[2][0][1]
    p=timeConvert(sqrt(a**3/M),"yr")
    arr[2][2]=p
    return arr, "P^2=a^3/M"

def Ib3(arr):
    if arr[2][2]=="j" or arr[2][0]=="j" or not arr[2][1]=="j":
        return arr,""
    M=arr[2][0][1]
    p=arr[2][2][4]
    a=lengthConvert(((p**2)*M)**(1/3),"au")
    arr[2][1]=a
    return arr, "P^2=a^3/M"

def Ic3(arr):
    if arr[2][1]=="j" or arr[2][2]=="j" or not arr[2][0]=="j":
        return arr,""
    a=arr[2][1][1]
    p=arr[2][2][4]
    M=massConvert(a**3/p**2,"sm")
    arr[2][0]=M
    return arr, "P^2=a^3/M"
    
def Ja1(arr):
    if arr[0][3][0]=="j" or arr[0][0][1]=="j" or not arr[0][4][0]=="j":
        return arr,""
    M=arr[0][3][0][0]
    R=arr[0][0][1][0]
    v=velConvert(sqrt(2*6.67e-11*M/R),"m/s")
    arr[0][4][0]=v
    return arr, "Vesc=sqrt(2GM/R)"

def Jb1(arr):
    if arr[0][4][0]=="j" or arr[0][3][0]=="j" or not arr[0][0][1]=="j":
        return arr,""
    v=arr[0][4][0][0]
    M=arr[0][3][0][0]
    R=lengthConvert(2*6.67e-11*M/(v**2),"m")
    arr[0][0][1]=R
    return arr, "Vesc=sqrt(2GM/R)"

def Jc1(arr):
    if arr[0][4][0]=="j" or arr[0][0][1]=="j" or not arr[0][3][0]=="j":
        return arr,""
    v=arr[0][4][0][0]
    R=arr[0][0][1][0]
    M=massConvert(R*v**2/(2*6.67e-11),"kg")
    arr[0][3][0]=M
    return arr, "Vesc=sqrt(2GM/R)"

def Ja2(arr):
    if arr[1][3][0]=="j" or arr[1][0][1]=="j" or not arr[1][4][0]=="j":
        return arr,""
    M=arr[1][3][0][0]
    R=arr[1][0][1][0]
    v=velConvert(sqrt(2*6.67e-11*M/R),"m/s")
    arr[1][4][0]=v
    return arr, "Vesc=sqrt(2GM/R)"

def Jb2(arr):
    if arr[0][4][0]=="j" or arr[0][3][0]=="j" or not arr[0][0][1]=="j":
        return arr,""
    v=arr[0][4][0][0]
    M=arr[0][3][0][0]
    R=lengthConvert(2*6.67e-11*M/(v**2),"m")
    arr[0][0][1]=R
    return arr, "Vesc=sqrt(2GM/R)"

def Jc2(arr):
    if arr[0][4][0]=="j" or arr[0][0][1]=="j" or not arr[0][3][0]=="j":
        return arr,""
    v=arr[0][4][0][0]
    R=arr[0][0][1][0]
    M=massConvert(R*v**2/(2*6.67e-11),"kg")
    arr[0][3][0]=M
    return arr, "Vesc=sqrt(2GM/R)"

def Ka3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[0][0][3]=="j" or not arr[1][0][3]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m2=arr[1][3][0][1]
    a1=arr[0][0][3][1]
    a2=lengthConvert(m1*a1/m2,"au")
    arr[1][0][3]=a2
    return arr, "m1/m2=a2/a1"

def Kb3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[1][0][3]=="j" or not arr[0][0][3]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m2=arr[1][3][0][1]
    a2=arr[1][0][3][1]
    a1=lengthConvert(m2*a2/m1,"au")
    arr[0][0][3]=a1
    return arr, "m1/m2=a2/a1"

def Kc3(arr):
    if arr[1][3][0]=="j" or arr[0][0][3]=="j" or arr[1][0][3]=="j" or not arr[0][3][0]=="j":
        return arr,""
    m2=arr[1][3][0][1]
    a1=arr[0][0][3][1]
    a2=arr[1][0][3][1]
    m1=massConvert(a2*m2/a1,"sm")
    arr[0][3][0]=m1
    return arr, "m1/m2=a2/a1"

def Kd3(arr):
    if arr[0][3][0]=="j" or arr[0][0][3]=="j" or arr[1][0][3]=="j" or not arr[1][3][0]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    a1=arr[0][0][3][1]
    a2=arr[1][0][3][1]
    m2=massConvert(a1*m1/a2,"sm")
    arr[1][3][0]=m2
    return arr, "m1/m2=a2/a1"

def La3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[0][4][2]=="j" or not arr[1][4][2]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m2=arr[1][3][0][1]
    v1=arr[0][4][2][0]
    v2=velConvert(m1*v1/m2,"m/s")
    arr[1][4][2]=v2
    return arr, "m1/m2=v2/v1"

def Lb3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[1][4][2]=="j" or not arr[0][4][2]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m2=arr[1][3][0][1]
    v2=arr[1][4][2][0]
    v1=velConvert(m2*v2/m1,"m/s")
    arr[0][4][2]=v1
    return arr, "m1/m2=v2/v1"

def Lc3(arr):
    if arr[0][3][0]=="j" or arr[0][4][2]=="j" or arr[1][4][2]=="j" or not arr[1][3][0]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    m2=massConvert(m1*v1/v2,"sm")
    arr[1][3][0]=m2
    return arr, "m1/m2=v2/v1"

def Ld3(arr):
    if arr[1][3][0]=="j" or arr[0][4][2]=="j" or arr[1][4][2]=="j" or not arr[0][3][0]=="j":
        return arr,""
    m2=arr[1][3][0][1]
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    m1=massConvert(m2*v2/v1,"sm")
    arr[0][3][0]=m1
    return arr, "m1/m2=v2/v1"
    
def Ma3(arr):
    if arr[0][0][3]=="j" or arr[1][0][3]=="j" or arr[0][4][2]=="j" or not arr[1][4][2]=="j":
        return arr,""
    a1=arr[0][0][3][1]
    a2=arr[1][0][3][1]
    v1=arr[0][4][2][0]
    v2=velConvert(a2*v1/a1,"m/s")
    arr[1][4][2]=v2
    return arr, "a2/a1=v2/v1"

def Mb3(arr):
    if arr[0][0][3]=="j" or arr[1][0][3]=="j" or arr[1][4][2]=="j" or not arr[0][4][2]=="j":
        return arr,""
    a1=arr[0][0][3][1]
    a2=arr[1][0][3][1]
    v2=arr[1][4][2][0]
    v1=velConvert(a1*v2/a2,"m/s")
    arr[0][4][2]=v1
    return arr, "a2/a1=v2/v1"

def Mc3(arr):
    if arr[0][4][2]=="j" or arr[1][0][3]=="j" or arr[1][4][2]=="j" or not arr[0][0][3]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    a2=arr[1][0][3][1]
    v2=arr[1][4][2][0]
    a1=lengthConvert(a2*v1/v2,"au")
    arr[0][0][3]=a1
    return arr, "a2/a1=v2/v1"

def Md3(arr):
    if arr[0][4][2]=="j" or arr[0][0][3]=="j" or arr[1][4][2]=="j" or not arr[1][0][3]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    a1=arr[0][0][3][1]
    v2=arr[1][4][2][0]
    a2=lengthConvert(a1*v2/v1,"au")
    arr[1][0][3]=a2
    return arr, "a2/a1=v2/v1"

def Oa1(arr):
    if arr[0][2][0]=="j" or arr[0][4][2]=="j" or not arr[0][0][3]=="j":
        return arr,""
    P=arr[0][2][0][0]
    v=arr[0][4][2][0]
    a=lengthConvert(P*v/(2*pi),"m")
    arr[0][0][3]=a
    return arr, "Pv=2*pi*a"

def Ob1(arr):
    if arr[0][2][0]=="j" or arr[0][0][3]=="j" or not arr[0][4][2]=="j":
        return arr,""
    P=arr[0][2][0][0]
    a=arr[0][0][3][0]
    v=velConvert(2*pi*a/P,"m/s")
    arr[0][4][2]=v
    return arr, "Pv=2*pi*a"

def Oc1(arr):
    if arr[0][0][3]=="j" or arr[0][4][2]=="j" or not arr[0][2][0]=="j":
        return arr,""
    a=arr[0][0][3][0]
    v=arr[0][4][2][0]
    P=timeConvert(2*pi*a/v,"s")
    arr[0][2][0]=P
    return arr, "Pv=2*pi*a"

def Oa2(arr):
    if arr[1][2][0]=="j" or arr[1][4][2]=="j" or not arr[1][0][3]=="j":
        return arr,""
    P=arr[1][2][0][0]
    v=arr[1][4][2][0]
    a=lengthConvert(P*v/(2*pi),"m")
    arr[1][0][3]=a
    return arr, "Pv=2*pi*a"

def Ob2(arr):
    if arr[1][2][0]=="j" or arr[1][0][3]=="j" or not arr[1][4][2]=="j":
        return arr,""
    P=arr[1][2][0][0]
    a=arr[1][0][3][0]
    v=velConvert(2*pi*a/P,"m/s")
    arr[1][4][2]=v
    return arr, "Pv=2*pi*a"

def Oc2(arr):
    if arr[1][0][3]=="j" or arr[1][4][2]=="j" or not arr[1][2][0]=="j":
        return arr,""
    a=arr[1][0][3][0]
    v=arr[1][4][2][0]
    P=timeConvert(2*pi*a/v,"s")
    arr[1][2][0]=P
    return arr, "Pv=2*pi*a"

def Pa1(arr):
    if arr[0][1][1]=="j" or arr[0][0][0]=="j" or not arr[0][0][1]=="j":
        return arr,""
    a=arr[0][1][1][1]
    d=arr[0][0][0][0]
    R=lengthConvert((a*d/206265)/2,"m")
    arr[0][0][1]=R
    return arr, "D=ad/206265"

def Pb1(arr):
    if arr[0][0][1]=="j" or arr[0][0][0]=="j" or not arr[0][1][1]=="j":
        return arr,""
    R=arr[0][0][1][0]
    d=arr[0][0][0][0]
    a=angleConvert(2*R*206265/d,"as")
    arr[0][1][1]=a
    return arr, "D=ad/206265"

def Pc1(arr):
    if arr[0][1][1]=="j" or arr[0][0][1]=="j" or not arr[0][0][0]=="j":
        return arr,""
    a=arr[0][1][1][1]
    R=arr[0][0][1][0]
    d=lengthConvert(2*R*206265/a,"m")
    arr[0][0][0]=d
    return arr, "D=ad/206265"

def Pa2(arr):
    if arr[1][1][1]=="j" or arr[1][0][0]=="j" or not arr[1][0][1]=="j":
        return arr,""
    a=arr[1][1][1][1]
    d=arr[1][0][0][0]
    R=lengthConvert((a*d/206265)/2,"m")
    arr[1][0][1]=R
    return arr, "D=ad/206265"

def Pb2(arr):
    if arr[1][0][1]=="j" or arr[1][0][0]=="j" or not arr[1][1][1]=="j":
        return arr,""
    R=arr[1][0][1][0]
    d=arr[1][0][0][0]
    a=angleConvert(2*R*206265/d,"as")
    arr[1][1][1]=a
    return arr, "D=ad/206265"

def Pc2(arr):
    if arr[1][1][1]=="j" or arr[1][0][1]=="j" or not arr[1][0][0]=="j":
        return arr,""
    a=arr[1][1][1][1]
    R=arr[1][0][1][0]
    d=lengthConvert(2*R*206265/a,"m")
    arr[1][0][0]=d
    return arr, "D=ad/206265"

def Qa3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[2][1]=="j" or not arr[2][3]=="j":
        return arr,""
    m1=arr[0][3][0][0]
    m2=arr[1][3][0][0]
    r=arr[2][1][0]
    F=[6.67e-11*m1*m2/(r**2)]
    arr[2][3]=F
    return arr, "F=GMm/r^2"

def Qb3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or arr[2][3]=="j" or not arr[2][1]=="j":
        return arr,""
    m1=arr[0][3][0][0]
    m2=arr[1][3][0][0]
    F=arr[2][3][0]
    r=lengthConvert(sqrt(6.67e-11*m1*m2/F),"m")
    arr[2][1]=r
    return arr, "F=GMm/r^2"

def Qc3(arr):
    if arr[1][3][0]=="j" or arr[2][3]=="j" or arr[2][1]=="j" or not arr[0][3][0]=="j":
        return arr,""
    m2=arr[1][3][0][0]
    F=arr[2][3][0]
    r=arr[2][1][0]
    m1=massConvert(F*r**2/(6.67e-11*m2),"kg")
    arr[0][3][0]=m1
    return arr, "F=GMm/r^2"

def Qd3(arr):
    if arr[0][3][0]=="j" or arr[2][3]=="j" or arr[2][1]=="j" or not arr[1][3][0]=="j":
        return arr,""
    m1=arr[0][3][0][0]
    F=arr[2][3][0]
    r=arr[2][1][0]
    m2=massConvert(F*r**2/(6.67e-11*m1),"kg")
    arr[1][3][0]=m2
    return arr, "F=GMm/r^2"

def Ra1(arr):
    if arr[0][3][0]=="j" or arr[0][6][5]=="j" or not arr[2][3]=="j":
        return arr,""
    m=arr[0][3][0][0]
    a=arr[0][6][5][0]
    F=[m*a]
    arr[2][3]=F
    return arr, "F=ma"

def Rb1(arr):
    if arr[2][3]=="j" or arr[0][6][5]=="j" or not arr[0][3][0]=="j":
        return arr,""
    F=arr[2][3][0]
    a=arr[0][6][5][0]
    m=massConvert(F/a,"kg")
    arr[0][3][0]=m
    return arr, "F=ma"

def Rc1(arr):
    if arr[0][3][0]=="j" or arr[2][3]=="j" or not arr[0][6][5]=="j":
        return arr,""
    m=arr[0][3][0][0]
    F=arr[2][3][0]
    a=[F/m]
    arr[0][6][5]=a
    return arr, "F=ma"

def Ra2(arr):
    if arr[1][3][0]=="j" or arr[1][6][5]=="j" or not arr[2][3]=="j":
        return arr,""
    m=arr[1][3][0][0]
    a=arr[1][6][5][0]
    F=[m*a]
    arr[2][3]=F
    return arr, "F=ma"

def Rb2(arr):
    if arr[2][3]=="j" or arr[1][6][5]=="j" or not arr[1][3][0]=="j":
        return arr,""
    F=arr[2][3][0]
    a=arr[1][6][5][0]
    m=massConvert(F/a,"kg")
    arr[1][3][0]=m
    return arr, "F=ma"

def Rc2(arr):
    if arr[1][3][0]=="j" or arr[2][3]=="j" or not arr[1][6][5]=="j":
        return arr,""
    m=arr[1][3][0][0]
    F=arr[2][3][0]
    a=[F/m]
    arr[1][6][5]=a
    return arr, "F=ma"

def Sa1(arr):
    if arr[0][4][2]=="j" or arr[0][0][3]=="j" or not arr[0][6][5]=="j":
        return arr,""
    v=arr[0][4][2][0]
    r=arr[0][0][3][0]
    a=[v**2/r]
    arr[0][6][5]=a
    return arr, "a=v^2/r"

def Sb1(arr):
    if arr[0][4][2]=="j" or arr[0][6][5]=="j" or not arr[0][0][3]=="j":
        return arr,""
    v=arr[0][4][2][0]
    a=arr[0][6][5][0]
    r=lengthConvert(v**2/a,"m")
    arr[0][0][3]=r
    return arr, "a=v^2/r"

def Sc1(arr):
    if arr[0][6][5]=="j" or arr[0][0][3]=="j" or not arr[0][4][2]=="j":
        return arr,""
    a=arr[0][6][5][0]
    r=arr[0][0][3][0]
    v=velConvert(sqrt(r*a),"m/s")
    arr[0][4][2]=v
    return arr, "a=v^2/r"

def Sa2(arr):
    if arr[1][4][2]=="j" or arr[1][0][3]=="j" or not arr[1][6][5]=="j":
        return arr,""
    v=arr[1][4][2][0]
    r=arr[1][0][3][0]
    a=[v**2/r]
    arr[1][6][5]=a
    return arr, "a=v^2/r"

def Sb2(arr):
    if arr[1][4][2]=="j" or arr[1][6][5]=="j" or not arr[1][0][3]=="j":
        return arr,""
    v=arr[1][4][2][0]
    a=arr[1][6][5][0]
    r=lengthConvert(v**2/a,"m")
    arr[1][0][3]=r
    return arr, "a=v^2/r"

def Sc2(arr):
    if arr[1][6][5]=="j" or arr[1][0][3]=="j" or not arr[1][4][2]=="j":
        return arr,""
    a=arr[1][6][5][0]
    r=arr[1][0][3][0]
    v=velConvert(sqrt(r*a),"m/s")
    arr[1][4][2]=v
    return arr, "a=v^2/r"

def Ta1(arr):
    if arr[0][3][0]=="j" or arr[0][4][2]=="j" or not arr[0][6][6]=="j":
        return arr,""
    m=arr[0][3][0][0]
    v=arr[0][4][2][0]
    K=[0.5*m*(v**2)]
    arr[0][6][6]=K
    return arr, "KE=1/2mv^2"

def Tb1(arr):
    if arr[0][6][6]=="j" or arr[0][4][2]=="j" or not arr[0][3][0]=="j":
        return arr,""
    K=arr[0][6][6][0]
    v=arr[0][4][2][0]
    m=massConvert(2*K/(v**2),"kg")
    arr[0][3][0]=m
    return arr, "KE=1/2mv^2"

def Tc1(arr):
    if arr[0][3][0]=="j" or arr[0][6][6]=="j" or not arr[0][4][2]=="j":
        return arr,""
    m=arr[0][3][0][0]
    K=arr[0][6][6][0]
    v=velConvert(sqrt(2*K/m),"m/s")
    arr[0][4][2]=v
    return arr, "KE=1/2mv^2"

def Ta2(arr):
    if arr[1][3][0]=="j" or arr[1][4][2]=="j" or not arr[1][6][6]=="j":
        return arr,""
    m=arr[1][3][0][0]
    v=arr[1][4][2][0]
    K=[0.5*m*(v**2)]
    arr[1][6][6]=K
    return arr, "KE=1/2mv^2"

def Tb2(arr):
    if arr[1][6][6]=="j" or arr[1][4][2]=="j" or not arr[1][3][0]=="j":
        return arr,""
    K=arr[1][6][6][0]
    v=arr[1][4][2][0]
    m=massConvert(2*K/(v**2),"kg")
    arr[1][3][0]=m
    return arr, "KE=1/2mv^2"

def Tc2(arr):
    if arr[1][3][0]=="j" or arr[1][6][6]=="j" or not arr[1][4][2]=="j":
        return arr,""
    m=arr[1][3][0][0]
    K=arr[1][6][6][0]
    v=velConvert(sqrt(2*K/m),"m/s")
    arr[1][4][2]=v
    return arr, "KE=1/2mv^2"

def Ua3(arr):
    if arr[2][3]=="j" or arr[2][1]=="j" or not arr[2][4]=="j":
        return arr,""
    F=arr[2][3][0]
    r=arr[2][1][0]
    U=[F*r]
    arr[2][4]=U
    return arr, "U=F*r"

def Ub3(arr):
    if arr[2][3]=="j" or arr[2][4]=="j" or not arr[2][1]=="j":
        return arr,""
    F=arr[2][3][0]
    U=arr[2][4][0]
    r=[U/F]
    arr[2][1]=r
    return arr, "U=F*r"

def Uc3(arr):
    if arr[2][1]=="j" or arr[2][4]=="j" or not arr[2][3]=="j":
        return arr,""
    r=arr[2][1][0]
    U=arr[2][4][0]
    F=[U/r]
    arr[2][3]=F
    return arr, "U=F*r"

def Va1(arr):
    if arr[0][3][0]=="j" or arr[0][0][1]=="j" or arr[0][4][2]=="j" or not arr[0][6][8]=="j":
        return arr,""
    m=arr[0][3][0][0]
    r=arr[0][0][3][0]
    v=arr[0][4][2][0]
    L=[m*r*v]
    arr[0][6][8]=L
    return arr, "L=mrv"

def Vb1(arr):
    if arr[0][6][8]=="j" or arr[0][0][1]=="j" or arr[0][4][2]=="j" or not arr[0][3][0]=="j":
        return arr,""
    L=arr[0][6][8][0]
    r=arr[0][0][3][0]
    v=arr[0][4][2][0]
    m=massConvert(L/(r*v),"kg")
    arr[0][3][0]=m
    return arr, "L=mrv"

def Vc1(arr):
    if arr[0][3][0]=="j" or arr[0][6][8]=="j" or arr[0][4][2]=="j" or not arr[0][0][1]=="j":
        return arr,""
    m=arr[0][3][0][0]
    L=arr[0][6][8][0]
    v=arr[0][4][2][0]
    r=lengthConvert(L/(m*v),"m")
    arr[0][0][3]=r
    return arr, "L=mrv"

def Vd1(arr):
    if arr[0][3][0]=="j" or arr[0][0][1]=="j" or arr[0][6][8]=="j" or not arr[0][4][2]=="j":
        return arr,""
    m=arr[0][3][0][0]
    r=arr[0][0][3][0]
    L=arr[0][6][8][0]
    v=velConvert(L/(m*r),"m/s")
    arr[0][4][2]=v
    return arr, "L=mrv"

def Va2(arr):
    if arr[1][3][0]=="j" or arr[1][0][1]=="j" or arr[1][4][2]=="j" or not arr[1][6][8]=="j":
        return arr,""
    m=arr[1][3][0][0]
    r=arr[1][0][3][0]
    v=arr[1][4][2][0]
    L=[m*r*v]
    arr[1][6][8]=L
    return arr, "L=mrv"

def Vb2(arr):
    if arr[1][6][8]=="j" or arr[1][0][1]=="j" or arr[1][4][2]=="j" or not arr[1][3][0]=="j":
        return arr,""
    L=arr[1][6][8][0]
    r=arr[1][0][3][0]
    v=arr[1][4][2][0]
    m=massConvert(L/(r*v),"kg")
    arr[1][3][0]=m
    return arr, "L=mrv"

def Vc2(arr):
    if arr[1][3][0]=="j" or arr[1][6][8]=="j" or arr[1][4][2]=="j" or not arr[1][0][1]=="j":
        return arr,""
    m=arr[1][3][0][0]
    L=arr[1][6][8][0]
    v=arr[1][4][2][0]
    r=lengthConvert(L/(m*v),"m")
    arr[1][0][3]=r
    return arr, "L=mrv"

def Vd2(arr):
    if arr[1][3][0]=="j" or arr[1][0][1]=="j" or arr[1][6][8]=="j" or not arr[1][4][2]=="j":
        return arr,""
    m=arr[1][3][0][0]
    r=arr[1][0][3][0]
    L=arr[1][6][8][0]
    v=velConvert(L/(m*r),"m/s")
    arr[1][4][2]=v
    return arr, "L=mrv"
    
def Wa3(arr):
    if arr[0][0][3]=="j" or arr[1][0][3]=="j" or not arr[2][1]=="j":
        return arr,""
    a1=arr[0][0][3][1]
    a2=arr[1][0][3][1]
    a=lengthConvert(a1+a2,"au")
    arr[2][1]=a
    return arr, "a=a1+a2"

def Wb3(arr):
    if arr[2][1]=="j" or arr[0][0][3]=="j" or not arr[1][0][3]=="j":
        return arr,""
    a=arr[2][1][1]
    a1=arr[0][0][3][1]
    a2=lengthConvert(a-a1,"au")
    arr[1][0][3]=a2
    return arr, "a=a1+a2"

def Wc3(arr):
    if arr[2][1]=="j" or arr[1][0][3]=="j" or not arr[0][0][3]=="j":
        return arr,""
    a=arr[2][1][1]
    a2=arr[1][0][3][1]
    a1=lengthConvert(a-a2,"au")
    arr[0][0][3]=a1
    return arr, "a=a1+a2"

def Xa3(arr):
    if arr[0][3][0]=="j" or arr[1][3][0]=="j" or not arr[2][0]=="j":
        return arr,""
    M1=arr[0][3][0][1]
    M2=arr[1][3][0][1]
    Mtotal=M1+M2
    arr[2][0]=massConvert(Mtotal,"sm")
    return arr, "Total Mass=M1+M2"

def Xb3(arr):
    if arr[2][0]=="j" or arr[0][3][0]=="j" or not arr[1][3][0]=="j":
        return arr,""
    Mtotal=arr[2][0][1]
    M1=arr[0][3][0][1]
    M2=massConvert(Mtotal-M1,"sm")
    arr[1][3][0]=M2
    return arr, "Total Mass=M1+M2"

def Xc3(arr):
    if arr[2][0]=="j" or arr[1][3][0]=="j" or not arr[0][3][0]=="j":
        return arr,""
    Mtotal=arr[2][0][1]
    M2=arr[1][3][0][1]
    M1=massConvert(Mtotal-M2,"sm")
    arr[0][3][0]=M1
    return arr, "Total Mass=M1+M2"

def Ya1(arr):
    if arr[0][0][0]=="j" or arr[0][6][2]=="j" or not arr[0][6][1]=="j":
        return arr,""
    d=arr[0][0][0][3]
    M=arr[0][6][2][0]
    m=[M+5*log(d,10)-5]
    arr[0][6][1]=m
    return arr, "m-M=5log(d)-5"

def Yb1(arr):
    if arr[0][0][0]=="j" or arr[0][6][1]=="j" or not arr[0][6][2]=="j":
        return arr,""
    d=arr[0][0][0][3]
    m=arr[0][6][1][0]
    M=[m-5*log(d,10)+5]
    arr[0][6][2]=M
    return arr, "m-M=5log(d)-5"

def Yc1(arr):
    if arr[0][6][1]=="j" or arr[0][6][2]=="j" or not arr[0][0][0]=="j":
        return arr,""
    m=arr[0][6][1][0]
    M=arr[0][6][2][0]
    d=lengthConvert(10**((m-M+5)/5),"pc")
    arr[0][0][0]=d
    return arr, "m-M=5log(d)-5"

def Ya2(arr):
    if arr[1][0][0]=="j" or arr[1][6][2]=="j" or not arr[1][6][1]=="j":
        return arr,""
    d=arr[1][0][0][3]
    M=arr[1][6][2][0]
    m=[M+5*log(d,10)-5]
    arr[1][6][1]=m
    return arr, "m-M=5log(d)-5"

def Yb2(arr):
    if arr[1][0][0]=="j" or arr[1][6][1]=="j" or not arr[1][6][2]=="j":
        return arr,""
    d=arr[1][0][0][3]
    m=arr[1][6][1][0]
    M=[m-5*log(d,10)+5]
    arr[1][6][2]=M
    return arr, "m-M=5log(d)-5"

def Yc2(arr):
    if arr[1][6][1]=="j" or arr[1][6][2]=="j" or not arr[1][0][0]=="j":
        return arr,""
    m=arr[1][6][1][0]
    M=arr[1][6][2][0]
    d=lengthConvert(10**((m-M+5)/5),"pc")
    arr[1][0][0]=d
    return arr, "m-M=5log(d)-5"

def Za3(arr):
    if arr[0][3][0]=="j" or arr[2][0]=="j" or arr[2][1]=="j" or not arr[1][0][3]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m=arr[2][0][1]
    a=arr[2][1][1]
    a2=lengthConvert(m1*a/m,"au")
    arr[1][0][3]=a2
    return arr, "a2=(m1/mtotal)a"

def Zb3(arr):
    if arr[0][3][0]=="j" or arr[2][0]=="j" or arr[1][0][3]=="j" or not arr[2][1]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    m=arr[2][0][1]
    a2=arr[1][0][3][1]
    a=lengthConvert(a2*m/m1,"au")
    arr[2][1]=a
    return arr, "a2=(m1/mtotal)a"

def Zc3(arr):
    if arr[0][3][0]=="j" or arr[2][1]=="j" or arr[1][0][3]=="j" or not arr[2][0]=="j":
        return arr,""
    m1=arr[0][3][0][1]
    a=arr[2][1][1]
    a2=arr[1][0][3][1]
    m=massConvert(m1*a/a2,"sm")
    arr[2][0]=m
    return arr, "a2=(m1/mtotal)a"

def Zd3(arr):
    if arr[2][0]=="j" or arr[2][1]=="j" or arr[1][0][3]=="j" or not arr[0][3][0]=="j":
        return arr,""
    m=arr[2][0][1]
    a=arr[2][1][1]
    a2=arr[1][0][3][1]
    m1=massConvert(a2*m/a,"sm")
    arr[0][3][0]=m1
    return arr, "a2=(m1/mtotal)a"

def Ze3(arr):
    if arr[1][3][0]=="j" or arr[2][0]=="j" or arr[2][1]=="j" or not arr[0][0][3]=="j":
        return arr,""
    m2=arr[1][3][0][1]
    m=arr[2][0][1]
    a=arr[2][1][1]
    a1=lengthConvert(m2*a/m,"au")
    arr[0][0][3]=a1
    return arr, "a1=(m2/mtotal)a"

def Zf3(arr):
    if arr[1][3][0]=="j" or arr[2][0]=="j" or arr[0][0][3]=="j" or not arr[2][1]=="j":
        return arr,""
    m2=arr[1][3][0][1]
    m=arr[2][0][1]
    a1=arr[0][0][3][1]
    a=lengthConvert(a1*m/m2,"au")
    arr[2][1]=a
    return arr, "a1=(m2/mtotal)a"

def Zg3(arr):
    if arr[1][3][0]=="j" or arr[2][1]=="j" or arr[0][0][3]=="j" or not arr[2][0]=="j":
        return arr,""
    m2=arr[1][3][0][1]
    a=arr[2][1][1]
    a1=arr[0][0][3][1]
    m=massConvert(m2*a/a1,"sm")
    arr[2][0]=m
    return arr, "a1=(m2/mtotal)a"

def Zh3(arr):
    if arr[2][0]=="j" or arr[2][1]=="j" or arr[0][0][3]=="j" or not arr[1][3][0]=="j":
        return arr,""
    m=arr[2][0][1]
    a=arr[2][1][1]
    a1=arr[0][0][3][1]
    m2=massConvert(a1*m/a,"sm")
    arr[1][3][0]=m2
    return arr, "a1=(m2/mtotal)a"

def AAa3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[2][0]=="j" or not arr[0][3][0]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    M=arr[2][0][1]
    m1=massConvert(v2*M/(v1+v2),"sm")
    arr[0][3][0]=m1
    return arr, "v2/(v1+v2)=m1/(m1+m2)"

def AAb3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[0][3][0]=="j" or not arr[2][0]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    m1=arr[0][3][0][1]
    M=massConvert(m1*(v1+v2)/v2,"sm")
    arr[2][0]=M
    return arr, "v2/(v1+v2)=m1/(m1+m2)"

def AAc3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[2][0]=="j" or not arr[1][3][0]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    M=arr[2][0][1]
    m2=massConvert(v1*M/(v1+v2),"sm")
    arr[1][3][0]=m2
    return arr, "v1/(v1+v2)=m2/(m1+m2)"

def AAd3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[1][3][0]=="j" or not arr[2][0]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    m2=arr[1][3][0][1]
    M=massConvert(m2*(v1+v2)/v1,"sm")
    arr[2][0]=M
    return arr, "v1/(v1+v2)=m2/(m1+m2)"

def BBa3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[1][0][3]=="j" or not arr[2][1]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    a2=arr[1][0][3][1]
    a=lengthConvert(a2*(v1+v2)/v2,"au")
    arr[2][1]=a
    return arr, "a2/a=v2/(v1+v2)"

def BBb3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[2][1]=="j" or not arr[1][0][3]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    a=arr[2][1][1]
    a2=lengthConvert(v2*a/(v1+v2),"au")
    arr[1][0][3]=a2
    return arr, "a2/a=v2/(v1+v2)"

def BBc3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[0][0][3]=="j" or not arr[2][1]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    a1=arr[0][0][3][1]
    a=lengthConvert(a1*(v1+v2)/v1,"au")
    arr[2][1]=a
    return arr, "a1/a=v1/(v1+v2)"

def BBd3(arr):
    if arr[0][4][2]=="j" or arr[1][4][2]=="j" or arr[2][1]=="j" or not arr[0][0][3]=="j":
        return arr,""
    v1=arr[0][4][2][0]
    v2=arr[1][4][2][0]
    a=arr[2][1][1]
    a1=lengthConvert(v1*a/(v1+v2),"au")
    arr[0][0][3]=a1
    return arr, "a2/a=v2/(v1+v2)"

def CCa1(arr):
    if arr[0][6][9]=="j" or not arr[0][6][3]=="j":
        return arr,""
    f=arr[0][6][9][0]
    T=[(f/(5.67e-8))**(1/4)]
    arr[0][6][3]=T
    return arr, "F=5.67e-8*T^4"

def CCb1(arr):
    if arr[0][6][3]=="j" or not arr[0][6][9]=="j":
        return arr,""
    T=arr[0][6][3][0]
    f=[5.67e-8*(T**4)]
    arr[0][6][9]=f
    return arr, "F=5.67e-8*T^4"

def CCa2(arr):
    if arr[1][6][9]=="j" or not arr[1][6][3]=="j":
        return arr,""
    f=arr[1][6][9][0]
    T=[(f/(5.67e-8))**(1/4)]
    arr[1][6][3]=T
    return arr, "F=5.67e-8*T^4"

def CCb2(arr):
    if arr[1][6][3]=="j" or not arr[1][6][9]=="j":
        return arr,""
    T=arr[1][6][3][0]
    f=[5.67e-8*(T**4)]
    arr[1][6][9]=f
    return arr, "F=5.67e-8*T^4"


        
#This part reads the file, converts values, and places them into the allObjs array
print ("Astronomy Calculator 3.0.0************Camas High School************Jason Kim\n")
inFile=open("Astro3In.txt","r")
fileList=inFile.read().split()
numOfValues= int(len(fileList)/4)

for x in range(0, numOfValues):
    obj= int(fileList[x*4])
    valType= int(fileList[x*4+1])
    value= float(fileList[x*4+2])
    units= fileList[x*4+3]

    if obj==1 or obj==2:
        unitType=6
        valArray=[value]
        if units=="m" or units=="au" or units=="ly" or units=="pc" or units=="a" or units=="nm" or units=="rs":
            unitType=0
            valArray=lengthConvert(value, units)
        if units=="deg" or units=="as" or units=="rad":
            unitType=1
            valArray=angleConvert(value, units)
        if units=="s" or units=="min" or units=="hr" or units=="day" or units=="yr":
            unitType=2
            valArray=timeConvert(value, units)
        if units=="kg" or units=="sm":
            unitType=3
            valArray=massConvert(value, units)
        if units=="m/s" or units=="km/s":
            unitType=4
            valArray=velConvert(value, units)
        if units=="w" or units=="sl":
            unitType=5
            valArray=luminConvert(value, units)
        allObjs[obj-1][unitType][valType]=valArray
    else:
        if valType==0:
            valArray=massConvert(value, units)
        if valType==1:
            valArray=lengthConvert(value, units)
        if valType==2:
            valArray=timeConvert(value, units)
        if valType==3:
            valArray=[value]
        if valType==4:
            valArray=[value]
        allObjs[obj-1][valType]=valArray

        

#Calculating Process begins here

def inLoop(func):
    ph=func
    if not ph[1]=="":
        print (ph[1])
    return ph[0]

def runLoop(arr):
    arr=inLoop(Aa1(arr))
    arr=inLoop(Ab1(arr))
    arr=inLoop(Aa2(arr))
    arr=inLoop(Ab2(arr))
    arr=inLoop(Ba1(arr))
    arr=inLoop(Bb1(arr))
    arr=inLoop(Bc1(arr))
    arr=inLoop(Ba2(arr))
    arr=inLoop(Bb2(arr))
    arr=inLoop(Bc2(arr))
    arr=inLoop(Ca3(arr))
    arr=inLoop(Cb3(arr))
    arr=inLoop(Cc3(arr))
    arr=inLoop(Cd3(arr))
    arr=inLoop(Da1(arr))
    arr=inLoop(Db1(arr))
    arr=inLoop(Da2(arr))
    arr=inLoop(Db2(arr))
    arr=inLoop(Ea1(arr))
    arr=inLoop(Eb1(arr))
    arr=inLoop(Ec1(arr))
    arr=inLoop(Ea2(arr))
    arr=inLoop(Eb2(arr))
    arr=inLoop(Ec2(arr))
    arr=inLoop(Fa1(arr))
    arr=inLoop(Fb1(arr))
    arr=inLoop(Fa2(arr))
    arr=inLoop(Fb2(arr))
    arr=inLoop(Ga1(arr))
    arr=inLoop(Gb1(arr))
    arr=inLoop(Ga2(arr))
    arr=inLoop(Gb2(arr))
    arr=inLoop(Ia3(arr))
    arr=inLoop(Ib3(arr))
    arr=inLoop(Ic3(arr))
    arr=inLoop(Ja1(arr))
    arr=inLoop(Jb1(arr))
    arr=inLoop(Jc1(arr))
    arr=inLoop(Ja2(arr))
    arr=inLoop(Jb2(arr))
    arr=inLoop(Jc2(arr))
    arr=inLoop(Ka3(arr))
    arr=inLoop(Kb3(arr))
    arr=inLoop(Kc3(arr))
    arr=inLoop(Kd3(arr))
    arr=inLoop(La3(arr))
    arr=inLoop(Lb3(arr))
    arr=inLoop(Lc3(arr))
    arr=inLoop(Ld3(arr))
    arr=inLoop(Ma3(arr))
    arr=inLoop(Mb3(arr))
    arr=inLoop(Mc3(arr))
    arr=inLoop(Md3(arr))
    arr=inLoop(Oa1(arr))
    arr=inLoop(Ob1(arr))
    arr=inLoop(Oc1(arr))
    arr=inLoop(Oa2(arr))
    arr=inLoop(Ob2(arr))
    arr=inLoop(Oc2(arr))
    arr=inLoop(Pa1(arr))
    arr=inLoop(Pb1(arr))
    arr=inLoop(Pc1(arr))
    arr=inLoop(Pa2(arr))
    arr=inLoop(Pb2(arr))
    arr=inLoop(Pc2(arr))
    arr=inLoop(Qa3(arr))
    arr=inLoop(Qb3(arr))
    arr=inLoop(Qc3(arr))
    arr=inLoop(Qd3(arr))
    arr=inLoop(Ra1(arr))
    arr=inLoop(Rb1(arr))
    arr=inLoop(Rc1(arr))
    arr=inLoop(Ra2(arr))
    arr=inLoop(Rb2(arr))
    arr=inLoop(Rc2(arr))
    arr=inLoop(Sa1(arr))
    arr=inLoop(Sb1(arr))
    arr=inLoop(Sc1(arr))
    arr=inLoop(Sa2(arr))
    arr=inLoop(Sb2(arr))
    arr=inLoop(Sc2(arr))
    arr=inLoop(Ta1(arr))
    arr=inLoop(Tb1(arr))
    arr=inLoop(Tc1(arr))
    arr=inLoop(Ta2(arr))
    arr=inLoop(Tb2(arr))
    arr=inLoop(Tc2(arr))
    arr=inLoop(Ua3(arr))
    arr=inLoop(Ub3(arr))
    arr=inLoop(Uc3(arr))
    arr=inLoop(Va1(arr))
    arr=inLoop(Vb1(arr))
    arr=inLoop(Vc1(arr))
    arr=inLoop(Vd1(arr))
    arr=inLoop(Va2(arr))
    arr=inLoop(Vb2(arr))
    arr=inLoop(Vc2(arr))
    arr=inLoop(Vd2(arr))
    arr=inLoop(Wa3(arr))
    arr=inLoop(Wb3(arr))
    arr=inLoop(Wc3(arr))
    arr=inLoop(Xa3(arr))
    arr=inLoop(Xb3(arr))
    arr=inLoop(Xc3(arr))
    arr=inLoop(Ya1(arr))
    arr=inLoop(Yb1(arr))
    arr=inLoop(Yc1(arr))
    arr=inLoop(Ya2(arr))
    arr=inLoop(Yb2(arr))
    arr=inLoop(Yc2(arr))
    arr=inLoop(Za3(arr))
    arr=inLoop(Zb3(arr))
    arr=inLoop(Zc3(arr))
    arr=inLoop(Zd3(arr))
    arr=inLoop(Ze3(arr))
    arr=inLoop(Zf3(arr))
    arr=inLoop(Zg3(arr))
    arr=inLoop(Zh3(arr))
    arr=inLoop(AAa3(arr))
    arr=inLoop(AAb3(arr))
    arr=inLoop(AAc3(arr))
    arr=inLoop(AAd3(arr))
    arr=inLoop(BBa3(arr))
    arr=inLoop(BBb3(arr))
    arr=inLoop(BBc3(arr))
    arr=inLoop(BBd3(arr))
    arr=inLoop(CCa1(arr))
    arr=inLoop(CCb1(arr))
    arr=inLoop(CCa2(arr))
    arr=inLoop(CCb2(arr))
    return arr
    
loop=True
while loop==True:
    allObjs0=deepcopy(allObjs)
    allObjs=runLoop(allObjs)
    if allObjs0==allObjs:
        loop=False

#Loop terminates when there are no more updates in the allObjs array

        

#This is the print out
for x in range(0, len(allObjs)):
    if x==0 or x==1:
        for y in range(0, len(allObjs[x])):
            for z in range(0, len(allObjs[x][y])):
                if not "j" in str(allObjs[x][y][z]):
                    print ("\n"+allObjsNames[x][y][z])
                    for a in range(0, len(allObjs[x][y][z])):
                        if y==6:
                            print (str(allObjs[x][y][z][a])+" "+unitsArray[y][z])
                        else:
                            print (str(allObjs[x][y][z][a])+" "+unitsArray[y][a])
    else:
        for y in range(0, len(allObjs[x])):
            if not "j" in str(allObjs[x][y]):
                print ("\n"+allObjsNames[x][y])
                for a in range(0, len(allObjs[x][y])):
                    if y==0:
                        print (str(allObjs[x][y][a])+" "+unitsArray[3][a])
                    if y==1:
                        print (str(allObjs[x][y][a])+" "+unitsArray[0][a])
                    if y==2:
                        print (str(allObjs[x][y][a])+" "+unitsArray[2][a])
                    if y==3:
                        print (str(allObjs[x][y][a])+" N")
                    if y==4:
                        print (str(allObjs[x][y][a])+" J")

