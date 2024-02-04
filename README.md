# Next Birthday API

This Flask application provides a simple API to calculate the next birthday based on a given date of birth.

## Features

- Validates input date format (YYYY-MM-DD).
- Calculates the next birthday date.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have to install Python 3.x Version

## Installing Next Birthday API

To install Next Birthday API, follow these steps:

Linux and macOS:

```bash
git clone https://github.com/yourusername/next-birthday-api.git
cd next-birthday-api
python3 -m venv venv
source venv/bin/activate
pip install flask
```

Windows: 

```bash
git clone https://github.com/yourusername/next-birthday-api.git
cd next-birthday-api
python -m venv venv
venv\Scripts\activate
pip install flask
```

##  Using Next Birthday API

To use Next Birthday API, follow these steps:

```bash

flask run
Then, navigate to http://127.0.0.1:5000/GetNextBirthday/YYYY-MM-DD in your browser or API client.
Replace YYYY-MM-DD with the date of birth you want to query.

```
