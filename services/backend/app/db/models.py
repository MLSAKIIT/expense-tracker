from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from datetime import date

class users(SQLModel, table=True):
    user_id: str = Field(primary_key=True)
    email: str = Field(index=True, unique=True)
    username: str
    password: str

class UserCreate(BaseModel):
    email: str
    password: str
    username: str

class LoginRequest(BaseModel):
    email: str
    password: str

class receipts(SQLModel, table=True):
    receipt_id: str = Field(primary_key=True)
    category: str
    receipt_date: date
    vendor_name: str
    total_amount: float
    s3_url: str
    user_id: str = Field(index=True)