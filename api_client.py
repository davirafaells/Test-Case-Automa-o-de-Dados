import requests
import logging
from config import USERS_ENDPOINT, POSTS_ENDPOINT

def get_users():
    try:
        response = requests.get(USERS_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao obter usuários: {e}")
        return []

def get_posts_by_user(user_id):
    try:
        response = requests.get(POSTS_ENDPOINT, params={"userId": user_id})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao obter posts do usuário {user_id}: {e}")
        return []
