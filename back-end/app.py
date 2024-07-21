from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/calculate-interest', methods=['POST'])
def calculate_interest():
    data = request.json
    try:
        # Get parameters from request
        amount = float(data['amount'])
        rate = float(data['rate'])
        months = int(data['months'])
        
        # Calculate interest
        interest = (amount * rate * months) / (100 * 12)
        
        # Return the result as JSON
        return jsonify({"interest": round(interest, 2)})
    except KeyError:
        return jsonify({"error": "Missing required parameters"}), 400
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

# Gunicorn will use this to find the application
# Make sure your app object is named `app`
