from app import app, db
from models import Product
from datetime import date

# Sample tarot decks
sample_products = [
    {
        'name': 'Rider-Waite Tarot Deck',
        'price': 19.99,
        'description': 'The classic and most popular tarot deck. Perfect for beginners and experienced readers alike.',
        'dimensions': '4.7 x 2.8 in',
        'weight': 0.5,
        'isbn_13': '9780913866139',
        'isbn_10': '0913866130',
        'language': 'English',
        'author': 'Arthur Edward Waite',
        'publisher': 'U.S. Games Systems',
        'publish_date': date(1971, 9, 1),
        'publish_edition': None,
        'image': 'rider-waite.png',
        'qty': 50
    },
    {
        'name': 'The Wild Unknown Tarot Deck',
        'price': 29.95,
        'description': 'A stunning hand-drawn tarot deck featuring animals, nature, and symbolism.',
        'dimensions': '5.5 x 3.7 in',
        'weight': 0.8,
        'isbn_13': '9780062466594',
        'isbn_10': '0062466593',
        'language': 'English',
        'author': 'Kim Krans',
        'publisher': 'HarperOne',
        'publish_date': date(2016, 11, 8),
        'publish_edition': None,
        'image': 'wild-unknown.png',
        'qty': 35
    },
    {
        'name': 'Modern Witch Tarot Deck',
        'price': 24.99,
        'description': 'A diverse, modern take on the classic Rider-Waite deck with vibrant illustrations.',
        'dimensions': '4.8 x 3.0 in',
        'weight': 0.6,
        'isbn_13': '9781454938095',
        'isbn_10': '1454938099',
        'language': 'English',
        'author': 'Lisa Sterle',
        'publisher': 'Sterling Ethos',
        'publish_date': date(2019, 11, 12),
        'publish_edition': None,
        'image': 'modern-witch.png',
        'qty': 42
    }
]

with app.app_context():
    # Clear existing data (optional)
    db.drop_all()
    db.create_all()

    # Add sample products
    for product_data in sample_products:
        product = Product(**product_data)
        db.session.add(product)

    db.session.commit()
    print(f"Added {len(sample_products)} sample products to the database!")
