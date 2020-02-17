# -*- coding: utf8 -*-
#import pymysql
from flask import Flask, render_template, json, request, redirect, session
from flaskext.mysql import MySQL
import service
import makejenkinsfile
#import MySQLdb
#from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_SOCKET'] = None
app.secret_key = 'you will never know'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_sign_up')
def show_sign_up():
    return render_template('sign_up.html')


@app.route('/sign_up', methods=['POST'])
def sign_up():
    try:
        _name = request.form['inputName']

        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        if _name and _email and _password:
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': u'用户创建成功！！'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': u'<span>请输入必要的信息</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})

    finally:
        cursor.close()
        conn.close()


@app.route('/show_sign_in')
def show_sign_in():
    return render_template('sign_in.html')


@app.route('/validate_login', methods=['POST'])
def validate_login():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

    except Exception as e:
        return render_template('error.html', error=str(e))

    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_validateLogin', (_username,))
    data = cursor.fetchall()

    if len(data) > 0:
        if check_password_hash(str(data[0][3]), _password):
            session['user'] = data[0][0]
            return redirect('/user_home')
        else:
            return render_template('error.html', error=u'邮箱或密码错误。')
    else:
        return render_template('error.html', error=u'邮箱或密码错误。')


@app.route('/user_home')
def user_home():
    if session.get('user'):
        return render_template('user_home.html')
    else:
        return render_template('error.html', error=u'未授权访问')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


@app.route('/show_add_wish')
def show_add_wish():
    return render_template('add_wish.html')


@app.route('/add_wish', methods=['POST'])
def add_wish():
    try:
        if session.get('user'):
            _title = request.form['inputTitle']
            _num = request.form['inputNum']
            #_user_id=request.form['inputUser_id']#权限者
            _address=request.form['inputAddress']
            _description = request.form['inputDescription']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_addWish', (_title,_num,_address, _description, _user))
            print(type(_description))
            description = makejenkinsfile.make(_description)

            service.addservice(_title, description)





            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return redirect('/user_home')
            else:
                return render_template('error.html', error=u'发生错误!')

        else:
            return render_template('error.html', error=u'未授权访问')
    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        conn.close()


@app.route('/get_wish')
def get_wish():
    try:
        if session.get('user'):
            _user = session.get('user')

            con = mysql.connect()
            cursor = con.cursor()
            cursor.callproc('sp_GetWishByUser', (_user,))
            wishes = cursor.fetchall()

            wishes_dict = []
            for wish in wishes:
                wish_dict = {
                    'Id': wish[0],
                    'Title': wish[1],
                    'Description': wish[2],
                    'User_id':wish[3],
                    'Date': wish[4],
                    'Num':wish[5],
                    'Address':wish[6]
                }
                wishes_dict.append(wish_dict)

            return json.dumps(wishes_dict)
        else:
            return render_template('error.html', error=u'未授权访问')
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route('/get_wish_by_id', methods=['POST'])
def get_wish_by_id():
    try:
        if session.get('user'):

            _id = request.form['id']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetWishById', (_id, _user))
            result = cursor.fetchall()

            wish = list()
            wish.append({'Id': result[0][0], 'Title': result[0][1], 'Description': result[0][2],'User_id':result[0][3],'Date':result[0][4],'Num':result[0][5],'Address':result[0][6]})

            return json.dumps(wish)
        else:
            return render_template('error.html', error=u'未授权访问')
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route('/update_wish', methods=['POST'])
def update_wish():
    try:
        if session.get('user'):
            _user = session.get('user')
            _title = request.form['title']
            _num=request.form['num']
            _address=request.form['address']
            _description = request.form['description']
            #_user_id=request.form['user_id']
            #_date=request.form['date']

            _wish_id = request.form['id']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_updateWish', (_title,_num,_address,_description,_wish_id, _user))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'status': 'OK'})
            else:
                return json.dumps({'status': 'ERROR'})
    except Exception as e:
        return json.dumps({'status': u'未授权访问'})
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_wish', methods=['POST'])
def delete_wish():
    try:
        if session.get('user'):
            _id = request.form['id']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_deleteWish', (_id, _user))

            result = cursor.fetchall()

            if len(result) is 0:
                conn.commit()
                return json.dumps({'status': 'OK'})
            else:
                return json.dumps({'status': u'发送错误'})
        else:
            return render_template('error.html', error=u'未授权访问')
    except Exception as e:
        return json.dumps({'status': str(e)})
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
