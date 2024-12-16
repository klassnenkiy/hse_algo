def get_hash(string):
    result = 0
    for char in string:
        result = (result + ord(char)) % 200
    return result

N = int(input())
string = 'aa'
for i in range(N):
    print(string)
    string += 'aa'
