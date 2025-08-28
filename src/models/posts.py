from src.db import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'sm_posts'

    code = db.Column(db.Text, primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    
    name = db.Column(db.Text, nullable=False)
    status = db.Column(db.Text, nullable=False, default='draft')
    briefing = db.Column(db.Text)
    copy = db.Column(db.Text)
    scheduled_at = db.Column(db.DateTime(timezone=True))

    medias = db.relationship('PostMedia', backref='post', lazy=True)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "copy": self.copy,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "status": self.status,
            "scheduled_at": self.scheduled_at.isoformat() if self.scheduled_at else None,
            "briefing": self.briefing,
            "medias": [media.to_dict() for media in self.medias] if self.medias else []
        }

    
    def __repr__(self):
        return f"<Post {self.code} - {self.name}>"

class PostMedia(db.Model):
    __tablename__ = 'sm_posts_media'

    code = db.Column(db.Text, primary_key=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    key = db.Column(db.Text, nullable=False)
    posts_code = db.Column(db.Text, db.ForeignKey('sm_posts.code'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    details = db.Column(db.Text)

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "key": self.key,
            "posts_code": self.posts_code,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "details": self.details
        }

    def __repr__(self):
        return f"<PostMedia {self.code} - {self.name}>"