from flask import Blueprint, render_template
from app.src.domain.Investor import Investor
import app.src.db.dao as dao

uibp=Blueprint('ui', __name__, url_prefix='/ui')

@uibp.route('/', methods=['GET'])
def main():
    return render_template('home.html')

@uibp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@uibp.route('/investors', methods=['GET'])
def investor():
    investors=dao.get_all_investor()
    #investors.append(Investor)
    return render_template('investors.html', investors=investors)