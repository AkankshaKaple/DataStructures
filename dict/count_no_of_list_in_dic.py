dict = {'1' : 'Aknaksha', '1' : [1,2,3,4,5,6] , '3' : 'Sampada', '4' : [7,6,5,4,32]}
count =0
for value in dict.values():
    if type(value) == list :
        count+=1
print(count)