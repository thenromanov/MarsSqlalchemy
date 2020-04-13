from flask import Flask
from data import dbSession
from data.users import *
from data.jobs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


def main():
    dbSession.globalInit('db/mars.sqlite')
    session = dbSession.createSession()
    user1 = User(surname='Scott', name='Ridley', age=21, position='captain',
                 speciality='research engineer', address='module_1', email='scott_chief@mars.org')
    user2 = User(surname='Orwell', name='George', age=46, position='pilot',
                 speciality='drone pilot', address='module_1', email='orwell@mars.org')
    user3 = User(surname='Burgess', name='Anthony', age=45, position='geologist',
                 speciality='magnetologist', address='module_1', email='burgess@mars.org')
    user4 = User(surname='Huxley', name='Aldous', age=38, position='astrologist',
                 speciality='pilot', address='module_1', email='huxley@mars.org')
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()