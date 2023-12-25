# dirperseur et dimentineur et timer ideal de planete du systeme solaire

i=2
n=0
q=1.2
result = []
index = 7
nombre_max = int(input("Entrez le nombre maximun a atteindre: "))
marge_max = int(input("Entrez la marge de manoeuvre: "))

while n<8  and i < nombre_max:

    i = i + i * q

    result.append(i)

    n+=1
    if i + marge_max >= nombre_max:
        if n>7:
            last_result = result[-8:]
            print(last_result)
            print("reussi")
            break
        else:
            i = 2
            q-=0.05
            n=0
    elif i + marge_max < nombre_max:
        if n>7:
            i= 2
            q+=0.1
            n=0
        else:
            continue
        