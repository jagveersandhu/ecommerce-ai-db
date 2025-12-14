from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models

# -------------------- USERS --------------------
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, name: str, email: str, password_hash: str):
    user = models.User(name=name, email=email, password_hash=password_hash)
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        return None

def update_user(db: Session, user_id: int, **kwargs):
    user = get_user(db, user_id)
    if not user:
        return None
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user

# -------------------- CATEGORIES --------------------
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.category_id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, name: str, description: str = None):
    category = models.Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, **kwargs):
    category = get_category(db, category_id)
    if not category:
        return None
    for key, value in kwargs.items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if not category:
        return None
    db.delete(category)
    db.commit()
    return category

# -------------------- PRODUCTS --------------------
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, name: str, description: str, price: float, stock: int, category_id: int = None):
    product = models.Product(name=name, description=description, price=price, stock=stock, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db: Session, product_id: int, **kwargs):
    product = get_product(db, product_id)
    if not product:
        return None
    for key, value in kwargs.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product

# -------------------- ORDERS --------------------
def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, user_id: int, total_amount: float, status: str = "pending"):
    order = models.Order(user_id=user_id, total_amount=total_amount, status=status)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def update_order(db: Session, order_id: int, **kwargs):
    order = get_order(db, order_id)
    if not order:
        return None
    for key, value in kwargs.items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    if not order:
        return None
    db.delete(order)
    db.commit()
    return order

# -------------------- ORDER ITEMS --------------------
def get_order_item(db: Session, order_item_id: int):
    return db.query(models.OrderItem).filter(models.OrderItem.order_item_id == order_item_id).first()

def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()

def create_order_item(db: Session, order_id: int, product_id: int, quantity: int, price: float):
    item = models.OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_order_item(db: Session, order_item_id: int, **kwargs):
    item = get_order_item(db, order_item_id)
    if not item:
        return None
    for key, value in kwargs.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_order_item(db: Session, order_item_id: int):
    item = get_order_item(db, order_item_id)
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item

# -------------------- REVIEWS --------------------
def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.review_id == review_id).first()

def get_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Review).offset(skip).limit(limit).all()

def create_review(db: Session, product_id: int, user_id: int, rating: int, comment: str = None):
    review = models.Review(product_id=product_id, user_id=user_id, rating=rating, comment=comment)
    db.add(review)
    try:
        db.commit()
        db.refresh(review)
        return review
    except IntegrityError:
        db.rollback()
        return None

def update_review(db: Session, review_id: int, **kwargs):
    review = get_review(db, review_id)
    if not review:
        return None
    for key, value in kwargs.items():
        setattr(review, key, value)
    db.commit()
    db.refresh(review)
    return review

def delete_review(db: Session, review_id: int):
    review = get_review(db, review_id)
    if not review:
        return None
    db.delete(review)
    db.commit()
    return review
