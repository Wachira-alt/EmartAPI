from app import create_app
from dotenv import load_dotenv
import os

# Load .env manually
load_dotenv()

app = create_app()




if __name__ == "__main__":
     # Set debug/reload mode via FLASK_ENV
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(debug=debug)

# pipenv install flask flask-sqlalchemy flask-migrate flask-bcrypt flask-cors python-dotenv pyjwt
# pipenv shell
