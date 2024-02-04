from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/GetNextBirthday/<dateOfBirth>', methods=['GET'])
def get_next_birthday(dateOfBirth):
    # Validate date format using regex
    if not re.match(r"^\d{4}-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$", dateOfBirth):
        return jsonify({"error": "Invalid date format and Date format Should be YYYY-MM-DD"}), 400

    # Convert the string to a datetime object
    dob = datetime.strptime(dateOfBirth, '%Y-%m-%d')

    # Determine the next birthday
    today = datetime.now()
    next_birthday_year = today.year if today.month < dob.month or (
                today.month == dob.month and today.day < dob.day) else today.year + 1
    next_birthday = dob.replace(year=next_birthday_year)

    # Return the result
    return jsonify({"NextBirthday": next_birthday.strftime('%Y-%m-%d')})


if __name__ == '__main__':
    app.run(debug=True)

