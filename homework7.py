my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'])
print('Not existing value:', my_dict.get('Vova'))
my_dict.update({'Sasha': 1985, 'Katya': 1987})
Egor = my_dict.pop('Egor')
print('Deleted value:', Egor)
print('Modified dictionary:', my_dict)

my_set = {3, 123, 'Computer', 3, 3, 'Computer', 3, 123}
print('Set:', my_set)
my_set.update({3.33, (1, 3, 5.5, 'Дом')})
my_set.remove(3)
print('Modified set:', my_set)