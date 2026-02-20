from flask import Flask, render_template, request,redirect,flash,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
app.app_context().push()

class Employees(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name','').strip()
        email = request.form.get('email',"").strip()
        if not name or not email:
            flash("All fields are required","danger")
            return redirect('/');
        employee = Employees(name=name, email=email)
        db.session.add(employee)
        db.session.commit()
    flash("form submission succesful","success")

    allemployee = Employees.query.all()
    return render_template('index.html',allemployees=allemployee)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not name:
            flash("Name is required", "danger")
            return redirect('/register')
        if not email:
            flash("Email is required", "danger")
            return redirect('/register')
        if not password:
            flash("Password is required", "danger")
            return redirect('/register')
        if len(password) < 6:
            flash("Password must be at least 6 characters", "danger")
            return redirect('/register')
        
        existing_user = Employees.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered", "danger")
            return redirect('/register')
        
        new_user = Employees(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employees.query.filter_by(sno=sno).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        employee = Employees.query.filter_by(sno=sno).first()
        employee.name = name
        employee.email = email
        db.session.add(employee)
        db.session.commit()
        return redirect("/")

    employee = Employees.query.filter_by(sno=sno).first()
    return render_template("update.html", employee=employee)
@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = Employees.query.filter_by(email=session['email']).first()
        return render_template("dashboard.html",user=user)
if __name__ == '__main__':
    app.run(debug=True)