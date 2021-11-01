# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete
import typing as t
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection
import config
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio


def get_cnx() -> MySQLConnection:
    return connect(**config.dbparams)

'''
    Investor DAO functions
'''

def get_all_investor() -> list[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors

def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where id = %s'
    cursor.execute(sql, (id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        investor = Investor(row['name'], row['status'], row['id'])
        return investor
    db_cnx.close()

def get_investors_by_name(name: str) -> list[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where name = %s'
    cursor.execute(sql, (name,))
    if cursor.rowcount == 0:
        investors: list[dict] = []
    else:
        rows = cursor.fetchall()
        for row in rows:
            investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors


def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx:MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql:str = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()

def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s'
    cursor.execute(sql, (id,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set name = %s where id = %s'
    cursor.execute(sql, (id, name))
    db_cnx.commit()
    db_cnx.close()

def update_investor_status(id: int, status: str) -> None:
    '''
        Update the investor status [U]
    '''
    db_cnx :MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set status = %s where id = %s'
    cursor.execute(sql, (id, status))
    db_cnx.commit()
    db_cnx.close()

'''
    Account DAO functions
'''
def get_all_accounts() -> list[Account]:
    # Code goes here
    db_cnx: MySQLConnection =get_cnx()
    cur=db_cnx.cursor(dictionary=True)
    sql='select * from account'
    cur.execute(sql)
    rows=cur.fetchall()
    if len(rows)==0:
        return []
    accounts:list[dict]=[]
    for row in rows:
        accounts.append(
            Account(row['account_number'], row['investor_id'], row['balance'])
        )
    db_cnx.close()
    return accounts
def get_account_by_id(account_number: int) -> Account:
    # Code goes here
    db_cnx: MySQLConnection =get_cnx() #create db connection
    cur=db_cnx.cursor(dictionary=True) #cursor from db connection, everytime you create a cursor place dictionary to true so results come back as a dict
    sql='select account_number, investor_id, balance from account where account_number=%s' #sql query to get data, ? is a placeholder
    cur.execute(sql, (account_number,))#remember tuple of 1 needs an additional comma: (1)->Not a tuple, as a tuple, the values to replace the placeholder
    rows=cur.fetchone()
    if len(rows)==0:
        return []
    accounts=[]
    for row in rows:
        accounts.append(Account(row['investor_id'], row['balance'], row['account_number']))
    db_cnx.close()
    return accounts

def get_accounts_by_investor_id(investor_id: int) -> list[Account]:
    # Code goes here
    db_cnx: MySQLConnection =get_cnx() #create db connection
    cur=db_cnx.cursor(dictionary=True) #cursor from db connection, everytime you create a cursor place dictionary to true so results come back as a dict
    sql='select account_number, investor_id, balance from account where investor_id=%s' #sql query to get data, ? is a placeholder
    cur.execute(sql, (investor_id,))#remember tuple of 1 needs an additional comma: (1)->Not a tuple, as a tuple, the values to replace the placeholder
    rows=cur.fetchall()
    if len(rows)==0:
        return []
    accounts=[]
    for row in rows:
        accounts.append(Account(row['investor_id'], row['balance'], row['account_number']))
    db_cnx.close()
    return accounts
def delete_account(account_number: int) -> None:
    # Code goes here Delete function
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_acct_balance(account_number: int, balance: float) -> None:
    # Code goes here Update Function
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance = %s where account_number = %s'
    cursor.execute(sql, (balance, account_number))
    db_cnx.commit()
    db_cnx.close()

def create_account(account: Account) -> None:
    # Create Function
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (investor_id, balance) values (%s, %s)'
    cursor.execute(sql, (account.investor_id, account.balance))
    db_cnx.commit()
    db_cnx.close()

'''
    Portfolio DAO functions
'''
def get_all_portfolios() -> list[Portfolio]:
    # code goes here Read function
    cnx: MySQLConnection =get_cnx()
    cur=cnx.cursor(dictionary=True)
    sql:str='select account_number, ticker, quantity, purchase_price from portfolio'
    cur.execute(sql)
    rows=cur.fetchall()
    if len(rows)==0:
        return []
    portfolios=[]
    for row in rows:
        portfolios.append(
            Portfolio(row['account_number'], row['ticker'], row['quantity'], row['purchase_price'])
        )
    cnx.close()
    return portfolios

def get_portfolios_by_acct_id(account_number: int) -> list[Portfolio]:
    # Read function
    db_cnx: MySQLConnection =get_cnx() #create db connection
    cur=db_cnx.cursor(dictionary=True) #cursor from db connection, everytime you create a cursor place dictionary to true so results come back as a dict
    sql='select account_number, ticker, quantity, purchase_price from portfolio where account_number=%s' #sql query to get data, ? is a placeholder
    cur.execute(sql, (account_number,))#remember tuple of 1 needs an additional comma: (1)->Not a tuple, as a tuple, the values to replace the placeholder
    rows=cur.fetchall()
    if len(rows)==0:
        return []
    portfolios=[]
    for row in rows:
        portfolios.append(
            Portfolio(row['account_number'], row['ticker'], row['quantity'], row['purchase_price'])
    )
    db_cnx.close()
    return portfolios

def get_portfolios_by_investor_id(investor_id: int) -> list[Portfolio]:
    #Read
    db_cnx: MySQLConnection =get_cnx() #create db connection
    cur=db_cnx.cursor(dictionary=True) #cursor from db connection, everytime you create a cursor place dictionary to true so results come back as a dict
    sql='select a.account_number, a.ticker, a.quantity, a.purchase_price, b.investor_id from portfolio a left join account b on a.account_number=b.account_number where account_number=%s' #sql query to get data, ? is a placeholder
    cur.execute(sql, (investor_id,))#remember tuple of 1 needs an additional comma: (1)->Not a tuple, as a tuple, the values to replace the placeholder
    rows=cur.fetchall()
    if len(rows)==0:
        return []
    portfolios:list[Portfolio]=[]
    for row in rows:
        portfolios.append(
            Portfolio(row['investor_id'],row['account_number'], row['ticker'], row['quantity'], row['purchase_price'])
    )
    db_cnx.close()
    return portfolios

def delete_portfolio(account_number: int) -> None:
    #Delete
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from portfolio where account_number = %s'
    cursor.execute(sql, (account_number,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def buy_stock(account_number:int,ticker: str, purchase_price: float, volume: int) -> None:
    #Read
    # 1. update quantity in portfolio table
    # 2. update the account balance:


    #Retrieve current balance
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql: str ='select balance from account where account_number=%s'
    cursor.execute(sql,(account_number,))
    row=cursor.fetchone()
    current_balance= row[0]
    db_cnx.close()

    #check if funds are sufficient
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    total_stock_price=purchase_price*volume
    if total_stock_price>current_balance:
        print("Insufficient Funds to make this Trade")
        return None

    #update balance
    sql:str='update account set balance=balance-%s where account_number=%s'
    cursor.execute(sql,(total_stock_price,account_number))
    db_cnx.commit()
    db_cnx.close()

    #create list of stocks in portfolio
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)
    sql: str ='select distinct ticker from portfolio where account_number=%s'
    cursor.execute(sql, (account_number,))
    rows=cursor.fetchall()
    stocks=[]
    for row in rows:
        stocks.append(row)
    db_cnx.close()

    #check if ticker in list
    #update quantity
    #insert values
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    if ticker not in stocks:
        sql:str='insert into portfolio(account_number, ticker, quantity, purchase_price) values (%s,%s,%s,%s)'
        cursor.execute(sql, (account_number, ticker, volume, purchase_price))
        db_cnx.commit()

    else:
        sql:str='update portfolio set quantity=quantity+%s where account_number=%s and ticker=%s'
        cursor.execute(sql,(volume, account_number,ticker))
        db_cnx.commit()
    db_cnx.close()


def sell_stock(account_number:int,ticker: str, volume: int, sale_price: float) -> None:
    # 1. update quantity in portfolio table
    # 2. update the account balance:
    # Example: 10 APPL shares at $1/share with account balance $100
    # event: sale of 2 shares for $2/share
    # output: 8 APPLE shares at $1/share with account balance = 100 + 2 * (12 - 10) = $104
    #Read Function

    #sale_price*volume to get total dollars

    # get current quantity
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True)
    sql:str='select quantity from portfolio where account_number=%s and ticker=%s'
    cursor.execute(sql, (account_number, ticker))
    row=cursor.fetchone()
    current_quantity=[]
    for i in row:
        current_quantity.append(i)
    current_quantity=current_quantity[0]
    db_cnx.close()

    #make sure not to sell more than we have
    db_cnx: MySQLConnection =get_cnx()
    cursor=db_cnx.cursor()
    if current_quantity < volume:
        print("You do not have sufficient shares to sell")
        return None

    elif current_quantity==volume:
        sql:str='delete from portfolio where account_number=%s and ticker=%s'
        cursor.execute(sql, (account_number, ticker))
        db_cnx.commit()

    elif current_quantity>volume:
        sql:str='update from portfolio set quantity=quantity-%s where account_number=%s and ticker=%s'
        cursor.execute(sql, (volume,account_number, ticker))
        db_cnx.commit()
    db_cnx.close()

    #update balance with total sale price
    total_sale=sale_price*volume
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor()
    sql:str='update account set balance=balance+%s where account_number=%s'
    cursor.execute(sql,(total_sale, account_number))
    db_cnx.commit()

    db_cnx.close()













