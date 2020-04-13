from flask import Flask, render_template
from data import dbSession
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    session = dbSession.createSession()
    users = session.query(User).all()
    jobs = session.query(Jobs).all()
    return render_template('index.html', users=users, jobs=jobs)


def main():
    dbSession.globalInit('db/mars.sqlite')
    app.run()


if __name__ == '__main__':
    main()
