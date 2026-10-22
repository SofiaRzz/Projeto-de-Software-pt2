import requests
from modelos.configuracao import configuracao

class AviationStack:
    URL = "http://api.aviationstack.com/v1/flights"
    
    def __init__(self, api_key: str | None = None):
        self.__api_key = api_key or configuracao().aviationstack_key
        if not self.__api_key:
            raise KeyError("Variável 'AVIATIONSTACK_KEY' não encontrada. Defina-a no arquivo .env.")

    def buscar_voo(self, iata_code: str) -> dict:
        paramd = {"access_key": self.__api_key, "flight_iata": iata_code}
        try:#tratamento de erro
            resposta = requests.get(self.URL, params=paramd, timeout=10)
            resposta.raise_for_status()
            dados = resposta.json()
        except requests.RequestException as erro:
            raise requests.RequestException(f"Resposta de AviationStack é um JSON inválido: {erro}") from erro
    
        try:
            if not dados["data"]:
                raise ValueError(f"Voo {iata_code} não encontrado")
            return dados["data"][0]
        except KeyError as erro:
            raise KeyError(f"Resposta da AviationStack em formato inesperado: {erro}") from erro