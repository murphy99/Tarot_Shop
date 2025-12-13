from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from models import db, Product

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

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

# Route to add item to cart
@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    # Initialize cart in session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []

    # Check if product already in cart
    cart = session['cart']
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] += 1
            session.modified = True
            return jsonify({'success': True, 'cart_count': sum(item['quantity'] for item in cart)})

    # Add new item to cart
    cart.append({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'author': product.author,
        'quantity': 1
    })
    session.modified = True

    return jsonify({'success': True, 'cart_count': sum(item['quantity'] for item in cart)})

# Route for shopping cart
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

# Route to remove item from cart
@app.route('/remove-from-cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        cart = session['cart']
        session['cart'] = [item for item in cart if item['id'] != product_id]
        session.modified = True
    return redirect(url_for('cart'))

# Route to update quantity
@app.route('/update-cart/<int:product_id>/<action>')
def update_cart(product_id, action):
    if 'cart' in session:
        cart = session['cart']
        for item in cart:
            if item['id'] == product_id:
                if action == 'increase':
                    item['quantity'] += 1
                elif action == 'decrease' and item['quantity'] > 1:
                    item['quantity'] -= 1
                break
        session.modified = True
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
