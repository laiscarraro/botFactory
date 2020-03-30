import subprocess
import spacy
import nltk

try:
  from nltk.corpus import stopwords
except:
  nltk.download('stopwords')
  from nltk.corpus import stopwords

'''
Essa é a função mágica do pré-processamento de texto!!!
Nela, você pode escolher incluir:

1 - Tokenização por palavra: tokenizar significa separar; tokenizar por palavra, basicamente significa retornar um array com as palavras do texto.
2 - Remoção de stopwords: stopwords são aquelas palavras que só fazem volume no texto, e não têm muito significado. Tirar stopwords requer tokenização que, portanto, está implícita neste passo.
3 - Tagging de classes gramaticais: encontra a classe gramatical de cada palavra do texto, e requer tokenização (implícito).
4 - Lemmatização: basicamente passa os verbos para o infinitivo. Palavras como "mim" e "me" também contam como a mesma coisa. Requer tagging de classe gramatical e idealmente remoção de stopwords.
'''

def pre_processamento(texto, so_tokenizar=False, sem_stopwords=True, lemma=True):
  try:
    nlp = spacy.load('pt')
  except:
    subprocess.call('python -m spacy download pt', shell=True)
    nlp = spacy.load('pt')
  texto2 = nlp(u''+texto)
  resp = texto2
  if so_tokenizar:
    return texto2.text.split()
  if lemma:
    lemmatizado = [token.lemma_ for token in texto2]
    resp = lemmatizado
  if sem_stopwords:
    try:
      lixo = set(stopwords.words('portuguese'))
    except:
      
    no_stop = [token for token in resp if token not in lixo]
    resp = no_stop
  return resp
