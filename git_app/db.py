from app import db
from models import Users, UserSettings, Settings

db.create_all()

# db.session.add(DevPost("First Post", "Kevin Tucker", "Yep this is the post"))
# db.session.add(DevPost("First Post", "Kevin Tucker", "Yep this is the post"))
# db.session.add(Users("yep", "kwtucker4@gmail.com", "kwtucker", "lskdjflsdkjflskdjflsd"))
# db.session.commit()