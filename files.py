file = open('test.txt', 'a')

file.write("hello world\n")

file.close()
try:
    file = open('test.txt', 'r')
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("File not found")

#read and create csv files
data = [9,10]
# x = data[0]
# y = data[1]
x,y = data
print(x)
print(y)

def population():
    return "Nairobi",4000000

name, pp = population()
print(pp)
print(name)
