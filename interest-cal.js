<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interest Calculator</title>
    <script>
        function calculateInterest() {
            const amount = document.getElementById('amount').value;
            const rate = document.getElementById('rate').value;
            const months = document.getElementById('months').value;

            fetch(`https://financeinterestcalculator-80f194934066.herokuapp.com/api/calculate-interest?amount=${amount}&rate=${rate}&months=${months}`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('result').innerText = `Error: ${data.error}`;
                    } else {
                        document.getElementById('result').innerText = `Interest: ${data.interest}`;
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('result').innerText = 'An error occurred';
                });
        }
    </script>
</head>
<body>
    <h1>Interest Calculator</h1>
    <label for="amount">Amount:</label>
    <input type="text" id="amount"><br>
    <label for="rate">Rate:</label>
    <input type="text" id="rate"><br>
    <label for="months">Months:</label>
    <input type="text" id="months"><br>
    <button onclick="calculateInterest()">Calculate</button>
    <p id="result"></p>
</body>
</html>
