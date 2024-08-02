def sort(lst_names):  
    dict_list={}

    for i in range(len(lst_names)):
        dict_list[lst_names[i]]=len(lst_names[i])
    print(dict_list)

    list_dict=list(dict_list.items())
    n=len(list_dict)

    for i in range(n):
        for j in range(n-i-1):
            if list_dict[j][1]>list_dict[j+1][1]:
                list_dict[j],list_dict[j+1]=list_dict[j+1],list_dict[j]
    print(list_dict)

    sorted_list=[]
    for i in range(len(list_dict)):
        sorted_list.append(list_dict[i][0])
    print(sorted_list)

lst_names=['aniket','sahil','pratiksha','prashant','hari']
sort(lst_names)
