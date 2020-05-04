result_list = []
while True:
    result = input("Please enter a string:- (0) to stop:- ")
    if result == '0':
        break
    elif result[0] in result[1:] :
        result_list.append(result)

print(result_list)
