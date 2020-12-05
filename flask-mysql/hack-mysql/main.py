import pymysql
import os
from app import app
from config import mysql
from flask import jsonify
from flask import request
from flask import flash
from flask import Response
from werkzeug.utils import secure_filename

@app.route('/add', methods=['POST'])
def add_emp():

    #json1 = request.get_json()
    #lat1 = json1["lat"]
    #lon1 = json1["lon"]
    #comp1 = json1["comp"]
    #date1 = json1["reg_date"]

    firstname1 = request.form["firstname"]
    lastname1 = request.form["lastname"] 
    address1 = request.form["address"]
    date1 = request.form["date_of_birth"]
    contact_number1 = request.form["contact_number"]
    lat1 = request.form["lat"]
    lon1 = request.form["longt"]

    
    ####photo
    #f = request.files['photo']
    #img1 = f.read()
    ####
    
    
    if lat1 and lon1 and date1 and firstname1 and lastname1 and address1 and contact_number1 and request.method == 'POST':
    #if lat1 and lon1 and comp1 and  date1 and request.method == 'POST':
        #sqlQuery = "INSERT INTO complains(lat,lon,comp,reg_date) VALUES(%s, %s, %s, %s)"
        sqlQuery = "INSERT INTO general_data(firstname,lastname,date_of_birth,address,contact_number,lat,longt) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        bindData = (firstname1,lastname1,date1,address1,contact_number1,lat1,lon1)
        #bindData = (lat1,lon1,comp1,date1)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData)
        conn.commit()
            
        #respone = jsonify('Employee added successfully!')
        #respone.status_code = 200
        #return Response(" ## record was added ## \n", status=200, mimetype='application/json')
        return '## record added ##'
    else:
        return 'error'
    #try:
        
    #except Exception as e:
    #    print(e)
 #   finally:
 #       cursor.close()
 #       conn.close()
        
@app.route('/emp')
def emp():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, email, phone, address FROM rest_emp")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
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
        
        
        
        #########POST
           #sql = """INSERT INTO rest_emp(name, email, phone, address) VALUES(%s, %s, %s, %s)"""
    #MAIN_DB.execute( sql, (req_json["name"], req_json["email"], req_json["phone"], req_json["address"]) )
    #db.commit()
    #return Response(" ## record was added ## \n", status=200, mimetype='application/json')
    
    #file = request.files['photo']
    #extension = os.path.splitext(file.filename)[1]
    #f_name = str(uuid.uuid4()) + extension
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
    #filename = images.save(request.files['photo'])
    #self.image_filename = filename
    #self.image_url = images.url(filename) 

