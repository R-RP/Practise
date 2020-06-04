from flask import Flask,render_template, url_for, request, redirect
import csv
app = Flask(__name__)

def write_file(data):
	with open ('database.txt',mode='a',newline='') as fh:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]	
		file = fh.write(f'\n{email},{subject},{message}')	

def write_csv(data):
	with open('database.csv',mode='a') as csv_file:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(csv_file,delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/submit_form',methods=['POST','GET'])
def my_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_file(data)
			write_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'data not saved to database'	
	else:
		return 'something went wrong'	

@app.route('/<string:page_name>')
def my_html(page_name):
	return render_template(page_name)    

'''
@app.route('/index.html')
def my_home2():
	return render_template('index.html')

@app.route('/works.html')
def my_work():
	return render_template('works.html')


@app.route('/about.html')
def my_about():
	return render_template('about.html')        


@app.route('/contact.html')
def my_contact():
	return render_template('contact.html')


@app.route('/components.html')
def my_components():
	return render_template('components.html')
	'''