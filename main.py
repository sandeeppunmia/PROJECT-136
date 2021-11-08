from flask import Flask,jsonify,request
from data import data
app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"It's a success"
    }),200
@app.route("/star")
def star():
    #The special syntax *args in function definitions in python is used to pass a variable number of arguments to a 
    #function. It is used to pass a non-key worded, variable-length argument list. 
    #For example : we want to make a multiply function that takes any number of arguments and able to multiply them
    #all together. It can be done using *args.
    name=request.args.get("name")
    star_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data":star_data,
        "message":"It's a success"
    }),200

if __name__=="__main__":
    app.run()