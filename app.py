from try_1 import mydb
from flask import Flask,render_template,request,redirect, jsonify, Response
import json
import time
import random
app=Flask(__name__)


messages = []
  


@app.route("/")
def login():
    return render_template("signin.html")
@app.route("/page",methods=["POST","GET"])
def page():
    cursor=mydb.cursor(dictionary=True)
    email=request.form.get("email")
    password=request.form.get("password")
    var=[email,password]
    cursor.execute("select first_name from users where Email= %s and password= %s ",var)
    user=cursor.fetchone()
    mydb.commit()
    if user is not None:
        return render_template("page.html",fname=user["first_name"])
    else:
        return render_template("signinagain.html")
    
@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/page1",methods=["POST"])
def facepage():
    cursor=mydb.cursor(dictionary=True)
    email=request.form.get("email")
    password=request.form.get("password")
    fname=request.form.get("fname")
    sname=request.form.get("sname")
    date=request.form.get("date")
    phone1=request.form.get("phone1")
    phone2=request.form.get("phone2")
    if phone1.startswith("0"):
        phone1 = phone1[1:]

    if phone1.isdigit():
        phone1=int(phone1)
    else:
        return render_template("signupagain.html")
    
    if phone2 != '' :
        if phone2.startswith("0"):
            phone2 = phone2[1:]

        if phone2.isdigit():
            phone2=int(phone2)
        else:
            return render_template("signupagain.html")      
    else:
        userid=random.randint(100000,999999)
        var=[fname,sname,date,password,email,phone1,phone2,userid]
        var2=[email,password]
        cursor.execute("select first_name from users where Email= %s and password= %s ",var2)
        user=cursor.fetchone()
        if len(password)>64 or len(password)<8 :
            return render_template("signupagain.html")
        if user is None:
            cursor.execute("INSERT INTO `users` (first_name, last_name, DOB, password, Email, phone_1, phone_2, about,userId) values (%s,%s,DATE(%s),%s,%s,%s,%s,NULL,%s) ",var)
            mydb.commit()
            return render_template("page.html",fname=fname)
        else:
            return render_template("signupagain.html")
        
@app.route("/logout")
def logout():
    id=request.args.get("id")
    if id:
        return render_template("signin.html")
    else:
        return redirect("signin.html")
@app.route("/chat")    
def chatting():
    return render_template("chat.html")
# @app.route("/add")
# def add():
#     cursor=mydb.cursor()
#     title=request.args.get("post")
#     createdby=request.args.get("user")
#     postid=random.randint(10000,99999)
#     var=[createdby]
    # cursor.execute("select userId from users where first_name=%s "var)
    # user=cursor.fetchone()
    #var2=[postid,title,createdby]
    #cursor.execute("INSERT INTO `posts` (postid,title,createdby,date,likes) values (%i,%s,%s,NULL,NULL) ",var2)
    #mydb.commit()
    # return render_template("page.html",fname=createdby)
    




# @app.route("/send", methods=["POST"])
# def send():
#     message = request.json["message"]
#     sender = "User"
#     messages.append({"sender": sender, "text": message})
#     return jsonify({"status": "OK"})

# @app.route("/stream")
# def stream():
#     def generate():
#         last_event_id = int(time.time() * 1000)
#         while True:
#             if len(messages) > 0:
#                 for message in messages:
#                     event_id = int(time.time() * 1000)
#                     data = {"id": event_id, "data": message}
#                     yield f"id: {event_id}\ndata: {json.dumps(data)}\n\n"
#                 messages.clear()
#             time.sleep(1)
#     return Response(generate(), mimetype="text/event-stream")

# @app.route("/page.html",methods=["GET"]) 
# def addpost():

#     cursor=mydb.cursor()
#     titels=request.args.get("post")  
#     email=request.args.get("email")
#     var=[titels,email]
#     cursor.execute("insert into posts(titles,Email) values (%s,%s)",var)
#     return render_template("page.html")