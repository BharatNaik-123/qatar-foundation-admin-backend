from flask import Blueprint, request, jsonify
from models import db, Opportunity
from flask_login import login_required, current_user

opportunity_bp = Blueprint('opportunity', __name__, url_prefix='/api/opportunities')


# GET ALL
@opportunity_bp.route('', methods=['GET'])
@login_required
def get_opportunities():
    opportunities = Opportunity.query.filter_by(admin_id=current_user.id).all()

    data = []

    for opp in opportunities:
        data.append({
            "id": opp.id,
            "title": opp.title,
            "category": opp.category,
            "duration": opp.duration
        })

    return jsonify({
        "status": "success",
        "data": data
    }), 200


# CREATE
@opportunity_bp.route('', methods=['POST'])
@login_required
def create_opportunity():
    data = request.get_json()

    if not data.get('title') or not data.get('category'):
        return jsonify({"status": "error", "message": "Missing required fields"}), 400

    new_op = Opportunity(
        title=data.get('title'),
        duration=data.get('duration'),
        start_date=data.get('start_date'),
        description=data.get('description'),
        skills=data.get('skills'),
        category=data.get('category'),
        future_opportunities=data.get('future_opportunities', False),
        max_applicants=data.get('max_applicants'),
        admin_id=current_user.id
    )

    db.session.add(new_op)
    db.session.commit()

    return jsonify({"status": "success", "message": "Created"}), 201


# GET ONE
@opportunity_bp.route('/<int:id>', methods=['GET'])
@login_required
def get_opportunity(id):
    op = Opportunity.query.get_or_404(id)

    if op.admin_id != current_user.id:
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    return jsonify({
        "status": "success",
        "data": {
            "id": op.id,
            "title": op.title,
            "description": op.description
        }
    })


# UPDATE
@opportunity_bp.route('/<int:id>', methods=['PUT'])
@login_required
def update_opportunity(id):
    op = Opportunity.query.get_or_404(id)

    if op.admin_id != current_user.id:
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    data = request.get_json()

    op.title = data.get('title', op.title)
    op.description = data.get('description', op.description)
    op.category = data.get('category', op.category)

    db.session.commit()

    return jsonify({"status": "success", "message": "Updated"})


# DELETE
@opportunity_bp.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_opportunity(id):
    op = Opportunity.query.get_or_404(id)

    if op.admin_id != current_user.id:
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    db.session.delete(op)
    db.session.commit()

    return jsonify({"status": "success", "message": "Deleted"})