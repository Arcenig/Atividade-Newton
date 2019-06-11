def media (nota1, nota2):
    media = (nota1 + nota2)/2
    return media

# Exercício 02
arq = open('series.csv', 'r')
arq2 = open('series_novas.csv', 'r')

texto = arq.readlines()

# Lê cada elemento da lista
print('Séries')
for i in texto:
    print(i, end='')

texto2 = arq2.readlines()

print('Séries novas')
for i in texto2:
    print(i, end='')

print("")

nota1 = texto[5]
nota2 = texto[6]

media()

arq.close()


# Exercício 04
n = str(input('Insira o nome da série que deseja ver a média'))


diciomedia = {'The Big Bang Theory': media,
              'Friends': media,
              'Breaking Bad': media,
              'Black Mirror': media}

print(diciomedia[n])


# Exercício 05
arq3 = open('melhores.csv', 'w')

if media >= 7.5:
    arq.write('n')

arq.close()
