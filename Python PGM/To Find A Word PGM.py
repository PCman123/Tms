f = open('sample.txt', 'r')
data = f.read()
if 'hello' in data:
    print("hello is present")
    print(data.count('hello'))
else:
    print("hello not present")

f.close()
