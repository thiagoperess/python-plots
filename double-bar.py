import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
x2 = [2, 9, 7, 4, 7]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 5, 8, 4, 9]

plt.title('Meu primeiro gráfico em Python')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

plt.bar(x1, y1, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')
plt.show()