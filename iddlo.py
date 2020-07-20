#!/usr/local/bin/python
#Importation de  NLTK
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
text="""La Faculté des sciences-Rabat (FSR) a été créée en 1952. Elle fait partie de l'ensemble des facultés de l’Université Mohammed V de Rabat. Elle est la faculté où les étudiants bacheliers poursuivent leurs études supérieures dans le domaine scientifique (mathématiques, informatique, physique, science de la vie et de l'univers, chimie)."""
#Division en phrases
#tokenized_text=sent_tokenize(text)
#print(tokenized_text)
#Division en mots
tokenized_word=word_tokenize(text)
#print(tokenized_word)
# Nombre de Mots
fdist = FreqDist(tokenized_word)
#print(fdist)
# Mots les plus utilisés
#fdist.most_common(1)
#graphe des mots les plus utilisés
fdist.plot(30,cumulative=False)
plt.show()