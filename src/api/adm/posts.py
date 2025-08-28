from flask import Blueprint, jsonify, request
from src.services import posts_service

posts_bp_api = Blueprint('adm_posts_api', __name__)

@posts_bp_api.route('/api/adm/posts')
def get():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
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
    
    return jsonify({
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total_items": pagination.total,
        "total_pages": pagination.pages,
        "has_next": pagination.has_next,
        "has_prev": pagination.has_prev,
        "items": [post.to_dict() for post in pagination.items],
        "filters": {
            "term": term,
            "date_from": date_from,
            "date_to": date_to
        }
    })