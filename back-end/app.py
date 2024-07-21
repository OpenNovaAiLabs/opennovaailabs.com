from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/calculate-interest', methods=['POST'])
def calculate_interest():
    data = request.json
    try:
        amount = float(data['amount'])
        rate = float(data['rate'])
        months = int(data['months'])
        interest = (amount * rate * months) / (100 * 12)
        return jsonify({"interest": round(interest, 2)})
    except KeyError:
        return jsonify({"error": "Missing required parameters"}), 400
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run()
