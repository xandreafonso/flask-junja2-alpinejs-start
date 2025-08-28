from src.models.posts import Post
from sqlalchemy import or_
from datetime import datetime, time
from zoneinfo import ZoneInfo

def posts_query(page=1, per_page=10, term='', date_from=None, date_to=None):    
    query = Post.query
    
    if term:
        query = query.filter(
            or_(
                Post.name.ilike(f'%{term}%'),
                Post.status.ilike(f'{term}%'),
            )
        )
    
    tz = ZoneInfo('America/Sao_Paulo')

    if date_from:
        date_from_obj = datetime.strptime(date_from, '%Y-%m-%d').date()
        date_from_tz = datetime.combine(date_from_obj, time.min, tz)
        date_from_utc = date_from_tz.utctimetuple()
        date_from_utc = datetime(*date_from_utc[:6])
        query = query.filter(Post.created_at >= date_from_utc)
    
    if date_to:
        date_to_obj = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to_tz = datetime.combine(date_to_obj, time.max, tz)
        date_to_utc = date_to_tz.utctimetuple()
        date_to_utc = datetime(*date_to_utc[:6])
        query = query.filter(Post.created_at <= date_to_utc)
    
    pagination = query.order_by(Post.created_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return pagination