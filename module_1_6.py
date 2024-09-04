# 1st task
my_dict = {'Алексей': 2003, 'Олег': 1997, 'Роман': 1984}
print('Dict:',my_dict)
print('Existing value:',my_dict['Роман'])
print('Non existing value:',my_dict.get('Eвгений'))
my_dict['Николай'] = 2024
my_dict['Вероника'] = 1996
print('Deleted value:',my_dict.pop('Олег'))
print('Modified dictionary:',my_dict)

# 2nd task
my_set = {True, False, 1, 2, 3, 4, 6, 7, 7, 5, 4, 4, 3, 2, 1, 'q', 'w', 'r', 'r', 'e', 'r', 'g'}
print('Set:',my_set)
my_set.add(3.14)
my_set.add('pi')
my_set.discard(True)
print('Modified set:',my_set)