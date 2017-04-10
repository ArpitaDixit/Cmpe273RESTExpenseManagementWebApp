from flask_sqlalchemy import *
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
DATABASE = 'cmpe273'
PASSWORD = 'Arpita@123'
USER = 'root'
HOSTNAME = 'mysqlserver'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Expense_data(db.Model):
    __tablename__ ='expense_data'
    id = db.Column('id',db.Integer, primary_key = True)
    name = db.Column('name',db.String(100))
    email = db.Column('email',db.String(100))
    category = db.Column('category',db.String(50))
    description = db.Column('description',db.String(255))
    link = db.Column('link',db.String(2000))
    estimated_costs = db.Column('estimated_costs',db.String(100))
    submit_date = db.Column('submit_date',db.DateTime)
    status = db.Column('status',db.String(70))
    decision_date = db.Column('decision_date',db.DateTime)
    
    def __init__(self, id, name = '',email = '',category = '',description = '',link = '',estimated_costs = 0, submit_date ='',status = '',decision_date=''): 
        self.id = id
        self.name = name
        self.email = email
        self.category = category
        self.description = description
        self.link = link
        self.estimated_costs = estimated_costs
        self.submit_date = submit_date
        self.status = status 
        self.decision_date = decision_date

class CreateDB():
	def __init__(self, hostname=None):
		if hostname != None:	
			HOSTNAME = hostname
		import sqlalchemy
		engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME)) # connect to server
		engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE))

if __name__ == '__main__':
	manager.run()
