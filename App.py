from flask import Flask,render_template
from flask import request as rq
import requests
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if rq.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer {KEY}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
    
        data = rq.form["data"]

        maxl = int(rq.form["maxl"])
        minl = maxl//4

        output = query({
        	"inputs": data,
        	"parameters":{"min_length":minl,"max_length":maxl},
        })

        f_output = output[0]["summary_text"]
        return render_template("index.html",result=f_output)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()