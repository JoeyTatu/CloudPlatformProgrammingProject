from flask import Blueprint, Flask, render_template, request, redirect, send_file, url_for, jsonify
import aws_controller
# from . import db

auth = Blueprint('auth', __name__)

@auth.route('/account/login')
def login():
    return render_template('account/login.html')

@auth.route('/account/signup')
def signup():
    return render_template('account/signup.html')

@auth.route('/account/logout')
def logout():
    return 'Logout'