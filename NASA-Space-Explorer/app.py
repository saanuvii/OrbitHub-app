from flask import Flask, render_template
from config import Config
from flask_caching import Cache

cache = Cache()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    cache.init_app(app)


    # Register blueprints
    from routes.main import main_bp
    from routes.apod import apod_bp
    from routes.asteroids import asteroids_bp
    from routes.epic import epic_bp
    from routes.exoplanets import exoplanets_bp
    from routes.search import search_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(apod_bp, url_prefix='/apod')
    app.register_blueprint(asteroids_bp, url_prefix='/asteroids')
    app.register_blueprint(epic_bp, url_prefix='/epic')
    app.register_blueprint(exoplanets_bp, url_prefix='/exoplanets')
    app.register_blueprint(search_bp, url_prefix='/search')

    # Global Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    return app

# Initialize app for Gunicorn
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
