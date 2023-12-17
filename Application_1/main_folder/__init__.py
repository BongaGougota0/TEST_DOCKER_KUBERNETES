from flask import Flask

app = Flask(__name__)

def create_app():
    # from general.main_folder.home import home
    from main_folder.general.routes import home
    app.register_blueprint(home)
    return app