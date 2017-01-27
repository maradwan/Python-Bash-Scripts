from flask import Flask, jsonify, abort, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'users'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)




app = Flask(__name__)


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    try:
        # validate the received values
        name = request.json.get('name', "")
        phonenumber = request.json.get('phonenumber', "")
        email = request.json.get('email', "")
        if name and phonenumber and email:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO address(name,phone,email) VALUES ('" + name + "', '" + phonenumber + "' , '" + email + "')")
            data = cursor.fetchall()
            print (data) 
            if len(data) is 0:
                conn.commit()
                return jsonify({'name': name},{'phonenumber': phonenumber},{'email': email}), 201
            else:
                abort(400)
        else:
            return jsonify({'You Need to insert Email,Phone Numner and Email': data }), 400

    except Exception as e:
        abort(400)
    finally:
        cursor.close()
        conn.close()


@app.route('/todo/api/v1.0/tasks/<email>', methods=['GET'])
def get_task(email):
    try:
        if email:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * from address where email='" + email + "'")
            data = cursor.fetchall()
            if data is None:
                abort(404)
            else:
                return jsonify({'data': data[0]})
    except Exception as e:
        abort(404)
    finally:
        cursor.close()
        conn.close()
 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1.0/tasks/<email>', methods=['PUT'])
def update_task(email):
    try:
        phonenumber = request.json.get('phonenumber', "")
        #email = request.json.get('email', "")
        if phonenumber and email:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("update address set phone = '" + phonenumber + "' where email='" + email + "'")
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return jsonify({'result': True})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            abort(404)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/todo/api/v1.0/tasks/<email>', methods=['DELETE'])
def delete_task(email):
    try:
        if email:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("delete from address where email='" + email + "'")
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return jsonify({'result': True})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            abort(404)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
