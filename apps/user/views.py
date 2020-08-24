from flask import Blueprint, render_template

userBp = Blueprint('user', __name__)

@userBp.route('/')
def userCenter():
    return '用户中心'

@userBp.route('/register', methods=['POST', 'GET'])
def userRegister():
    return render_template('user/register.html')

@userBp.route('/login')
def userLogin():
    return render_template('user/login.html')