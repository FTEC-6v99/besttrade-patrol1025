import typing as t
import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Portfolio import Portfolio


portfolio_bp =bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

#Portfolio Routes


@bp.route('/get-all-portfolios')
def get_portfolios():
    portfolios:t.List[Portfolio]=dao.get_all_portfolios()
    if len(portfolios)==0:
        return json.dumps([])
    else:
        return json.dumps(portfolios, default=lambda x: x.__dict__())

@bp.route('/get-portfolio-by-account-id/<id>')
def get_portfolios_by_acct_id(id):
    portfolio: t.List[Portfolio] = dao.get_portfolios_by_acct_id(id)
    if len(portfolio)==0:
        return 'Portfolio does not exist'
    return json.dumps(portfolio, default=lambda x: x.__dict__())

@bp.route('/get-portfolio-by-investor-id/<id>')
def get_portfolio_by_investor_id(id):
    portfolio: t.List[Portfolio] = dao.get_portfolios_by_acct_id(id)
    if len(portfolio)==0:
        return 'Portfolio does not exist'
    return json.dumps(portfolio, default=lambda x: x.__dict__())

@bp.route('/delete-portfolio/<account_id>/<ticker>')
def delete_portfolio(account_id, ticker):
    dao.delete_portfolio(account_id, ticker)
    return 'Portfolio Deleted', 200


@bp.route('/buy-stock/<account_number>/<ticker>/<purchase_price>/<volume>', methods=['POST'])
def buy_stock(account_number:int,ticker: str, purchase_price: float, volume: int):
    dao.buy_stock(account_number, ticker, purchase_price, volume)
    return f'{volume} shares of {ticker} were bought at {purchase_price}', 200

@bp.route('/sell-stock/<account_number>/<ticker>/<sale_price>/<volume>', methods=['POST'])
def sell_stock(account_number:int,ticker: str, sale_price:float, volume: int):
    dao.sell_stock(account_number, ticker, sale_price, volume)
    return f'{volume} shares of {ticker} were sold at {sale_price}', 200