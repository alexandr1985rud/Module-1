my_list = ['apple', 'banana', 'orange', 'peach', 'kiwi']
print('List:', my_list)
print('First element:', my_list[0])
print('Last element:', my_list[-1])
print('Sublist:', my_list[2:])
my_list[2] = 'grape'
print('Modified list:', my_list)

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print('Dictionary:', my_dict)
print('Translation:', my_dict['banana'])
my_dict['apple'] = 'СЛИВА'
print('Modified dictionary:', my_dict)
my_dict['peach'] = 'персик'
print('Modified dictionary:', my_dict)
del my_dict['orange']
print('Modified dictionary:', my_dict)
my_dict.update({'grape': 'виноград', 'kiwi': 'киви'})
print('Modified dictionary:', my_dict)