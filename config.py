import os

basedir = os.path.abspath(os.path.dirname(__file__))

# create environment variables that Flask will need access to later on
class Config():
    """
    Set config variables for the Flask App here.
    Using Environment variables where available, otherwise
    will create the config variable(s) if not already done
    """

    # SECRET_KEY allows use of forms inside of flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess...'
    
    # Alchemy is ORM (object relational manager) that allows us to go between Python and Flask
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages from the database



