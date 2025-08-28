from src.db import db
from datetime import datetime
import uuid

class User(db.Model):
    __tablename__ = 'users'
    
    code = db.Column(db.Text, primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        return {
            'code': self.code,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'active': self.active,
            'name': self.name,
            'email': self.email,
        }
    
    def __repr__(self):
        return f"<User {self.code} - {self.name}>"