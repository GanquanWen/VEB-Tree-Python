import string
import random
g = open("input.txt","w")
co = 10000000
for i in range (co):
    g.write(str(random.randint(0, co))+'\n')
g.close()
print('file created')
