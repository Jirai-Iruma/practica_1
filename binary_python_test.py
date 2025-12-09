from turtle import right


def main():
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    x:int =0
    y:int = len(list)-1
    z = int(input("Ponga un numero para buscar:\n"))
    
    found:bool = False
    while(x<=y):
        medio:int = (x+y)//2
        if (list[medio] == z ):
            found = True
            break;
        elif(list[medio] > z):
            y=medio-1
        else:
            x=medio+1

    if found:
        print(f"El numero esta en la posicion: ") 
        print(medio)
    else:
        print("no se encontro el numero")


def insert_method(lista:list):
    for every in range (len(lista)):
        valor = every
        while lista[valor-1] > lista[valor] and valor>0:
            lista[valor-1], lista[valor] = lista[valor], lista[valor-1]
            valor -= 1
            
    print(lista)

def bubble_sort(lista:list):
    x= True
    for every in range(len(lista)-1):
        x=True
        for also_evry in range(len(lista)-1):
            if lista[also_evry] >lista[also_evry+1]:
                x=False
                lista[also_evry+1], lista[also_evry] =  lista[also_evry], lista[also_evry+1]
        if x:
            break;

    print(lista)

def quick_sort(lista:list):
    
    if len(lista) <= 1:
        return lista
    else:
        medio= lista[0]
        listas_izquierda:list = []
        listas_centrales:list = []
        listas_derechas:list = []

        for every in lista:
            if every > medio:
                listas_derechas.append(every)

            elif every == medio:
                listas_centrales.append(every)

            else:
                listas_izquierda.append(every)

    final:list = quick_sort(listas_izquierda) + listas_centrales + quick_sort(listas_derechas)
    return final;

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left_part = merge_sort(lista[:mid])
    right_part = merge_sort(lista[mid:])

    lista_final = []
    i = 0
    k = 0
    while i < len(left_part) and k < len(right_part):
        if left_part[i] <= right_part[k]:
            lista_final.append(left_part[i])
            i += 1
        else:
            lista_final.append(right_part[k])
            k += 1

    while i < len(left_part):
        lista_final.append(left_part[i])
        i += 1

    while k < len(right_part):
        lista_final.append(right_part[k])
        k += 1

    return(lista_final)

def listas_s():
     list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
     list2 = [5, 4, 7, 3, 24, 5, 16, 7, 18, 9, 10, 11, 1, 3, 4, 15, 6, 17, 8, 19, 20]
     list3 = ["manzana", "naranja", "pera", "uva", "kiwi"]
     # print(quick_sort(list1))
     # print(quick_sort(list2))
     # print(quick_sort(list3))

     print(merge_sort(list2))
     print(merge_sort(list3))

if __name__ == "__main__":
    listas_s()
