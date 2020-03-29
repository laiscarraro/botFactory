import time
import random

class Digitador:
    
    def __init__(self, bot_name="Bot", mensagem_digitando="(digitando...)"):
        self.bot_name = bot_name
        self.mensagem_digitando = mensagem_digitando
        self.entrar()
    
    def enviar(self, msg, input_=False):
        mensagem = self.bot_name+": "+msg
        
        tamanho = len(msg)
        pensando = random.uniform(0.0, 0.5)
        tempo = (tamanho*0.05) + pensando
        
        time.sleep(random.uniform(0.3, 0.8))
        
        #tempo = 0
        
        self.digitando(tempo)
        if(len(mensagem) < len(self.mensagem_digitando)):
            mensagem += (" ")*(len(self.mensagem_digitando) - len(mensagem))
        if not input_:
            print("\r"+mensagem)
            time.sleep(random.uniform(0.3, 1.5))
        
        else:
            resp = input("\r"+mensagem+"\nVocê: ")
            return resp
            
        
    def digitando(self, tempo):
        timeout = time.time() + tempo
        print("\r"+self.mensagem_digitando, end = "", flush = True)
        while True:
            if time.time() > timeout:
                break
    
    def entrar(self):
        print("\n["+self.bot_name+" entrou na sala]\n")
        
    def sair(self):
        print("\n["+self.bot_name+" saiu da sala]\n")
        
