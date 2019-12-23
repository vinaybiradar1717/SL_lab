# 10b. Python and JavaScript – Student Registration: Design a HTML form that displays 
#     • Two text fields to input the user’s USN and Date of Birth.
#     • Three text boxes to input three marks. 
# Validate the data entry on the server side using Javascript so that null values are not accepted for all the five text boxes. Validate the entry on server-side using Python to ensure that USN is accepted in a proper pattern as well as date validations are done. 
# Calculate the average using Python on server-side and display the result.

from flask import *
import re 

app = Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def index():
     if request.method == "GET":
	
	     return render_template("index.html",msg="hello user enter your details")

     if request.method == "POST":
          if not re.match("^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$",request.form["usn"]):
               return render_template("index.html",msg="***USN format invalid***")

          avg = (int(request.form['m1'])+int(request.form['m2'])+int(request.form['m3']))/3.0
          return render_template("index.html",msg="student avrage marks :"+str(round(avg,3)) )

if __name__ =='__main__':
     app.run()
