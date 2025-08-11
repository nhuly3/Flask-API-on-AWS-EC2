import os
import json
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    flash,
    jsonify
)

app = Flask(__name__)

DATA_FILE = "truckinglist.json"

def read_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return '''
        <h2>Trucking Company API</h2>
        <p>This is a RESTful API for managing trucking company data.</p>
        <p>Available endpoints:</p>
        <ul>
            <li>GET /companies</li>
            <li>GET /companies/&lt;name&gt;</li>
            <li>POST /companies</li>
            <li>PUT /companies/&lt;name&gt;</li>
            <li>DELETE /companies/&lt;name&gt;</li>
        </ul>
    '''

@app.route('/companies', methods=['GET'])
def get_all_companies():
    data = read_data()
    return jsonify(data)

@app.route('/companies/<string:name>', methods=['GET'])
def get_company(name):
    data = read_data()
    company = data.get(name)
    if company is None:
        return jsonify({'error': 'Company not found'}), 404
    return jsonify({name: company})

@app.route('/companies', methods=['POST'])
def add_company():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    new_company = request.get_json()
    if 'Company' not in new_company:
        return jsonify({'error': 'Missing "Company" field'}), 400
    name = new_company['Company']
    data = read_data()
    if name in data:
        return jsonify({'error': 'Company already exists'}), 400
    data[name] = new_company
    write_data(data)
    return jsonify({'message': f'Company {name} added'}), 201

@app.route('/companies/<string:name>', methods=['PUT'])
def update_company(name):
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    updates = request.get_json()
    data = read_data()
    if name not in data:
        return jsonify({'error': 'Company not found'}), 404
    data[name].update(updates)
    write_data(data)
    return jsonify({'message': f'Company {name} updated'})

@app.route('/companies/<string:name>', methods=['DELETE'])
def delete_company(name):
    data = read_data()
    if name not in data:
        return jsonify({'error': 'Company not found'}), 404
    del data[name]
    write_data(data)
    return jsonify({'message': f'Company {name} deleted'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)