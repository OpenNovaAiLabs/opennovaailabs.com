from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/calculate-interest', methods=['GET'])
def calculate_interest():
    try:
        amount = float(request.args.get('amount'))
        rate = float(request.args.get('rate'))
        months = int(request.args.get('months'))
        interest = (amount * rate * months) / (100 * 12)
        return jsonify({"interest": round(interest, 2)})
    except TypeError:
        return jsonify({"error": "Invalid input or missing parameters"}), 400
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
