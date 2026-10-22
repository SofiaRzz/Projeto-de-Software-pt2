from abc import ABC, abstractmethod
import secrets
from modelos.canal_notificacao import CanalNotificacao, CanalEmail, CanalPush

class CanalCreator(ABC):                      # Creator
    @abstractmethod
    def criar_canal(self) -> CanalNotificacao: ...   # Factory Method
    @abstractmethod
    def obter_destino(self) -> str: ...

    def criar_inscricao(self) -> tuple:       # usa o produto sem saber a classe concreta
        return (self.criar_canal(), self.obter_destino())

class EmailCreator(CanalCreator):             # ConcreteCreator
    def criar_canal(self):
        return CanalEmail()
    def obter_destino(self):
        email = input("Digite seu e-mail: ").strip()
        while not email or "@" not in email:
            email = input("E-mail inválido, precisa ter '@'. Digite de novo: ").strip()
        return email

class PushCreator(CanalCreator):              # ConcreteCreator
    def criar_canal(self):
        return CanalPush()
    def obter_destino(self):
        topico = f"painel-transporte-{secrets.token_hex(4)}"
        print(f"\nInstale o app 'ntfy' no celular e assine o tópico: {topico}")
        input("Quando terminar de assinar, aperte Enter... ")
        return topico