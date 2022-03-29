from math import *

def calculate_theta(Ts,Ta):
    return Ts - Ta

def calculate_m(h,P,k,A):
    return sqrt((h*P)/(k*A))

def calculate_M(h,P,A,k,theta):
    return sqrt(h*P*A*k) * theta

def fin_heat_transfer(M,m,L,h,k):

    num= sinh(m*L) + (h/(m*k)) * cosh(m*L)

    den= cosh(m*L) + (h/(m*k)) * sinh(m*L)

    return M * (num/den)


def fin_temp_distribution(m,L,h,k,x):

    num = cosh(m*(L-x)) + (h/(m*k)) * sinh(m*(L-x))

    den = cosh(m*L) + (h/(m*k)) * sinh(m*L)

    return (num/den)

def effectiveness(qa,h,Ab,theta):

    return qa/(h*Ab*theta)

def efficiency(qa,h,As,theta):

    return qa/(h*As*theta)

def temperature(tamb, text, temp_distrib):
    return temp_distrib*(text - tamb) + tamb
