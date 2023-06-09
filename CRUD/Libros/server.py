from app import app
from app.controllers import authors
from app.controllers import books


if __name__ == "__main__":
    app.run(debug=True)
