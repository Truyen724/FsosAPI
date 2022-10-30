from flask import Flask, request
from flask_cors import CORS 
import json
app = Flask(__name__)
# CORS(app)
@app.route('/store',methods=['POST'])
def add_product():
    if request.method == 'POST':
        product = json.loads(request.data)
        print(type(product))
        print(product)
        return "hello"
if(__name__ == "__main__"):
    app.run(host = "0.0.0.0",debug=True)