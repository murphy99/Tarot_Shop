from flask import Flask, render_template
from models import db, Product

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Route for homepage - display all products
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Route for individual product page
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

# Route for shopping cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
