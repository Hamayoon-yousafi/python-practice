list_items = []
item = None
while item != "Q" or item != "":
    item = input("enter your item or to quit, enter Q ") 
    list_items.append(item)
    if item == 'Q' or item == "q":
        print("Ok! that's it!")
        print(list_items)
        break



    