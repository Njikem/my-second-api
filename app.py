from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement
from helpers import check_endpoint_info

app = Flask(__name__)


# Item

@app.get('/api/items')
def get_all_items():
    
    try: 
        results = run_statement("CALL get_all_items()", [])
        if(results == None):
            return "somthing is wrong"
        return make_response(jsonify(results), 200)
    except error as error:
        return make_response("f{error}", 400) 



@app.post('/api/item')
def insert_new_item():
    valid_check = check_endpoint_info(request.json, ['name', 'description', 'in_stock_quantity'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    
    results = run_statement("CALL insert_new_item(?, ?, ?)", [request.json.get("name"), request.json.get("description"), request.json.get("in_stock_quantity")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)

   
@app.patch('/api/item')
def update_items():
    valid_check = check_endpoint_info(request.json, ['id', 'new_in_stock_quantity'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    
    results = run_statement("CALL update_items(?, ?)", [request.json.get("id"), request.json.get("new_in_stock_quantity")])
    if(type(results) ==list): 
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    

@app.delete('/api/item/<int:id>')
def delete_item(id):
    if (id):
         results = run_statement("CALL delete_item(?)", [id])
         # with a real id / Without a correcr id
         print(results)
         return make_response(jsonify(results), 200)
    
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)

   


# Employee

    
@app.get('/api/employee/<int:id>')
def get_employee(id):
    results = run_statement("CALL get_employee(?)", [id])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
      

@app.post('/api/employee')
def insert_new_employee():
    valid_check = check_endpoint_info(request.json, ['name', 'position', 'hourly_wage'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    
    results = run_statement("CALL insert_new_employee(?, ?, ?)", [request.json.get("name"), request.json.get("position"), request.json.get("hourly_wage")])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)

   
@app.patch('/api/employee')
def update_employee():
    valid_check = check_endpoint_info(request.json, ['id', 'new_hourly_wage'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    
    results = run_statement("CALL update_employee(?, ?)", [request.json.get("id"), request.json.get("new_hourly_wage")])
    if(type(results) ==list): 
        return make_response(jsonify(results), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
    

@app.delete('/api/employee/<int:id>')
def delete_employee(id):
    if (id):
         results = run_statement("CALL delete_employee(?)", [id])
         print(results)
         return make_response(jsonify(results), 200)
    
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)
       

    
        
    
    
     
        
        







app.run(debug=True)