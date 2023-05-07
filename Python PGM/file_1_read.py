
f = open('sample.txt', 'r')
data = f.read()
print(data)
f.close()



#read one by one line
f = open('sample.txt')
data = f.readline()
print(data)
#second line
data = f.readline()
print(data)
#third line
data = f.readline()
print(data)
#fouth line
data = f.readline()
print(data)
f.close()
