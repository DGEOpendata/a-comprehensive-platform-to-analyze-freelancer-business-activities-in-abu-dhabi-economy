python
import pandas as pd
import json
from flask import Flask, jsonify, request

# Initialize Flask App
app = Flask(__name__)

# Load Dataset
data = pd.read_excel('Freelancer_Business_Activities_AbuDhabi.xlsx')
data.fillna('', inplace=True)  # Replace NaN with empty strings

# Convert to JSON
data_json = data.to_dict(orient='records')

@app.route('/api/freelancers', methods=['GET'])
def get_freelancers():
    """Endpoint to retrieve all freelancer activities."""
    return jsonify(data_json)

@app.route('/api/freelancers/search', methods=['GET'])
def search_freelancers():
    """Endpoint to search freelancer activities by keyword."""
    keyword = request.args.get('q', '').lower()
    if not keyword:
        return jsonify({'error': 'Query parameter q is required'}), 400

    results = [record for record in data_json if keyword in record['English Name'].lower() or keyword in record['Arabic Name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
