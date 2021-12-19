#My application entry point
from flask import Flask #python framework for developing web apps
import typing as t
import json
from app.src.domain.Investor import Investor
import app.src.db.dao as dao
from app.src.api.blueprint.investorbp import investor_bp
from app.src.api.blueprint.accountbp import account_bp
from app.src.api.blueprint.portfoliobp import portfolio_bp
from app.src.api.blueprint.uibp import uibp

app=Flask(__name__) #instantiates the flask class
app.route('/')

app.register_blueprint(investor_bp)
app.register_blueprint(account_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(uibp)







#investor object needs to be encoded into json
#JSON encoding: converting python objects to json format so that the client can understand the data
#data that i sent back from the server should adhere to JSON format
#data sent to the server in a request should adhere to json format

#one file for account, one for investor, one for portfolio
if __name__=='__main__':
    app.run(port=8080, debug=True)

#pip3 install -r requirements.txt  installs everything in requirements doc