V = ['Vectors of n coordinates', 'Arrays of m rows and n columns', 'Grade n polynomials', 'Locally integrable functions']
S = ['Standard basis', 'Trigonometric polynomials', 'Custom basis']
v = ['Step', 'Ramp', ]


# Definición de V

print('Define V:\n') 

for V_i in range(0,len(V),1):
    print(f'({V_i+1}) {V[V_i]}')

V_i = len(V)

while V_i >= len(V) or V_i < 0:
    V_i = int(input('Select vector space: ')) - 1

print(f'V = {V[V_i]}\n')


# Definición de S

print('Define S:\n')

for S_i in range(0,len(S),1):
    print(f'({S_i+1}) {S[S_i]}')

S_i = len(S)

while S_i >= len(S) or S_i < 0:
    S_i = int(input('Select subspace: ')) - 1

print(f'S = {S[S_i]}\n')
