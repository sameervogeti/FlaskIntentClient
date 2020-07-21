from flask import Flask,render_template,url_for,request
from ResultTest import getPrediction


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		my_prediction = getPrediction(data)
		print("Result we got from Backend is :"+str(my_prediction))
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)