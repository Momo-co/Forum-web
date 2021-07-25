from application import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(1000), nullable = False)
    comments = db.relationship('Comment', backref = 'post')

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.String(1000), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable = False)

    
