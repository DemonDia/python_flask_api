from config import db, ma

# the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f"User[id={self.id}, name={self.name}]"

# the User schema (for JSON formatting)
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name")
# Creating instance of schemas
# when theres a single instance to be returned
user_schema = UserSchema(many = False)
# when there are multiple instances to be returned
users_schema = UserSchema(many = True)