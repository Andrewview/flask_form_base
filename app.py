from flask import Flask, render_template, session, redirect, request
from flask_sqlalchemy import SQLAlchemy
# pip install flask_sqlalchemy
# pip install pymysql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def indexView():
	if request.method == 'POST':
		return redirect('/login_success')

	else:
		return render_template('index.html')


@app.route('/login_success')
def successView():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')