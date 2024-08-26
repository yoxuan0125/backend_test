from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yc0125@db:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category,
            'size': self.size,
            'unit_price': str(self.unit_price),
            'inventory': self.inventory,
            'color': self.color
        }

@app.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Products.query.get_or_404(id)
    return jsonify(product.to_dict())

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Products(
        name=data['name'],
        code=data['code'],
        category=data['category'],
        size=data['size'],
        unit_price=data['unit_price'],
        inventory=data['inventory'],
        color=data['color']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Products.query.get_or_404(id)
    data = request.json
    product.name = data['name']
    product.code = data['code']
    product.category = data['category']
    product.size = data['size']
    product.unit_price = data['unit_price']
    product.inventory = data['inventory']
    product.color = data['color']
    db.session.commit()
    return jsonify(product.to_dict())

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)