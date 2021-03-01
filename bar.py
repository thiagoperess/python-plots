import matplotlib.pyplot as plt

x = [1, 2, 4, 3]
y = [2, 3, 7, 3]

plt.title('Meu primeiro gráfico em Python')

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.bar(x, y)
plt.show()