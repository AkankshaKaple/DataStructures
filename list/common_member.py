#9. Write a Python function that takes two lists and returns True
# if they have at least one common member.


class String:
    list1 = [1, 2, 3, 4]
    list2 = [1, "Akanksha", 6]
    def __init__(self):
        print("Constructor")

    def fun(list3,list4):

        for i in list3 :
            if i in list4 :
                # print("True")
                return True
            else:
                return False
        return
    fun(list1,list2)
        # result = self.fun()
        # print(result)