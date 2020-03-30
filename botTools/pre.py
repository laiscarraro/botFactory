!python -m spacy download pt
import spacy
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

def pre_processamento(texto):
  nlp = spacy.load('pt')
  texto2 = nlp(u''+texto)
  lemmatizado = [token.lemma_ for token in texto2]
  lixo = set(stopwords.words('portuguese'))
  return [token for token in lemmatizado if token not in lixo]
