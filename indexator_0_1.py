import pymorphy2
morph = pymorphy2.MorphAnalyzer()

spam = {'.', ',', ':', ';', '...', '?', '!', '(', ')', '-'}
tmp_1 = set()
tmp_2 = set()
index = {'from' : []}

library = []
with open('library.txt', 'r', encoding='utf8') as file:
    for line in file:
        library += [line.strip()]
#print(library)


def cleaner(mnoz, text):
    mnoz_2 = set()

    with open(text, 'r', encoding='utf8') as file:
        for line in file:
            line = line.strip().split()
            for i in range(len(line)):
                mnoz.update({line[i].lower()})

    for word in mnoz:
        if word[-1] == '.' or word[-1] == ',' or word[-1] == ':' or word[-1] == ';' or word[-1] == ')':
            word = word[0 : -1]
        mnoz_2.update({word})

    mnoz.clear()

    for word in mnoz_2:
        p = morph.parse(word)[0].normal_form
        mnoz.update({p})

    mnoz_2.clear()
    return mnoz


controller = 0
sum = 0
for name_1 in range(len(library)):
    tmp_1 = cleaner(tmp_1, library[name_1])

    for name in range(controller, len(library)):

        tmp_2 = cleaner(tmp_2, library[name])
        for k in tmp_1:

            if k in tmp_2:
                if k in index.keys():
                    if library[name] not in index[k]:
                        index[k] += [library[name]]
                else:
                    index.update({k : [library[name]]})
                    sum += 1
                    print('add', sum)
        tmp_2.clear()
        print('________________next file________________')
    tmp_1.clear()
    controller += 1

with open('index.txt', 'w', encoding='utf8') as file:
    file.write(str(index))

#print(index)
