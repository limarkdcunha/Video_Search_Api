from flask import Flask,request,jsonify
from flask_cors import CORS
import search_values

app = Flask(__name__)
CORS(app)

@app.route('/videoname', methods=['GET'])
def give_search_results():
    res = search_values.results(request.args.get('title'))
    return jsonify(res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)
