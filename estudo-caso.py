# CRESCIMENTO DA POPULAÇÃO BRASILEIRA 1980-2016
# DATASUS
import matplotlib.pyplot as plt

data = open('populacao_brasileira.csv').readlines()

x = []
y = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(';')
        x.append(int(line[0]))
        y.append(int(line[1]))

plt.plot(x, y)
plt.title('CRESCIMENTO POPULAÇÃO BRASILEIRA 1980-2016')
plt.xlabel('Ano')
plt.ylabel('População x100.000.000')
plt.savefig('POPULAÇÃO BRASILEIRA.png')
plt.show()