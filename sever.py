from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)



@app.route("/submit_form", methods=['POST','GET'])
def submit_page():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return 'sent with successful'
        except:
            return 'not sent successful'
    else:
        return 'Message not sent successfully, please try again later'
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name=data["name"]
        email = data["email"]
        msg=data["message"]
        file= database.write(f'\n{email},{name},{msg}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name= data["name"]
        email = data["email"]
        msg= data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, msg])