from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

choco = ChatBot("ericBot")

#trainer = ChatterBotCorpusTrainer(choco)

#choco.storage.drop()

#trainer.train(
#    'chatterbot.corpus.custom'
#)

name = input("Seu nome: ")
print("ericBot: Oi meu bom!")
while True:
    request=input(name+': ')
    if request=='tchau' or request =='bye':
        print('ericBot: Tchau')
        break
    else:
        response = choco.get_response(request)
        print('ericBot:',response)
