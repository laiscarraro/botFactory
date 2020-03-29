from digitar import Digitador
import re
import random

eric = Digitador(bot_name = "Eric")

class EricBot:
    
    resp_negativas = ("n", "nao", "não", "nah", "nope", "meh")
    resp_sair = ("tchau", "embora", "sai", "vai", "vaza")
    assuntos = ("do PET", "de mim", "da Each", "do coronga", "de smash", "de game design", "do Felipe", "do André", "do Fukuda", "da Laís", "da USP", "do Grace", "do BXCOMP", "do Fala Coruja")
    
    def __init__(self):
        self.resp_dicio = {
            'smash': [r'.*joga.*smash.*'],
            'switch': [r'.*switch.*'],
            'desculpa': [r'.*desculp(a|e).*'],
            'epetusp': [r'.* epetusp .*'],
            'concordo': [r'(.*) (é|eh) (.*)((, )?(ne|né|(nao|não|n)(eh|é)))?(\?)?']
        }
    
    def inicio(self):
        eric.enviar("Oi, meu bom!")
        self.nome = eric.enviar("Qual o seu nome?", True)
        eric.enviar("Legal!")
        eric.enviar("Oi, "+self.nome+"!")
        
        conversa = eric.enviar("Quer conversar comigo?", True).lower()
        
        for i in self.resp_negativas:
            if i in conversa:
                eric.enviar("Ah... tudo bem")
                eric.enviar("Se cuida")
                eric.enviar("Flw, "+self.nome+"!")
                eric.sair()
                return
        
        eric.enviar("Yaay!")
        sentimento = eric.enviar(self.nome+", como vc tá se sentindo?", True)
        self.conversar(sentimento)
        
    def conversar(self, resp):
        while not self.sair(resp):
            resp = self.dar_match(resp)
    
    def sair(self, resp):
        for i in self.resp_sair:
            if i in resp.lower():
                eric.enviar("Eita, vou ter que sair")
                eric.enviar("Se cuida, "+self.nome)
                eric.sair()
                return True
        return False
    
    def dar_match(self, resp):
        for chave, valor in self.resp_dicio.items():
            for regex in valor:
                deu_match = re.match(regex, resp.lower())
                if deu_match:
                    if chave == 'smash':
                        return self.bo_jogar_smash()
                    elif chave == 'switch':
                        return self.eu_trouxe_o_switch()
                    elif chave == 'desculpa':
                        return self.que_isso_cara()
                    elif chave == 'epetusp':
                        return self.nao_fala_de_epetusp()
                    elif chave == 'concordo':
                        return self.concordo(deu_match.groups()[0], deu_match.groups()[2])
        return eric.enviar("Vamos falar de outra coisa. O q vc acha " + self.assuntos[random.randint(0, len(self.assuntos))]+"?", True)
    
    def bo_jogar_smash(self):
        eric.enviar("Ow, "+self.nome)
        eric.enviar("Tava pensando")
        return eric.enviar("Bo jogar smash?", True)
    
    def eu_trouxe_o_switch(self):
        eric.enviar("Ow")
        eric.enviar("Falando em switch")
        return eric.enviar("Bo jogar smash?", True)
    
    def que_isso_cara(self):
        eric.enviar("Po, "+self.nome)
        eric.enviar("Que isso, cara")
        return eric.enviar("Tem problema nao, ta de boas", True)
        
    def nao_fala_de_epetusp(self):
        eric.enviar("Ai ai, "+self.nome+"...")
        eric.enviar("N fala de epetusp nao")
        return eric.enviar("Vamos falar de outra coisa, vai", True)
        
    def concordo(self, sujeito=None, predicado=None):
        eric.enviar("Nossa, concordo")
        return eric.enviar(sujeito+" é "+predicado+" mesmo", True)
