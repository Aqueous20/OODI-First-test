from fileinput import filename
import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask.helpers import send_from_directory
from werkzeug.utils import secure_filename
from .forms import BOOKING
from app.config import Config
#from flask_mysqldb import MySQL

# Config MySQL
#app.config['MySQL_HOST'] = 'localhost'
#app.config['MySQL_USER'] = 'root'
#app.config['MySQL_DB'] = 'myapp'
#app.config['MySQL_CURSORCLASS'] = 'DictCursor'

#mysql = MySQL(app)


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/Bookings', methods=['POST', 'GET'])
def Bookings():
    if not session.get('logged_in'):
        abort(401)

    myform= BOOKING(request.form)
    if request.method == 'POST' and myform.validate():
        if myform.validate_on_submit():
            #firstname = myform.firstname.data
            #lastname = myform.firstname.data
            #address = myform.firstname.data
            #email = myform.firstname.data
            #phonenumber = myform.firstname.data

            #cur = mysql.connection.cursor()

            #cur.execute("INSERT INTO clients(firstname,lastname,address,email,phonenumber) VALUES(%s,%s,%s,%s,%s,)",(firstname,lastname,address,email,phonenumber))
            
            #mysql.connection.commit()

            #cur.close()
            return redirect(url_for('home'))
        else:
            flash(flash_errors(myform))

    return render_template('Bookings.html', form = myform)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['ADMIN_USERNAME'] or request.form['password'] != app.config['ADMIN_PASSWORD']:
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            
            flash('You were logged in', 'success')
            return redirect(url_for('Bookings'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out', 'success')
    return redirect(url_for('home'))

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")