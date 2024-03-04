from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional
from fastapi.testclient import TestClient

# Initialize FastAPI
app = FastAPI()

# SQLite database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define Pydantic models for request and response data validation
class Book(BaseModel):
    title: str
    author: str
    publication_year: int

class Review(BaseModel):
    text_review: str
    rating: int

# Define SQLAlchemy models for database tables
class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    publication_year = Column(Integer)

class ReviewDB(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text_review = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("BookDB", back_populates="reviews")

# Create database tables
Base.metadata.create_all(bind=engine)

# Endpoints for CRUD operations
@app.post("/books/", response_model=Book)
def create_book(book: Book, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.post("/books/{book_id}/reviews/", response_model=Review)
def create_review(book_id: int, review: Review, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    db_review = ReviewDB(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    background_tasks.add_task(send_confirmation_email, db_review.id)  # Background task for sending confirmation email
    return db_review

@app.get("/books/", response_model=List[Book])
def get_books(author: Optional[str] = None, publication_year: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(BookDB)
    if author:
        query = query.filter(BookDB.author == author)
    if publication_year:
        query = query.filter(BookDB.publication_year == publication_year)
    return query.all()

@app.get("/books/{book_id}/reviews/", response_model=List[Review])
def get_book_reviews(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.reviews

# Background task function for sending confirmation email
def send_confirmation_email(review_id: int):
    # Simulated email sending process
    print(f"Confirmation email sent for review with ID {review_id}")

# Test client for API testing
client = TestClient(app)

# Tests for API endpoints
def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Test Author", "publication_year": 2022})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"

def test_create_review():
    response = client.post("/books/1/reviews/", json={"text_review": "Great book!", "rating": 5})
    assert response.status_code == 200
    assert response.json()["text_review"] == "Great book!"

def test_get_books():
    response = client.get("/books/?author=Test Author")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_book_reviews():
    response = client.get("/books/1/reviews/")
    assert response.status_code == 200
    assert len(response.json()) > 0
