import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template,request,redirect
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route("/")
def nav():
    return render_template("index.html")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/handel_data",methods=["POST"])
def handel_data():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    ethnicity = request.form.get("ethnicity")
    autism = request.form.get("autism")
    jaundice = request.form.get("jaundice")
    a1 = request.form.get("a1")
    a2 = request.form.get("a2")
    a3 = request.form.get("a3")
    a4 = request.form.get("a4")
    a5 = request.form.get("a5")
    a6 = request.form.get("a6")
    a7 = request.form.get("a7")
    a8 = request.form.get("a8")
    a9 = request.form.get("a9")
    a10 = request.form.get("a10")
    asum = int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)+int(a7)+int(a8)+int(a9)+int(a10)
    asm = (asum/10)*100
    if int(age) >= 18:
        file_1 = open("adult_model.pkl","rb")
        gbc = pickle.load(file_1)
        file_1.close()
    else:
        file_2 = open("child_model.pkl","rb")
        gbc = pickle.load(file_2)
        file_2.close()
    ar = np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,age,gender,ethnicity,jaundice,autism]).reshape(1,15)
    frs = gbc.predict(ar)
    fr = frs[0]
    autism = "No" if int(autism) == "0" else "Yes"
    jaundice = "Yes" if jaundice == "0" else "No"
    fr = "Negative" if frs == 0 else "Positive"
    gender = "Female" if gender == "0" else "Male"
    if ethnicity == "0":
        ethnicity = "White European"
    elif ethnicity == "1":
        ethnicity = "Asian"
    elif ethnicity == "2":
        ethnicity = "Middle Eastern"
    elif ethnicity == "3":
        ethnicity = "Black"
    elif ethnicity == "4":
        ethnicity = "South Asian"
    elif ethnicity == "5":
        ethnicity = "Pasifika"
    elif ethnicity == 6:
        ethnicity = "Latino"
    elif ethnicity == "7":
        ethnicity = "Hispanic"
    else:
        ethnicity = "Others"
    l = {"name":name,"age":age,"gender":gender,"ethnicity":ethnicity,"autism":autism,"a1":a1,"a2":a2,"a3":a3,"a7":a7,"a8":a8,"a9":a9,"a10":a10,"asm":asm,"jaundice":jaundice,"fr":fr,"pl":"Assesment Report","a4":a4,"a5":a5,"a6":a6}
    return render_template("result.html",l=l)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    l = {"name":"None","age":"None","gender":"None","ethnicity":"None","autism":"None","a1":"None","a2":"None","a3":"None","a4":"None","a5":"None","a6":"None","a7":"None","a8":"None","a9":"None","a10":"None","asm":"None","jaundice":"None","fr":"None","pl":"Please take the test to get your results"}
    return render_template("result.html",l=l)
@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)