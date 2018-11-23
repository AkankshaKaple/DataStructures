dict1 = {'id': 1, 'success': True, 'name': 'Lary'}
dict2 = {'id': 2, 'success': False, 'name': 'Rabi'}
dict3 = {'id': 3, 'success': True, 'name': 'Alex'}

data = [dict1, dict2, dict3]


count = 0
# for i in range(len(data)) :
#     for key,value in dict.items():
#         if key == 'success' and value == True :
#             count+=1
#         print(value , " = " , count)

for obj in data:
    if 'name' in obj and dict1['name'] == 'Lary':
            count+=1
    print(count)



