import math
import numpy as np
import math
import utils
import os
import json
import multiprocessing
import functools
import re

path = os.getcwd()

# Run j-invariant distribution computations in parallel

def get_results(i, n, a_bound_range, b_bound_range, Xmin, possible_j_invariants):

    # To parallelize the procedure we partition the range of 'a' values for all the elliptic curves E_{a,b}
    # in family E

    print(f"Partition {int(i / n)} --->")
    a_use = a_bound_range[i:i+n]

    List_of_Elliptic_Curves = []
    for a in a_use:
        for b in b_bound_range:
            if utils.disc(a, b) != 0 and utils.prime_condition(a, b) and utils.naive_height(a,b) > Xmin:
                List_of_Elliptic_Curves.append([a, b])
        
    print(f'Number of elliptic curves to study for this partition: {len(List_of_Elliptic_Curves)}')
    j_invariants = []
    for curve in List_of_Elliptic_Curves:
        a, b = curve[0], curve[1]
        j_invariant = 2**8*((3**3)*(a**3))/(4*(a**3) + 27*(b**2))
        if j_invariant in possible_j_invariants:
            j_invariants.append(j_invariant)

    unique, counts = np.unique(j_invariants, return_counts=True)
    dict_ = dict(zip(unique, counts))
    dict_ = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
    dict_ = {str(k):str(v) for k,v in dict_.items()}
    dict_['total_curves'] = len(List_of_Elliptic_Curves)

    # Store the partial results
    with open(f'{path}/partial_results_{i}.json', 'w') as f:
        json.dump(dict_, f)
        print('file written')

    return dict_


def Get_Distribution_J_invariants_in_family_E(Xmax, **kwargs):

    possible_j_invariants = [0.0, 1728.0, -3375.0, 8000.0, -32768.0, 54000.0, 287496.0, -12288000.0,
                             16581375.0, -884736.0, -884736000.0, -147197952000.0, -262537412640768000.0]

    Xmin = kwargs.get('Xmin', 0)
    print(f'Looking elliptic curves with naive height between {Xmin} and {Xmax} in family E:')

    a_bound = math.floor((Xmax/4)**(1/3))
    b_bound = math.floor(math.sqrt(Xmax/27))
    a_bound_range = range(-a_bound, a_bound + 1)
    b_bound_range = range(-b_bound, b_bound + 1)

    n = 100 # We will partition the (a,b) range of coefficient posibilities.
    # How many values of the coefficient 'a' do we want at each partition.
    print(f"Number of partitions {len(range(0, len(a_bound_range), n))}")

    n_cores = 3
    pool = multiprocessing.Pool(n_cores)
    _ = pool.map(functools.partial(get_results, n=n, a_bound_range=a_bound_range,
                                   b_bound_range=b_bound_range,
                                   Xmin=Xmin,
                                   possible_j_invariants=possible_j_invariants),
                                   range(0, len(a_bound_range), n))
    pool.close()
    pool.join()

    # Read all partial result files and merge them to create a total dictionary
    regex = re.compile('(partial_results.*json$)')
    total_dict = {}
    for _, _, files in os.walk(path):
        for file in files:
            if regex.match(file):
                try:
                    print(file)
                    f = open(f'{path}/{file}')
                    data = json.load(f)
                    for k,v in data.items():
                        total_dict[k] = total_dict.get(k, 0) + int(v)
                    os.remove(f'{path}/{file}')
                except Exception as e:
                    print(f'Error with file {file}: {e}')

    return total_dict


if __name__ == '__main__':
    
    Xmax = 10**8

    distE = Get_Distribution_J_invariants_in_family_E(Xmax)
    print(f'Distribution in family E up to X={Xmax}')
    print(distE)