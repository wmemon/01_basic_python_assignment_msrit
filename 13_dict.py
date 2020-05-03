dict={}
def add(w,m):
    dict.update({w:m})
def search_word(w):
    try:
        print(dict[w])
    except :
        print("Not present")

def synonym(m):
    empty=True
    listOfItems = dict.items()
    for item in listOfItems:
        if item[1] == m:
            empty=False
            print(item)
    if empty==True:
        print("Empty")
def delete_entry(n):
    try :
        del dict[n]
    except :
        print("Empty")
def sort_words():
    try:
        for i in sorted(dict.keys()):
            print(i, end=" ")
    except :
        print("Empty")
print("Enter choice \n1:enter new entry\n 2:Search word\n 3:find synonym of meaning\n 4:delete entry\n 5:print sorted words\n anything else to exit\n")
while True:

    k=input()
    if k=='1':
        w=input("Enter word ")
        m=input("Enter meaning ")
        add(w,m)
    elif k=='2':
        w = input("Enter word ")
        search_word(w)
    elif k=='3':
        m = input("Enter meaning ")
        synonym(m)
    elif k=='4':
        w = input("Enter word to delete ")
        delete_entry(w)
    elif k=='5':
        print(dict)
    else:
        break
