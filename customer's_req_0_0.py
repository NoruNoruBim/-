request = input()
while request != 'done':
    with open("url's.txt", 'a') as file:
        file.write('\n' + 'https://en.wikipedia.org/wiki/' + request)
    request = input()
    
