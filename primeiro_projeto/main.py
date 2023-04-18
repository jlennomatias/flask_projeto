from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.app_context().push()


db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views_ativos import *
from views_user import *

#Executando o site
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
