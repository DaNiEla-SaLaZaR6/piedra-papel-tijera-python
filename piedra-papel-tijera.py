import random
x=0
contm=0
conty=0

num=random.randint(1,3)
can=int(input('cuantas veces quieres jugar PIEDRA,PAPEL O TIJERA:?'))
while x!=num:
    print('tener en cuenta\n 1=piedra \n2=papel \n3=tijera:')
    for i in range(can):
        x=int(input('piedra,papel o tijera?'))
        if x==num:
            print('empate')
        if x==1 and num==2:
            contm+=1
            print('gano contrincante')
        if x==1 and num==3:
            conty+=1
            print('Ganaste')
        if x==2 and num==3:
            contm+=1
            print('gano contrincante')
        if x==2 and num==1:
            conty+=1
            print('Ganaste')
        if x==3 and num==1:
            conty+=1
            print('Ganaste')
        if x==3 and num==2:
            contm+=1
            print('gano contincante')
print(f'puntos contrincante: {contm}')
print(f'puntos tuyos:{conty}')            
