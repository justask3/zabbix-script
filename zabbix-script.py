from datetime import datetime
def return_number_until_loop(n):
    n = float(n)
    assert n.is_integer() == True, 'The input has to be an integer'
    assert n > 0, 'The input has to be positive'
    list_of_numbers = []
    while n > 1:
        list_of_numbers.append(n)
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2
    list_of_numbers.append(1)
    print(len(list_of_numbers))
    
    
number = input('Enter n: ') or (datetime.now().second * datetime.now().minute)
return_number_until_loop(number)