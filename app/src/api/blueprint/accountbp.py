import typing as t
import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Account import Account

account_bp = bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/get-all-accounts')
def get_all_accounts():
    accounts:t.List[Account]=dao.get_all_accounts()
    if len(accounts)==0:
        return json.dumps([])
    else:
        return json.dumps(accounts, default=lambda x: x.__dict__)

@bp.route('/get-account-by-id/<id>')
def get_acct_by_id(id: int): #need to troubleshoot this function in DAO
    account: Account = dao.get_account_by_id(id)
    if account is None:
        return 'Account does not exist'
    return json.dumps(account.__dict__)


@bp.route('/get-account-by-investor-id/<id>')
def get_account_by_investor_id(id):
    accounts: t.list[Account]=dao.get_accounts_by_investor_id(id)
    if len(accounts)==0:
        return 'Account does not exist'
    return json.dumps(accounts, default=lambda x: x.__dict__)


@bp.route('/delete-account/<id>', methods=['DELETE']) #foreign key constraint causing error
def delete_account(id):
    #check if there are any portfolios, if there are return error message to the user
    check_ports=dao.get_portfolios_by_acct_id(id)
    if len(check_ports) >0:
        return 'There are still existing portfolios. Delete those first before deleting the account'
    else:
        dao.delete_account(id)
        return '', 200

@bp.route('/update-account-balance/<id>/<balance>', methods=['PUT'])
def update_account_balance(id, balance):
    dao.update_acct_balance(id, balance)
    return '', 200

@bp.route('/create-account/<account_id>/<investor_id>/<balance>', methods=['POST'])
def create_account(account_id:int, investor_id: int, balance: float):
    #check if investor exists, use investor by id function if exists
    inv= dao.get_investor_by_id(investor_id)
    if inv is None:
        return 'There is no account with this id. Please create an investor account'
    #check if account id exists
    check_acc=dao.get_account_by_id(account_id)
    if check_acc is None:
        account = Account(account_id, investor_id, balance)
        dao.create_account(account)
        return 'Account Successfully Created', 200

    else:
        return 'An account with this ID already exists. Please try again'

