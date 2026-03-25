

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-c171121ed3014d058758d7e565efba61-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzI2OTkxMjAsInAiOnsicm9hIjp7Im5zIjpbIjAxOWNiZDE5LWQ1MDEtNzUwNy1hYzk1LTVmZDZkZWIwMDk0NyJdfSwicnciOnsibnMiOlsiMDE5Y2JkMTktZDUwMS03NTA3LWFjOTUtNWZkNmRlYjAwOTQ3Il19fSwicmlkIjoiZjc2ZjgzNmYtNzlhYS00NWQyLWEyMzMtMGZkMGY5ZTk0N2UzIn0.4JzkOUDSlCJCBqlaW5lkgtlRhJfNVud-8PmoTMVm5yRYnhXM9hkFo9mbD3QwShOSA4Hyd9T8t5BMTDyi0IW9Ag",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

