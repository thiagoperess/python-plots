dataInput = open('dados/human.fasta').read()
dataExit = open('dados/bacteria.html','w')
score = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        score[i + j] = 0

dataInput = dataInput.replace('\n', '')

for k in range(len(dataInput)-1):
    score[dataInput[k] + dataInput[k + 1]] += 1

print(score)