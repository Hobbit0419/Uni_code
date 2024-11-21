from itertools import product

def uttryck(P):
    lhs = ((P[0] or P[1]) and (P[2] or P[3]) and (P[4] or P[5]))
    rhs = ((P[6] and P[7]) or (P[8] and P[9]))
    
    return (not lhs) or rhs

alla_varianter = list(product([False, True], repeat=10))

dom_som_funka = [comb for comb in alla_varianter if uttryck(comb)]

print(len(dom_som_funka))
