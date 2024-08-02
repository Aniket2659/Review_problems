def uppercase(n,lst_names):

    count=0

    for i in range(len(lst_names)):
        if len(lst_names[i])>count:
            lst_names[i]=lst_names[i].replace(lst_names[i][i],lst_names[i][i].upper())
            count+=1
    return lst_names


n=int(input('enter number of names:'))
lst_names=[input('enter name:') for i in range(n)]
print(uppercase(n,lst_names))