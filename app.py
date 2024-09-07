from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from main import get_account_balance, get_transactions
from datetime import datetime


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    address = request.json['address']
    balance = get_account_balance(address)
    transactions = get_transactions(address)
    
    formatted_transactions = []
    for tx in transactions:
        timestamp = datetime.fromtimestamp(int(tx['timeStamp']))
        value_eth = int(tx['value']) / (10 ** 18)
        formatted_transactions.append({
            'date': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'from': tx['from'],
            'to': tx['to'],
            'value': f"{value_eth:.4f} ETH"
        })
    
    return jsonify({
        'address': address,
        'balance': f"{balance:.4f} ETH",
        'transactions': formatted_transactions
    })

if __name__ == '__main__':
    app.run(debug=True)