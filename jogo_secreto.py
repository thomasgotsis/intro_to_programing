import random
import numpy as np
#matriz numerica
lista =  ['X',1,2,0,0]
lista2 = [0,0,1,0,2]
lista3 = [0,1,2,0,5]
lista4 = [0,0,1,0,2]
lista5= [0,2,0,1,0]
lista6 = []

random.shuffle(lista)
random.shuffle(lista2)
random.shuffle(lista3)
random.shuffle(lista4)
random.shuffle(lista5)

lista6.clear()
lista6.append(lista)
lista6.append(lista2)
lista6.append(lista3)
lista6.append(lista4)
lista6.append(lista5)

matriz2 = np.matrix(lista6)
matriz2
#gerador de palavras
word_list = open('words.txt').read().split()
listap1 = []
myword1 = random.choice(words)
myword2 = random.choice(words)
myword3 = random.choice(words)
myword4 = random.choice(words)
myword5 = random.choice(words)
listap1.append(myword1)
listap1.append(myword2)
listap1.append(myword3)
listap1.append(myword4)
listap1.append(myword5)

word_list = open('words.txt').read().split()
listap2 = []
myword1 = random.choice(words)
myword2 = random.choice(words)
myword3 = random.choice(words)
myword4 = random.choice(words)
myword5 = random.choice(words)
listap2.append(myword1)
listap2.append(myword2)
listap2.append(myword3)
listap2.append(myword4)
listap2.append(myword5)

word_list = open('words.txt').read().split()
listap3 = []
myword1 = random.choice(words)
myword2 = random.choice(words)
myword3 = random.choice(words)
myword4 = random.choice(words)
myword5 = random.choice(words)
listap3.append(myword1)
listap3.append(myword2)
listap3.append(myword3)
listap3.append(myword4)
listap3.append(myword5)

word_list = open('words.txt').read().split()
listap4 = []
myword1 = random.choice(words)
myword2 = random.choice(words)
myword3 = random.choice(words)
myword4 = random.choice(words)
myword5 = random.choice(words)
listap4.append(myword1)
listap4.append(myword2)
listap4.append(myword3)
listap4.append(myword4)
listap4.append(myword5)

word_list = open('words.txt').read().split()
listap5 = []
myword1 = random.choice(words)
myword2 = random.choice(words)
myword3 = random.choice(words)
myword4 = random.choice(words)
myword5 = random.choice(words)
listap5.append(myword1)
listap5.append(myword2)
listap5.append(myword3)
listap5.append(myword4)
listap5.append(myword5)

listap6 = []
listap6.clear()
listap6.append(listap1)
listap6.append(listap2)
listap6.append(listap3)
listap6.append(listap4)
listap6.append(listap5)
listap6