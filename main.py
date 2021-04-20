from flask import Flask ,jsonify , request ,session,render_template ,redirect,render_template_string,make_response
import pandas as pd
app = Flask(__name__)

# @app.route('/' ,  methods=["GET"])
# def hello_world():

#     return redirect("/new")

@app.route('/' ,  methods=["POST","GET"])
def test1():
    error = None
    username = None
    password = None
    gender = None
    Card_cate = None

    try :

        if request.form and request.method == 'POST':
            username = request.form['input1']
            password = request.form['input2']

            ####################################

            Cus_num = request.form['Cus_num']
            Cus_age = request.form['Cus_age']
            gender = request.form['gender']
            Dep_num = request.form['Dep_num']
            Cus_edu = request.form['Cus_edu']
            Marital_sta = request.form['Marital_sta']
            Inc_cate = request.form['Inc_cate']
            Card_cate = request.form['Card_cate']
            Month_ob = request.form['Month_ob']
            Total_Relationship_Count = request.form['Total_Relationship_Count']
            Months_Inactive_12_mon = request.form['Months_Inactive_12_mon']
            Contacts_Count_12_mon = request.form['Contacts_Count_12_mon']
            Total_Revolving_Bal = request.form['Total_Revolving_Bal']
            Avg_Open_To_Buy = request.form['Avg_Open_To_Buy']
            Total_Amt_Chng_Q4_Q1 = request.form['Total_Amt_Chng_Q4_Q1']
            Total_Trans_Amt = request.form['Total_Trans_Amt']
            Total_Trans_Ct = request.form['Total_Trans_Ct']
            Total_Ct_Chng_Q4_Q1 = request.form['Total_Ct_Chng_Q4_Q1']
            Avg_Utilization_Ratio = request.form['Avg_Utilization_Ratio']

            ####################################

            print("username : ", username)
            print("password : ", password)

            if username == '' or password == '' or gender == '' :
                error = True 
                print("!!!!!")

            

        return render_template('test.html' , error = error  ,username = username , password = password , show = True , gender = gender , Card_cate = Card_cate) 
    
    except Exception as e:
        #print("Error is : " , str(e))
        #return("Error is : " + str(e))
        return("กลับไปเลือกให้ครบไอ้เวร")

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', threaded=True, port=6969)

# structure python
#     MVC module view controller  component
#     OOP object orented programing component []