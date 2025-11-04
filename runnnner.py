from main import app
from project.database import SessionLocal
from project.users.models import User

user = User(username='test1', email='test1@example.com')
session = SessionLocal()
session.add(user)
session.commit()

new_session = SessionLocal()
usr = new_session.query(User).first().username
print(usr)