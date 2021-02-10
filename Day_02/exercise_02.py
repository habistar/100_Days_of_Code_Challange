a = "111"
b = "222"
c = 333

print(a + b) #111222
#print(a + c) type error
print(a + str(c)) #111333
print(int(a) + c) #444