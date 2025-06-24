from flask import Blueprint, request, jsonify
from .models import db, Episode, Guest, Appearance

api = Blueprint('api', __name__)


@api.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_list = [ep.to_dict() for ep in episodes]
    return jsonify(episodes_list), 200


@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)

    if episode:
        ep_dict = episode.to_dict()
        
        ep_dict['appearances'] = []
        for appearance in episode.appearances:
            ap_dict = appearance.to_dict()
            ep_dict['appearances'].append(ap_dict)
        return jsonify(ep_dict), 200
    else:
        return jsonify({"error": "Episode not found"}), 404


@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guest_list = [g.to_dict() for g in guests]
    return jsonify(guest_list), 200

@api.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    # Check for validation errors
    if not (1 <= rating <= 5):
        return jsonify({"errors": ["rating must be between 1 and 5"]}), 400

    # Create new appearance
    new_appearance = Appearance(
        rating=rating,
        episode_id=episode_id,
        guest_id=guest_id
    )

    # Add to DB
    db.session.add(new_appearance)
    db.session.commit()

    return jsonify(new_appearance.to_dict()), 201
