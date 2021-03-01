# boxplot

import matplotlib.pyplot as plt
import random

vector = []

for i in range(0, 10):
    aleatoryNumber = random.randint(0, 50)
    vector.append(aleatoryNumber)
plt.boxplot(vector)
plt.title('Bloxpot')
plt.show()
