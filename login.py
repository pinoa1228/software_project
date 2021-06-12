
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['nm'] == '박연수' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('login'))

@app.route('/success')
def success():
   return render_template('diarylist.html')



   
if __name__ == '__main__':
   app.run(debug = True)


