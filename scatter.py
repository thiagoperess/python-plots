import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [3, 6, 1, 5, 7]

plt.title('Scatterplot')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()

plt.scatter(x, y, color= 'maroon')
plt.plot(x, y)
plt.show() 