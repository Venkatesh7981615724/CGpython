list1 = [10,23,45,78]
list2 = [1,2,3]
def addLists(list1,list2):
    try:
        res = []
        for i in range(4):
            res.append(list1[i] + list2[i])
    except IndexError:
        print("Invalid index, try again.")
    except TypeError:
        print("Invalid type, try again.")

addLists(list1,list2)