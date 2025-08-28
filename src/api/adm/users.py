from flask import Blueprint, jsonify, request
from src.models.users import User
from sqlalchemy import or_
from datetime import datetime, time
from zoneinfo import ZoneInfo
from src.services import posts_service
from src.libs import bcrypt_lib
from src.db import db

users_bp_api = Blueprint('adm_users_api', __name__)

@users_bp_api.route('/api/adm/users/<string:code>', methods=['GET'])
def get(code):
    try:
        user = User.query.filter_by(code=code).first()
        
        if not user:
            return jsonify([{ 'message': 'Usuário não encontrado' }]), 404
        
        return jsonify(user.to_dict())
        
    except Exception as e:
        return jsonify([{ 'message': f'Erro ao buscar usuário. Motivo: {e}' }]), 500


@users_bp_api.route('/api/adm/users', methods=['GET'])
def all():
    list = User.query.all()
    
    return jsonify([user.to_dict() for user in list])
    

@users_bp_api.route('/api/adm/users', methods=['POST'])
def create():
    try:
        body = request.get_json()
        
        if not body:
            return jsonify([{ 'message': 'Dados não fornecidos' }]), 400
        
        name = body.get('name')
        email = body.get('email')
        password = body.get('password')
        
        if not name or not email or not password:
            return jsonify([{ 'message': 'Nome, email e password são obrigatórios' }]), 400
        
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return jsonify([{ 'message': 'Email já cadastrado' }]), 409
        
        hashed_password = bcrypt_lib.hash_password(password)
        
        new_user = User(
            name=name,
            email=email,
            password=hashed_password,
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify(new_user.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()

        return jsonify([{ 'message': f'Erro na tentativa de salvar. Motivo {e}' }]), 500


@users_bp_api.route('/api/adm/users/<string:code>', methods=['DELETE'])
def delete(code):
    try:
        user = User.query.filter_by(code=code).first()
        
        if not user:
            return jsonify([{ 'message': 'Usuário não encontrado' }]), 404
        
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({ 'message': 'Usuário deletado com sucesso' }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify([{ 'message': f'Erro na tentativa de deletar. Motivo: {e}' }]), 500

