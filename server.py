from flask import Flask, render_template, redirect, session, request
import random

app= Flask(__name__)
app.secret_key="it's a secret"

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    
    jobs = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,50)
    }
    return render_template('index.html', jobs = jobs)

@app.route('/process_money')
def process():
    
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)