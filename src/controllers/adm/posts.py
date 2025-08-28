from flask import Blueprint, render_template, request
from src.models.posts import Post
from sqlalchemy import or_
from datetime import datetime, time
from zoneinfo import ZoneInfo
from src.services import posts_service

posts_bp = Blueprint('adm_posts', __name__)

@posts_bp.route('/adm/posts')
def page():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=7, type=int)
    
    term = request.args.get('term', '').strip()
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    
    pagination = posts_service.posts_query(
        page=page,
        per_page=per_page,
        term=term,
        date_from=date_from,
        date_to=date_to
    )

    return render_template(
        'adm/posts.html',
        page=pagination.page,
        per_page=pagination.per_page,
        total_items=pagination.total,
        total_pages=pagination.pages,
        filters={
            "term": term,
            "date_from": date_from,
            "date_to": date_to
        }
    )
