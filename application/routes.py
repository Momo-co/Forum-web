from application import app, db
from flask import redirect, request, render_template, url_for
from application.forms import BasicForm
from application.models import Post, Comment

@app.route('/')
@app.route('/home')
def home():
    all_post = Post.query.all()

    return render_template("home.html", all_post = all_post)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BasicForm()

    if request.method == 'POST':
        new_post = Post(content = form.post.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create.html', form = form)

@app.route('/forum/<int:id>', methods = ['GET', 'POST'])
def forum(id):
    form = BasicForm()
    current_post = Post.query.get(id)
    all_comment = Comment.query.all()
    if request.method == 'POST':
        new_comment = Comment(message = form.comment.data)
        new_comment.post_id = id
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('forum', id = id))
    else:
        return render_template('forum.html', current_post = current_post, form = form, all_comment = all_comment)

@app.route('/edit/<int:post_number>', methods = ['GET', 'POST'])
def edit(post_number):
    form = BasicForm()
    post = Post.query.get(post_number)
    if request.method == 'POST':
        post.content = form.edit_post.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('forum', id = post_number))
    else:
        return render_template('post_edit.html', form = form, post = post)

@app.route('/change/<int:comment_number>', methods = ['GET', 'POST'])
def change(comment_number):
    form = BasicForm()
    comment = Comment.query.get(comment_number)
    if request.method == 'POST':
        comment.message = form.modify_comment.data
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('forum', id = comment.post_id))
    else:
        return render_template('comment_edit.html', form = form, comment = comment)


