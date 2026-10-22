import os
from dotenv import load_dotenv

class configuracao:
    _instancia = None

    # declara os atributos para o Pylance reconhecê-los
    aviationstack_key: str | None
    email_remetente: str | None
    email_senha_app: str | None
    ntfy_servidor: str
    gtfs_url: str | None

    def __new__(cls):
        if cls._instancia is None:
            load_dotenv()  # roda uma única vez em todo o sistema
            inst = super().__new__(cls)
            inst.aviationstack_key = os.getenv("AVIATIONSTACK_KEY")
            inst.email_remetente   = os.getenv("EMAIL_REMETENTE")
            inst.email_senha_app   = os.getenv("EMAIL_SENHA_APP")
            inst.ntfy_servidor     = os.getenv("NTFY_SERVIDOR", "https://ntfy.sh").rstrip("/")
            inst.gtfs_url          = os.getenv("GTFS_URL")
            cls._instancia = inst
        return cls._instancia