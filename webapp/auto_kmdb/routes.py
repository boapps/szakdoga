from flask import jsonify, Blueprint, request

from auto_kmdb.Article import Article


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/articles', methods=["GET"])
def api_articles():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.filter_by(is_corruption=True).order_by(Article.date.desc()).paginate(page=page, per_page=10)
    return jsonify({'pages': pagination.pages, 'articles': [a.dict() for a in pagination]}), 200
