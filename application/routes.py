from application import app, db
from flask import redirect, request, render_template, url_for
from application.forms import BasicForm
from application.models import Post, Comment

@app.route('/')
@app.route('/home')
def home():
    all_post = Post.query.all()

    return render_template("home.html", all_post = all_post)

@app.route('/post', methods = ['GET', 'POST'])
def post():
    form = BasicForm()

    if request.method == 'POST':
        new_post = Post(content = form.post.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create.html', form = form)

@app.route('/comment/<int:id>', methods = ['GET', 'POST'])
def comment(id):
    form = BasicForm()
    current_post = Post.query.get(id)
    all_comment = Comment.query.all()
    if request.method == 'POST':
        new_comment = Comment(message = form.comment.data)
        new_comment.post_id = id
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('comment', id = id))
    else:
        return render_template('comment.html', current_post = current_post, form = form, all_comment = all_comment)


