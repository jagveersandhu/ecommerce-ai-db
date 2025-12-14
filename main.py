from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud, database, models, schemas
from sql_agent import run_query

app = FastAPI(title="E-commerce API", version="1.0")

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================== AI QUERY ====================

class AIQuery(BaseModel):
    question: str

@app.post("/ai/query")
def ai_query(payload: AIQuery):
    """
    Natural language → SQL → Answer
    """
    answer = run_query(payload.question)
    return {"answer": answer}

# -------------------- Root --------------------
@app.get("/")
def root():
    return {"message": "E-commerce API is running!"}

# -------------------- Users --------------------
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    created = crud.create_user(db, **user.dict())
    if not created:
        raise HTTPException(status_code=400, detail="User already exists or error occurred")
    return created

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, **user.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted

# -------------------- Categories --------------------
@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.get("/categories", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, **category.dict())

@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    updated = crud.update_category(db, category_id, **category.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated

@app.delete("/categories/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted

# -------------------- Products --------------------
@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/products", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, **product.dict())

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, **product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@app.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted

# -------------------- Orders --------------------
@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/orders", response_model=list[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

@app.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, **order.dict())

@app.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    updated = crud.update_order(db, order_id, **order.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@app.delete("/orders/{order_id}", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_order(db, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted

# -------------------- Order Items --------------------
@app.get("/order_items/{order_item_id}", response_model=schemas.OrderItem)
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    item = crud.get_order_item(db, order_item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item

@app.get("/order_items", response_model=list[schemas.OrderItem])
def read_order_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_order_items(db, skip=skip, limit=limit)

@app.post("/order_items", response_model=schemas.OrderItem)
def create_order_item(item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_item(db, **item.dict())

@app.put("/order_items/{order_item_id}", response_model=schemas.OrderItem)
def update_order_item(order_item_id: int, item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    updated = crud.update_order_item(db, order_item_id, **item.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Order item not found")
    return updated

@app.delete("/order_items/{order_item_id}", response_model=schemas.OrderItem)
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_order_item(db, order_item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order item not found")
    return deleted

# -------------------- Reviews --------------------
@app.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = crud.get_review(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@app.get("/reviews", response_model=list[schemas.Review])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_reviews(db, skip=skip, limit=limit)

@app.post("/reviews", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    created = crud.create_review(db, **review.dict())
    if not created:
        raise HTTPException(status_code=400, detail="Review already exists or error occurred")
    return created

@app.put("/reviews/{review_id}", response_model=schemas.Review)
def update_review(review_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    updated = crud.update_review(db, review_id, **review.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Review not found")
    return updated

@app.delete("/reviews/{review_id}", response_model=schemas.Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_review(db, review_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Review not found")
    return deleted

