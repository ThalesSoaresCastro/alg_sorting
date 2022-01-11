
def mediana(arr, lt, rt):
    md = int((lt+rt-1)/2)
    #arr_median = [ arr[lt], arr[rt], arr[md] ]

    if arr[lt] <= arr[md] and arr[md] <= arr[rt]:
        return md
    if arr[rt] <= arr[md] and arr[md] <= arr[lt]:
        return md

    if arr[lt] <= arr[rt] and arr[rt] <= arr[md]:
        return rt
    if arr[md] <= arr[rt] and arr[rt] <= arr[lt]:
        return rt
    return lt

    #retirando laço e verificando apenas com comparações
    """
    maior = 0
    for i in range(1, len(arr_median)-1):
        if arr_median[i] > arr_median[maior]:
            arr_median[maior],arr_median[i] = arr_median[i], arr_median[maior]
            maior=i
    
    if arr_median[1] == arr[lt]: 
        return lt
    elif arr_median[1] == arr[md]:
        return md
    else:
        return rt
    """

def particao(arr,lt, rt):
    #melhorando a escolha do pivô utilizando a mediana
    md = mediana(arr, lt, rt)
    arr[lt],arr[md] = arr[md], arr[lt]

    pivot = arr[rt]
    menor= lt-1

    for i in range(lt, rt):
        if arr[i] <= pivot:
            menor+=1
            arr[menor], arr[i] = arr[i], arr[menor]

    arr[menor+1], arr[rt] = arr[rt], arr[menor+1]

    return menor+1



def quicksort(arr, lt, rt):
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr

    if lt < rt:
        q = particao(arr, lt, rt)
        quicksort(arr, lt, q-1)
        quicksort(arr, q+1, rt)

