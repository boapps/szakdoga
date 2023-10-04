from flask import jsonify, Blueprint

from auto_kmdb.Article import Article


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/articles', methods=["GET"])
def api_articles():
    return jsonify([a.dict() for a in Article.query.filter_by(is_classified=True).all()]), 200
