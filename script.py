import math
import numpy as np
import math
import utils
from sage.all import EllipticCurve

# Family E analysis: ================================== #

def Get_Distribution_J_invariants_in_family_E(Xmax):

    # This function receives a positive real number X>0 and returns the distribution of j-invariants for elliptic curves
    # that belong to the family of curves E_{a, b}: y^2 = x^3 + ax +b over integers (a,b) subject to the conditions that
    # E_{a, b} is an elliptic curve and that there is no prime p with
    # p^4|a and p^6|b, and with naive height h(E_{a, b}) := max(4|a|^3, 27|b|^2) <= Xmax

    possible_j_invariants = [0.0, 1728.0, -3375.0, 8000.0, -32768.0, 54000.0, 287496.0, -12288000.0,
                             16581375.0, -884736.0, -884736000.0, -147197952000.0, -262537412640768000.0]

    print(f'Looking elliptic curves with naive height < {Xmax} in family E:')

    a_bound = math.floor((Xmax/4)**(1/3))
    b_bound = math.floor(math.sqrt(Xmax/27))
    a_bound_range = range(-a_bound, a_bound + 1)
    b_bound_range = range(-b_bound, b_bound + 1)

    List_of_Elliptic_Curves = []
    for a in a_bound_range:
        for b in b_bound_range:
            if utils.disc(a, b) != 0 and utils.prime_condition(a, b):
                List_of_Elliptic_Curves.append([a, b])

    print(f'Total number of curves: {len(List_of_Elliptic_Curves)}')

    j_invariants = []

    # For each elliptic curve in this partition, check if they satisfy
    for curve in List_of_Elliptic_Curves:
        a, b = curve[0], curve[1]
        j_invariant = 2**8*((3**3)*(a**3))/(4*(a**3) + 27*(b**2))
        if j_invariant in possible_j_invariants:
            j_invariants.append(j_invariant)

    unique, counts = np.unique(j_invariants, return_counts=True)
    dict_ = dict(zip(unique, counts))
    dict_ = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))

    return dict_

# Family ET analysis: ================================== #

def Get_Distribution_J_invariants_in_family_ET(Xmax):
    # Computes the distribution of j-invariants
    # the family ET , focusing on curves that have complex multiplication (CM).
    fixed_curves_dict = {
        0 : (0, 1),
        54000 : (-15, 22),
        -12288000 : (-120, 506),
        1728 : (1,0),
        287496 : (-11, 14),
        -3375 : (35, 98),
        16581375 : (-595, 5586),
        8000 : (-30, 56),
        -32768 : (-1056, 13552),
        -884736 : (-152, 722),
        -88473600 : (-3440, 77658),
        -147197952000 : (-29480, 1948226),
        -262537412640768000 : (-34790720, 78984748304)
    }

    count_dict = {}

    for j in fixed_curves_dict.keys():

        a_j = fixed_curves_dict[j][0]
        b_j = fixed_curves_dict[j][1]
        
        fixed_curve_height = utils.naive_height(a=a_j, b=b_j)
        
        if j == 0:
            n_j = 6
            m_j = 2
        elif j == 1728:
            n_j = 4
            m_j = 3
        else:
            n_j = 2
            m_j = 6

        bound = math.pow(1/fixed_curve_height, 1/m_j)*math.pow(Xmax, 1/m_j) 
        power_free_ints = utils.get_power_free_integers(X=bound, k=n_j)

        number_of_cm_curves = 0

        for d in power_free_ints:

            if j == 0:
                a = 0
                b = d*b_j
            elif j == 1728:
                a = d*a_j
                b = 0
            else:
                a = (d**2)*a_j
                b = (d**3)*b_j

            if EllipticCurve([a, b]).has_cm():
                number_of_cm_curves = number_of_cm_curves + 1
        
        count_dict[j] = number_of_cm_curves

    dict_ = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
    return dict_


if __name__ == '__main__':
    
    Xmax = 10**5

    distE = Get_Distribution_J_invariants_in_family_E(Xmax)
    print(f'Distribution in family E up to X={Xmax}')
    print(distE)

    distET = Get_Distribution_J_invariants_in_family_ET(Xmax)
    print(f'Distribution in family ET up to X={Xmax}')
    print(distET)