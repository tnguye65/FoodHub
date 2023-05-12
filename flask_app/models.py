from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()



class User(db.Document, UserMixin):
    username = db.StringField(unique=True, required=True, min_length=1, max_length=40)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)
    profile_picture = db.ImageField()
    pic_encoded = db.StringField()
    bio = db.StringField(max_length=500)
    


    # Returns unique string identifying our object
    def get_id(self):
        return self.username

class Following(db.Document):
    user1 = db.ReferenceField(User)
    user2 = db.ReferenceField(User)
    date = db.StringField(required=True)
    
class Follower(db.Document):
    user1 = db.ReferenceField(User)
    user2 = db.ReferenceField(User)
    date = db.StringField(required=True)
    

class Review(db.Document):
    commenter = db.ReferenceField(User)
    content = db.StringField(required=True, min_length=5, max_length=500)
    date = db.StringField(required=True)
    id_business = db.StringField(required=True)
    movie_title = db.StringField(required=True)
    image = db.ImageField()
    image_encoded = db.StringField()