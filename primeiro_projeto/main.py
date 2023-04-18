from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.app_context().push()


db = SQLAlchemy(app)




from views import *

#Executando o site
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
