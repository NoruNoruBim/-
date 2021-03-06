import pymorphy2
morph = pymorphy2.MorphAnalyzer()

request = ''
word = ''
arr = []
while word != 'done':
    request = input().split()
    with open("url's.txt", 'a') as online:
        for word in request:
            if word != 'done':
                arr += [word]
                online.write('\n' + 'https://ru.wikipedia.org/wiki/' + word)


index = dict()
s = ''
key = ''
value = ''
label = 1
with open('index.txt', 'r', encoding='utf8') as ind:
    for line in ind:
        s += str(line)


i = 0
l_1 = 1
while i != len(s):
    l_1 = 1
    if i >= len(s) - 3:
        break
    key = ''
    while s[i] != "'":
        i += 1
    if s[i] == "'" and s[i + 1] == "'":
        while 1:
            i += 1
            if s[i] == "[":
                i += 1
            if s[i] == "]":
                i += 3
                break 
    while 1:
        i += 1
        if s[i] == "'":
            break
        key += s[i]
    index.update({key : []})

    while s[i] != "[":
        i += 1
    while s[i] != "'":
        i += 1

    while 1:
        value = ''
        while 1:
            i += 1
            if s[i] == "'":
                if s[i + 1] == "]":
                    i += 1
                    index[key] += [value]
                    l_1 = 0
                    break
                elif s[i + 1] == ",":
                    i += 3
                    index[key] += [value]
                    break
                elif s[i + 1] == "}":
                    l_1 = 0
                    break
            value += s[i]
        if l_1 == 0:
            break


set_1 = set()
set_2 = set()
for i in index.values():
    for j in i:
        set_1.update({j})

for word in arr:
    p = morph.parse(word.lower())[0].normal_form
    if p in index.keys():
        #print(word, index[p])
        for i in index[p]:
            set_2.update({i})
        set_1 = set_1.intersection(set_2)
    #else:
        #print('None')

print('Your phrase is in these files:\n', set_1)
