from flask import Blueprint, jsonify, request
from src.models.users import User
from sqlalchemy import or_
from datetime import datetime, time
from zoneinfo import ZoneInfo
from src.services import posts_service
from src.libs import bcrypt_lib
from src.db import db
from src.libs import jwt_lib

login_bp_api = Blueprint('login_api', __name__)

@login_bp_api.route('/api/login', methods=['POST'])
def login():
    try:
        body = request.get_json()
        
        if not body:
            return jsonify([{ 'message': 'Dados não fornecidos' }]), 400
        
        email = body.get('email')
        password = body.get('password')
        
        if not email or not password:
            return jsonify([{ 'message': 'Email e password são obrigatórios' }]), 400
        
        user = User.query.filter_by(email=email).first()

        if user is None:
            return jsonify([{ 'message': 'Usuário e/ou senha inválidos' }]), 400
        
        is_ok = bcrypt_lib.verify_password(password, user.password)
        
        if not is_ok:
            return jsonify([{ 'message': 'Usuário e/ou senha inválidos' }]), 400

        token = jwt_lib.generate_token({"code": user.code})      
        
        return jsonify({**user.to_dict(), "token": token}), 200       
    except Exception as e:
        db.session.rollback()

        return jsonify([{ 'message': f'Erro na tentativa de login. Motivo {e}' }]), 500
