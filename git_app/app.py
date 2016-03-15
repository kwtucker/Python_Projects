from flask import Flask, flash, render_template, json, jsonify, request, redirect, url_for, session,g
import subprocess
from pync import Notifier
from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.github import GitHub

app = Flask(__name__)


app.config['GITHUB_CLIENT_ID'] = 'd2e6f04d44ae06dd5b75'
app.config['GITHUB_CLIENT_SECRET'] = '3a4ccb84b1e4dd4c7c15f01477a496cac904c4ce'
github = GitHub(app)
redirect_uri="http://localhost:5000/dash/"
state = "4F)vQzyf+YZctK2UnD"




engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/git_app'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
from models import *


@app.route('/')
def homepage():
    return render_template('login.html')


@app.route('/app/1/')
def home():
    return Notifier.notify('Hello Kevin',sound='Ping', execute="open /Applications/iTerm.app")

@app.route('/settings/')
def settings():
    return render_template('settings.html')

@app.route('/settingsSubmit',methods=['GET','POST'])
def settingsSubmit():
    #print str(session['token']) + "Submit"
    print request.args.get("gitAC")
    print request.args.get("gitPu")
    if not request.args.get("gitAC") is None:
        print 'commit'
        # print  request.args.get("gitAC")
        gAC = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitAC")).count()
        if(gAC == 0):
            u = UserSettings(int(session['userid']),request.args.get("gitAC"), 1 )
            db.session.add(u)
            db.session.commit()
        else:
            print "Hello1"


    if not request.args.get("gitPu") is None:
        print 'push'
        print  request.args.get("gitPu")
        gPU = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitPu")).count()
        if(gPU == 0):
            u = UserSettings(int(session['userid']),request.args.get("gitPu"), 1 )
            db.session.add(u)
            db.session.commit()
        else:
            print "Hello2"


    # If the gitAC option is switched off the setting will be removed
    if request.args.get("gitAC") is None:
        gACDelete = UserSettings.query.filter_by(user_id=session['userid'], setting_id=1).one()
        db.session.delete(gACDelete)
        db.session.commit()

    # If the gitPu option is switched off the setting will be removed
    if request.args.get("gitPu") is None:
        gPUDelete = UserSettings.query.filter_by(user_id=session['userid'], setting_id=2).one()
        db.session.delete(gPUDelete)
        db.session.commit()




    # print int(request.form['gitAC'])
    return render_template('settings.html')


@app.route('/githubLogin/', methods=['GET','POST'])
def login():
    print "hello"
    db.session.commit()

    if session.get('user_id', None) is None:
        return github.authorize(scope="repo user", redirect_uri=redirect_uri, state=state)
    else:
        return 'Already logged in'


@app.route('/dash/')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        flash("Authorization failed.")
        print "Authorization failed"
        return redirect('/')
    user = Users.query.filter_by(github_access_token=oauth_token).first()

    if user is None:
        user = Users(oauth_token)
        db.session.add(user)

    user.github_access_token = oauth_token
    db.session.commit()

    session['userid'] = user.id
    session['token']  = user.github_access_token

    return render_template('userDash.html')

# @app.route('/user')
# def user():
#     return jsonify(github.get('user'))

@github.access_token_getter
def token_getter():
    print "token Getter"
    user = g.user
    if user is not None:
        return user.github_access_token


@app.route('/logout')
def logout():
    session.delete()
    return redirect(url_for('homepage'))



if __name__ == "__main__":
    app.secret_key = "nT>pB2z^gR8JQvisvX"
    app.run(debug=True)

