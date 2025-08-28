import jwt
import datetime
from flask import current_app
import os

def generate_token(payload, expires_in_minutes=30):
    try:        
        secret_key = os.getenv('JWT_SECRET_KEY', 'your-secret-key-here')

        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes)

        payload.update({"exp": expiration})

        token = jwt.encode(payload, secret_key, algorithm='HS256')
        
        return token        
    except Exception as e:
        raise Exception(f"Erro ao gerar token: {str(e)}")
    
    
def decode_token(token):
    try:
        secret_key = os.getenv('JWT_SECRET_KEY', 'your-secret-key-here')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])

        return payload        
    except jwt.ExpiredSignatureError:
        raise Exception("Token expirado")
    except jwt.InvalidTokenError:
        raise Exception("Token inválido")