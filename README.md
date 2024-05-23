<div align="center">
  <h1>Flask Razorpay Integration</h1> 
</div>
<p>This is a simple Flask application that demonstrates how to integrate the Razorpay payment gateway, focusing on recurring payments. The backend is developed using Python-Flask and PostgreSQL, utilizing the Razorpay Python module..</p>

## Features

- Integration with Razorpay payment gateway.
- Support for recurring payments.
- API endpoints for handling various payment operations
- Integration with Razorpay payment gateway
- PostgreSQL as the database

## Installation
1. Clone the repository
```
  git clone https://github.com/Muhammad-Shafaf123/Python-Flask-Razorpay-Integration.git
```
2. Install the dependencies
```
  pip install -r requirements.txt
```
3. Set up PostgreSQL database.
   
Create a new PostgreSQL database and note down the database name, username, and password.

4. Configure environment variables.


Copy the `.env.sample` file to create your `.env` file:
```
  cp .env.sample .env
```

Edit the .env file with your configuration.

5. Initialize the database
```
 flask db upgrade
```
6. Run the application
```
 flask --app app.py run
```

## Contribution

Ways to contribute:

- Suggest a feature
- Report a bug
- Fix something and open a pull request
- Help me document the code
- Spread the word
- Find something I missed which leaves any trace!
 
