a=int(input('Vvedite rezultat pervogo dnya'))
b=int(input('Vvedite ogidaemui rezultat'))
d=int(1)
while a<=b+b*0.1:
    print(f'{d}-den:{a}км')
    a=a+a*0.1
    d=d+1
print(f'Na {d-1}den sportsmen dostignet rezultata - ne menee{b}km')

#
