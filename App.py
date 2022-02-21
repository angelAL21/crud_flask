from flask import Flask , render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'mysqlflask'
mysql= MySQL(app)

#sessions.
app.secret_key = 'mysecretkey'

#routes
@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contacts():
    if request.method == 'POST':
        fullname= request.form['fullname'] 
        phone= request.form['phone'] 
        email= request.form['email'] 
        print(fullname)
        print(phone)
        print(email)
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)", (fullname, phone, email))
        mysql.connection.commit()
        flash('success')
        return redirect(url_for('Index'))

@app.route('/edit_contact')
def edit_contacts():
    return 'edit_contacts'

@app.route('/delete_contact')
def delete_contacts():
    return 'delete contacts'

if __name__ == '__main__':
    app.run(port=3000, debug=True)