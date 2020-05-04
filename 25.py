def create_lists(numlist):
    even_list = []
    odd_list = []
    if not isinstance ( numlist, list ):
        return "Please enter a list as an input"
    for num in numlist:
        if num % 2 == 0:
            even_list.append ( num )
        else:
            odd_list.append ( num )
    return {'even_list': even_list, 'odd_list': odd_list}.values()

print(create_lists([35,34,33,31,32,9,86,5]))
