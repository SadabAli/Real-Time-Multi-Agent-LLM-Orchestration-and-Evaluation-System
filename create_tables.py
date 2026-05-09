from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

print("Tables created successfully")