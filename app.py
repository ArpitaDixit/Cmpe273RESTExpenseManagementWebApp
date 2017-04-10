from flask import Flask, jsonify, request, abort, make_response
from a import Expense_data
from a import db
import datetime
import json


app = Flask(__name__)

@app.route('/v1/expenses',methods=['POST','GET'])
def post_expense(): 
    if request.method == "POST":
        last_id = Expense_data.query.order_by(Expense_data.id.desc()).first().id
        now = datetime.datetime.now()
        db.session.rollback()
        data = json.loads(request.data)
        new_row = Expense_data(last_id + 1,data['name'],data['email'],data['category'],data['description'],data['link'],data['estimated_costs'],data['submit_date'],'pending',None)
        db.session.add(new_row)
        db.session.commit()
        one = Expense_data.query.get(last_id + 1)
        one
        return jsonify(id =one.id,name = one.name, email = one.email, category = one.category, description = one.description, link = one.link, estimated_costs = one.estimated_costs, submit_date = one.submit_date, status = one.status, decision_date = one.decision_date),201
   

    
@app.route('/v1/expenses/<int:num>',methods=['GET','DELETE','PUT'])
def get_expense(num):
    if request.method == "GET":
        one = Expense_data.query.get(num)
        one
        if one is None:
            return 'Error',404 
        return jsonify(id =one.id,name = one.name, email = one.email, category = one.category, description = one.description, link = one.link, estimated_costs = one.estimated_costs, submit_date = one.submit_date, status = one.status, decision_date = one.decision_date)
    elif request.method == "DELETE":
        dele = Expense_data.query.filter_by(id=num).first()
        dele
        db.session.delete(dele)
        db.session.commit()
        return 'Data Deleted',204
    elif request.method == "PUT":
        data = json.loads(request.data)
        upd = Expense_data.query.filter_by(id=num).first()
        upd
        upd.estimated_costs = data['estimated_costs']
        db.session.commit()
        return 'Data Updated',202

app.run(debug=True, port=5000, host="0.0.0.0")
if __name__ == '__main__':
    app.run()
