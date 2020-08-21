from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode="a") as database:
  	email = data["email"]
  	subject = data["subject"]
  	message = data["message"]
  	file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
  with open('database.csv', newline='' , mode="a") as database2:
  	Email = data["Email"]
  	Name = data["Name"]
  	Message = data["Message"]
  	csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  	csv_writer.writerow([Email, Name, Message])


@app.route('/submit_form', methods=['POST', 'GET']) 
def submit_form():
    if request.method == 'POST':
      data = request.form.to_dict()
      write_to_csv(data)
      print(data)
      return redirect('/thanks.html')
      return 'form submite'
    else:
      return 'try again'