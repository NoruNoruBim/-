import pymorphy2
morph = pymorphy2.MorphAnalyzer()

spam = {'.', ',', ':', ';', '...', '?', '!', '(', ')', '-', 'в', 'на', 'или', 'и', 'но', 'с',
 'для', 'т.е.', 'то', 'т.п.', 'т.д.'}
library = ['data/1.txt', 'data/2.txt', 'data/3.txt']
tmp_1 = set()
tmp_2 = set()
index = {'from' : []}

with open('data/1.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip().split()
        for i in range(len(line)):
            tmp_1.update({line[i].lower()})
#print(tmp_1)

for word in tmp_1:
    if word[-1] == '.' or word[-1] == ',' or word[-1] == ':' or word[-1] == ';' or word[-1] == ')':
        word = word[0 : -1]
    #if word[0] == '(' or word[0] == '[':  shit again!
    #    word = word[1 : (len(word) - 1)]
    tmp_2.update({word})
#print(tmp_2)

tmp_1.clear()

for word in tmp_2:
    p = morph.parse(word)[0].normal_form
    tmp_1.update({p})
#print(tmp_1)

tmp_2.clear()

sum = 0
for k in tmp_1:
    for name in range(len(library)):
        with open(library[name], 'r', encoding='utf8') as file:
            for line in file:
                line = line.strip().split()
                for j in range(len(line)):
                    tmp_2.update({line[j].lower()})
        if k in tmp_2:
            if k in index.keys():
                index[k] += [library[name]]
            else:
                index.update({k : [library[name]]})
                sum += 1
                print('add', sum)
        tmp_2.clear()

print(index)
