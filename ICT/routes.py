from ICT import app
from flask import redirect, request,render_template,flash,url_for
from ICT.forms import Form
from ICT.models import User
from ICT import db

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    user.username = "changed"
    db.session.commit()
    flash("Your user has been deleted", 'success')
    return redirect(url_for('index'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = Form()
    if(request.method =='POST'):
        if form.validate_on_submit():
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You have Signed UP!!', 'success')
            return redirect(url_for('index'))
        else:
            flash("sign up failed, check errors", 'danger')
    return render_template('forms.html', form=form)
