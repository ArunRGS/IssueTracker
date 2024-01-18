from flask import Flask, request,render_template
import ibm_db
import re
app=Flask(__name__)

con=ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PORT=31249;UID=szb49837;PWD=JOitxOz3geo8wXFY;", "", "")
##2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud
                                            ##6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30376
##b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud
print("DB Connected")

@app.route('/')
def home():
    return render_template('login.html')
@app.route('/registration')
def home1():
    return render_template('registration.html')

@app.route('/registration',methods=['POST','GET'])
def registration():
    username=request.form['username']
    Password=request.form['Password']

    sql = "SELECT * FROM REGISTRATION WHERE USERNAME=?"
    smtp = ibm_db.prepare(con, sql)
    ibm_db.bind_param(smtp, 1, username)
    ibm_db.execute(smtp)
    account = ibm_db.fetch_assoc(smtp)
    if account:
        return render_template('registration.html', output="Sorry!!! Already This User Id Exists")
    if not re.match(r'[^@]+@[^@]+\.[^@]+', username):
        return render_template('registration.html',output="Invalid Email Address")

    else:
        sql="INSERT INTO REGISTRATION VALUES (?,?)"
        prepSql=ibm_db.prepare(con,sql)
        ibm_db.bind_param(prepSql, 1, username)
        ibm_db.bind_param(prepSql, 2, Password)
        ibm_db.execute(prepSql)
        return render_template('registration.html',output='You have successfully created an account and use this credentials for login')

@app.route('/login',methods=['POST','GET'])
def login():
    username=request.form['username']
##    Password=request.form['Password']
    sql = "SELECT * FROM REGISTRATION WHERE USERNAME=?"
    smtp = ibm_db.prepare(con ,sql)
    ibm_db.bind_param(smtp, 1, username)
##    ibm_db.bind_param(smtp, 2, Password)
    ibm_db.execute(smtp)
    account=ibm_db.fetch_assoc(smtp)
    if account:
        return render_template('login.html',output="Login Successfully")
    else:
        return render_template('login.html',output="This User Id is  not Registered")
if __name__=='__main__':
    app.run(debug=True)