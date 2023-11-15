# TASK 1

def favorite_movie():
    name = input('What is your favorine movie?\n')
    return print(f'My favorite movie is named "{name}"')

favorite_movie()


# TASK 2

def make_country():
    country_dict = dict()
    while True:
        country = input('Enter country name:\n')
        capital = input('Enter country capital:\n')
        if country == 'stop' or capital == 'stop':
            break
        else:
            country_dict.update({country: capital})
            print(country_dict)
    print(country_dict)

make_country()


# TASK 3

def calculator(operator, *args):
    a = list(args)
    if operator == '+':
        b = sum(a)
    elif operator == '-':
        b = a[0] - sum(a[1:])
    elif operator == '*':
        b = 1
        for i in a:
            b = b * i

    return print(b)

calculator('-', 5, 5, -10, -20)
        
    
    
