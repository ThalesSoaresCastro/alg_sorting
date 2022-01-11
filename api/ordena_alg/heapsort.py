def rearranja_heap(arr, itt, size_arr):

    lt,rt = 2*itt+1, 2*itt+2
    maior = 0
    
    maior = lt if( (lt < size_arr) and (arr[lt] > arr[itt]) ) else itt

    if (rt < size_arr) and (arr[rt]>arr[maior]):
        maior=rt
    if(maior!=itt):
        arr[itt], arr[maior] = arr[maior], arr[itt]
        
        rearranja_heap(arr, maior,size_arr)
        
def contruir_heap(arr):
    for i in range(int((len(arr)/2)-1), -1, -1): #-1, -1):
        rearranja_heap(arr, i, len(arr))

def heapsort(arr):
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr

    contruir_heap(arr)

    #size_hp = len(arr)
    for i in range(int(len(arr)-1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        #size_hp-=1 #ou size_hp -1  = i ?
        #rearranja_heap(arr, 0, size_hp)
        rearranja_heap(arr, 0, i)
