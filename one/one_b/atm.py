# 1b. Python and JavaScript - ATM Application: Design a HTML form that displays user’s
# current balance, an input field to enter amount and buttons to withdraw or deposit money.
# Validate the form such that negative amount cannot be entered and Users cannot withdraw 
# more than 5000 at one time. The maximum number of transactions  is 5.

from flask import *


app =Flask(__name__)

app.secret_key ="secret"

@app.route('/', methods = ['GET','POST'])
def aatm():

     try:
          b = session["b"]
     except KeyError:
          b = session["b"] = 8000

     if request.method == "GET":
          return render_template("aatm.html",msg="",balance=b)

     if request.method =="POST":
          if request.form["action"] == 'Withdraw':
               if int(request.form["amount"]) > session["b"]:
                    return render_template("aatm.html",msg="Cannot withdraw amount greater than balance",balance=b)
               
               elif int(request.form["amount"]) > 5000:
                    return render_template("aatm.html",msg="Cannot withdrow amount greater than 5000",balance=b)

               else:
                    b = b - int(request.form["amount"])
                    session["b"] = b
                    return render_template("aatm.html",msg="withdraw successfully",balance=b)

          elif request.form["action"] == "Deposit" :
               if int(request.form["amount"]) >10000 :
                    return render_template("aatm.html",msg="can npt deposit more than 10000",balance=b)
               else:
                    b = b + int(request.form["amount"])
                    session["b"] = b
                    return render_template("aatm.html",msg="deposit successfully",balance=b)

if __name__ == '__main__':
     app.run(host="localhost" , port= 7000)
