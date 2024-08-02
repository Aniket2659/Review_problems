def problem(lst):
    for i in range(len(lst)):
        if lst[i]%3==0 and lst[i]%5==0:
            print('FizzBuzz')
        elif lst[i]%3==0:
             print('Fizz')
        elif lst[i]%5==0:
            print('Buzz')
        else:
            print(str(lst[i]))
        

lst = [ 2 , 3 , 4 , 6 , 9 , 10 , 15 , 12 , 45 , 50 , 55]
problem(lst)