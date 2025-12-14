from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ----------------- Users -----------------
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password_hash: str

class User(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ----------------- Categories -----------------
class CategoryBase(BaseModel):
    name: str
    description: Optional[str]

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True

# ----------------- Products -----------------
class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int
    category_id: Optional[int]

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# ----------------- Orders -----------------
class OrderBase(BaseModel):
    user_id: int
    total_amount: float
    status: Optional[str] = "pending"

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    order_id: int
    order_date: datetime

    class Config:
        orm_mode = True

# ----------------- Order Items -----------------
class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True

# ----------------- Reviews -----------------
class ReviewBase(BaseModel):
    product_id: int
    user_id: int
    rating: int
    comment: Optional[str]

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    review_id: int
    created_at: datetime

    class Config:
        orm_mode = True
