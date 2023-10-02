from math import sqrt

print('Det här är ett program som kan lösa andragrads ekvationer på formen x^2 + px + q = 0')
p = int(input('Vad är ditt värde på p? '))
q = int(input('Vad är ditt värde på q? '))


if(((p/2)**2)-q < 0):
    print('Inga reela rötter finns.')

else:
    rot1 = -(p/2) + sqrt(((p/2)**2)-q)
    rot2 = -(p/2) - sqrt(((p/2)**2)-q)

    print(f'Rötterna till ekvationen x^2 + {p}x + {q} är {rot1} och {rot2}')
