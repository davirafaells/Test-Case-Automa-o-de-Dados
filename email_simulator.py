import logging
import json
import requests
from config import SEND_EMAIL_ENDPOINT

def simular_envio_email(caminho_arquivo):
    try:
        
        payload = {"filename": caminho_arquivo}
        response = requests.post(SEND_EMAIL_ENDPOINT, json=payload)
        print(f"Simulação de envio para {SEND_EMAIL_ENDPOINT} (não será realmente enviado)")
        return response.status_code == 200
    except Exception as e:
        logging.error(f"Erro ao simular envio de email: {e}")
        return False
