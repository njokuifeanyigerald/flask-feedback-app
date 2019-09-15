from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
app = Flask(__name__)


ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/lexus'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://emmmxzpkwhimeo:140e8e8e3a05bd6891e8da66edab82392bb1122709343047e9596e72d388ef71@ec2-54-221-212-126.compute-1.amazonaws.com:5432/d2mkdrcnujhbnn'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

# send_mail= send_mail(customer, dealer, rating, comments)
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer =db.Column(db.String(200), unique=True)
    dealer =db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer =customer
        self.dealer =dealer
        self.rating =rating
        self.comments =comments


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer,dealer,rating,comments)

        if customer == "" or dealer == "":
            return render_template('home.html', message='please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer,dealer,rating,comments)
            return render_template('success.html')
        return render_template('home.html', message='you have already submitted feedback')


if __name__ == '__main__':
    app.run()
