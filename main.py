import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_emp():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_phone = _json['phone']	
		if _name and _email and _phone and request.method == 'POST':			
			sqlQuery = "INSERT INTO Details(id, name, email, phone) VALUES(%s, %s, %s, %s)"
			bindData = (id,_name, _email, _phone)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User added successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp')
def emp():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone FROM Details")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp/<int:id>')
def emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone FROM Details WHERE id =%s", id)
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_emp():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']
		_phone = _json['phone']
                if _name and _email and _phone and _id and request.method == 'PUT':			
			sqlQuery = "UPDATE Details SET name=%s, email=%s, phone=%s WHERE id=%s"
			bindData = (_name, _email, _phone, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User updated successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()	
                except Exception as e:
		 print(e)
	        finally:
		 cursor.close() 
		 conn.close()
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM Details WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('User deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run()