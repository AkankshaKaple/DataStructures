

num = int(input("Enter number of key value pairs you want to add in dictionary : "))
dict = {}
for i in range(1,num+1) :

        input_key = input("Give key to appendd onto the dictionary")
        #input_value = input("Give value to appendd onto the dictionary")
        value = i*10
        dict[input_key] = value
        print(dict)
        num-=1
# num = int(input("Enter number of key value pairs you want to add in dictionary : "))
# dict = {}
# while num > 0 :
#
#         input_key = input("Give key to appendd onto the dictionary")
#         input_value = input("Give value to appendd onto the dictionary")
#         if input_value == " " :
#             input_value = "Not asigned"
#         else :
#             dict[input_key] = input_value
#             print(dict)
#         num-=1