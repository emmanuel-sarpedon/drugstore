from flask import Flask

# routes
from routes.drug import drugs

app = Flask(__name__)

app.register_blueprint(drugs)


if __name__ == '__main__':
    app.run(debug=True)
