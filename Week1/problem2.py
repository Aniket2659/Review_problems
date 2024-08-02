def move(arr):
    n=len(arr)
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(0)
    return arr
input=list(map(int,input('enter the value with quama seperated :').split(',')))
print(move(input))