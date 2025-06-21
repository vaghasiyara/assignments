from app.database import engine
from app.models.submission import Submission
from app.database import Base

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created.")

if __name__ == "__main__":
    create_tables()
