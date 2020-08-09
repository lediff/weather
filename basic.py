from flask import Flask, render_template
#import logging as logger
#logger.basicConfig(level="DEBUG")
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('basic.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')