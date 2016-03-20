from flask import Flask, render_template, json, jsonify, request, redirect, url_for, session
import urllib2,subprocess
from requests import put, get
from pync import Notifier
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.github import GitHub


app = Flask(__name__)


app.config['GITHUB_CLIENT_ID'] = 'd2e6f04d44ae06dd5b75'
app.config['GITHUB_CLIENT_SECRET'] = '3a4ccb84b1e4dd4c7c15f01477a496cac904c4ce'
github = GitHub(app)
redirect_uri="http://localhost:5000/dash/"
state = "4F)vQzyf+YZctK2UnD"


#engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/git_app'
engine = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kwtucker:relation_cloak_koch@git.cvsrzc8hq30b.us-east-1.rds.amazonaws.com:3306/git_app'

db = SQLAlchemy(app)
from models import *


@app.route("/api/settings/<int:user_id>/<user_oauth>", methods=['GET', 'POST'])
def geta(user_id,user_oauth):
    userO = Users.query.filter_by(github_access_token='%s' % user_oauth).first()

    if userO is None:
        error= [("gitAddCommit",int(404)),("gitPush",int(404))]
        errorDict=dict(error)
        return jsonify(errorDict)
    if userO:
        if int(userO.id) == int(user_id):
            n1 = UserSettings.query.filter_by(user_id='%d' % user_id, setting_id=1).first()
            n2 = UserSettings.query.filter_by(user_id='%d' % user_id, setting_id=2).first()
            Arr= [("gitAddCommit",int(n1.value)),("gitPush",int(n2.value))]
            Dictionary=dict(Arr)
            return jsonify(Dictionary)


@app.route('/')
def homepage():
    return render_template('login.html')


@app.route('/beer')
def beer():
    Notifier.notify('IPA Only', title="Beer Me",sound='Ping')
    return redirect('/')


@app.route('/KevinTucker')
def KevinTucker():
    Notifier.notify('Click for my GitHub', title="Kevin Tucker",sound='Ping', open='https://github.com/kwtucker')
    return redirect('/')

@app.route('/kevintucker')
def kevintucker2():
    Notifier.notify('Click for my GitHub', title="Kevin Tucker",sound='Ping', open='https://github.com/kwtucker')
    return redirect('/')

@app.route('/settings/')
def settings():
    if session:
        n1 = UserSettings.query.filter_by(user_id=session['userid'], setting_id=1).first()
        n2 = UserSettings.query.filter_by(user_id=session['userid'], setting_id=2).first()

        return render_template('settings.html', n1=n1.value, n2=n2.value)
    else:
        return redirect('/')



@app.route('/settingsSubmit',methods=['GET', 'POST'])
def settingsSubmit():
    if session:
        if not request.args.get("gitAC") is None:
            gAC = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitAC")).count()
            if(gAC == 0):
                u = UserSettings(int(session['userid']),request.args.get("gitAC"), 1)
                db.session.add(u)
                db.session.commit()
            else:
                ac = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitAC")).first()
                ac.value = 1
                db.session.commit()


        if not request.args.get("gitPu") is None:
            gPU = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitPu")).count()
            if(gPU == 0):
                u = UserSettings(int(session['userid']),request.args.get("gitPu"), 1 )
                db.session.add(u)
                db.session.commit()
            else:
                pu = UserSettings.query.filter_by(user_id=session['userid'], setting_id=request.args.get("gitPu")).first()
                pu.value = 1
                db.session.commit()


        # If the gitAC option is switched off the setting will be updated
        if request.args.get("gitAC") is None:
            gACD = UserSettings.query.filter_by(user_id=session['userid'], setting_id=1).count()
            if(gACD > 0):
                gACDelete = UserSettings.query.filter_by(user_id=session['userid'], setting_id=1).one()
                gACDelete.value = 0
                db.session.commit()
            else:
                pass

        # If the gitPu option is switched off the setting will be updated
        if request.args.get("gitPu") is None:
            gPUD = UserSettings.query.filter_by(user_id=session['userid'], setting_id=2).count()
            if(gPUD > 0):
                gPUDelete = UserSettings.query.filter_by(user_id=session['userid'], setting_id=2).one()
                gPUDelete.value = 0
                db.session.commit()
            else:
                pass

        return redirect(url_for("settings"))

    else:
        return redirect('/')




@app.route('/githubLogin/', methods=['GET','POST'])
def login():
    db.session.commit()
    if session.get('user_id', None) is None:
        return github.authorize(scope="repo user", redirect_uri=redirect_uri, state=state)
    else:
        return 'Already logged in'


@app.route('/dash/')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        if session:
            return render_template('userDash.html')
        else:
            return redirect('/')

    user = Users.query.filter_by(github_access_token=oauth_token).first()

    userprofile = urllib2.urlopen('https://api.github.com/user?access_token='+ oauth_token)
    uProObj = dict(json.load(userprofile))

    if user is None:
        user = Users(oauth_token)

        db.session.add(user)
        db.session.commit()


    user.github_access_token = oauth_token


    session['userid']      = user.id
    session['token']       = user.github_access_token
    session['usr']         = uProObj['login']
    session['userImgLink'] = uProObj['avatar_url']


    userinitSettings = UserSettings.query.filter_by(user_id=session['userid']).all()
    if not userinitSettings:
        initAC = UserSettings(int(session['userid']),1, 0)
        initPU = UserSettings(int(session['userid']),2, 0)
        db.session.add(initAC)
        db.session.add(initPU)
        db.session.commit()

    return render_template('userDash.html', sess=session )



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))



if __name__ == "__main__":
    app.secret_key = "nT>pB2z^gR8JQvisvX"
    app.run()

