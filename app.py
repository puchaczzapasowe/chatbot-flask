from flask import Flask, request,jsonify
import json
from chat import get_response
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
socketIO = SocketIO(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysqlite:///C:/Users/jur-s/Desktop\project_ai\chatbot-flask\products.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/jur-s/Desktop/project_ai/chatbot-flask/products.db'

db = SQLAlchemy(app)
# Enable CORS


class Ocena(db.Model):
    __tablename__ = 'Oceny'
    nick = db.Column(db.String(255), primary_key=True)
    id_klienta = db.Column(db.Integer)
    ocena = db.Column(db.Integer)
    id_produktu = db.Column(db.Integer, db.ForeignKey('Produkty.id'))
    def to_dict(self):
        return {
            'ID': self.id,
            'Nick': self.nick,
            'ID_Klienta': self.id_klienta,
            'Ocena': self.ocena,
            'ID_Produktu': self.id_produktu
        }

class Produkt(db.Model):
    __tablename__ = 'Produkty'
    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(255))
    model = db.Column(db.String(255))
    zdjecie = db.Column(db.String(255))
    cena = db.Column(db.Float)
    opis = db.Column(db.Text)
    oceny = db.relationship('Ocena', backref='Produkty', lazy=True)
    
    def to_dict(self):
        return {
            'ID': self.id,
            'Marka': self.marka,
            'Model': self.model,
            'Zdjecie': self.zdjecie,
            'Cena': self.cena,
            'Opis': self.opis
        }

def theBestProduct():
    return  db.session.query(Produkt).join(Ocena).group_by(Produkt).order_by(func.avg(Ocena.ocena).desc()).first()


CORS(app, origins='http://localhost:5173')
@app.route('/')
def index():
 
    
    return json.dumps({"message":"dziala"})


@app.route('/bot', methods=['POST'])
def handleBotMessage():
    message = request.get_json()
    message["message"]
    chatResponse = get_response(message["message"])
    if chatResponse["tag"]=="theBestProduct":
        chatResponse["product"] = theBestProduct().to_dict()
    return chatResponse



@app.route('/api/products', methods=['GET'])
def getProducts():
    products = Produkt.query.all()
    output = []
    output = [product.to_dict() for product in products]
    return jsonify({'products': output})
@app.route('/api/product/theBest', methods=['GET'])
def getTheBestProduct():
    return jsonify({'products': theBestProduct().to_dict()})
