from flask import Flask, jsonify
from config import Config
from models import db, Admin
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ✅ Define login_manager FIRST
login_manager = LoginManager()
login_manager.init_app(app)

# ❗ Optional: you can remove this for API-based apps
# login_manager.login_view = "auth.login"

# ✅ NOW add unauthorized handler
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({
        "status": "error",
        "message": "Unauthorized"
    }), 401


# Import routes
from routes.auth_routes import auth_bp
from routes.opportunity_routes import opportunity_bp

app.register_blueprint(auth_bp)
app.register_blueprint(opportunity_bp)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)