grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
dict_ = dict(zip(students, grades))
len_0 = sum(dict_['Aaron'])/len(dict_['Aaron'])
dict_['Aaron'] = len_0
len_1 = sum(dict_['Bilbo'])/len(dict_['Bilbo'])
dict_['Bilbo'] = len_1
len_2 = sum(dict_['Johnny'])/len(dict_['Johnny'])
dict_['Johnny'] = len_2
len_3 = sum(dict_['Khendrik'])/len(dict_['Khendrik'])
dict_['Khendrik'] = len_3
len_4 = sum(dict_['Steve'])/len(dict_['Steve'])
dict_['Steve'] = len_4
print(dict_)
