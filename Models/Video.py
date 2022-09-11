from config import db, ma

# the Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video[id={self.id}, name={self.name}, likes={self.likes}, views={self.views}]"
db.create_all()
# the Video schema (for JSON formatting)
class VideoSchema(ma.Schema):
    class Meta:
        fields = ("id","name","likes","views")
# Creating instance of schemas
# when theres a single instance to be returned
video_schema = VideoSchema(many = False)
# when there are multiple instances to be returned
videos_schema = VideoSchema(many = True)