from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)
app.secret_key = "secret_key_987123"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'marcus.mjh@gmail.com'
app.config['MAIL_PASSWORD'] = 'Grifter319412'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'marcus.mjh@gmail.com'
mail = Mail(app)


# THE INITIAL PAGE
@app.route("/", methods=['GET', 'POST'])

def tasks ():
    try:
        ruok = request.form['RUok']
    except Exception as e:
        return(str(e))
        return render_template('ru.html')


@app.route("/mail",methods=['GET', 'POST'])
def index():
   msg:str
   msghead:str
   info:str
   cprd:str
   anno:str
   basic:str
   advanced:str
   msghtml:str

   # GET VALUES FROM FORM
   msgtemp=str(request.values.get("msgtemp"))
   ruok=str(request.values.get("RUok"))

   msghead = """
   <head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>html title</title>
     <style type="text/css" media="screen">
	   #divbody{
	        width:800px;
	   		background-color: #f32422;
			font-family:Roboto;
	   }
       table{
           empty-cells:hide;
       }
	   #tableb{
		    margin: auto;
		    width: 50%;
		    border: none;
		    padding: 10px;
	   }
       td.cell{
           background-color: white;
       }
	   p,h3{
	   text-align:left;
	   }
     </style>
   </head>
   <body>
   <div id="divbody">
   """

   msgfoot = """
	 <div style="text-align:center">
	  <img height="16px" src="https://sites.google.com/a/roche.com/mdh-portal/_/rsrc/1488288449176/home/feedback.png?height=16px" style="color:rgb(51,51,51);font-family:Arial,Verdana,sans-serif;font-size:small;text-align:center;background-color:rgb(255,255,255)">
	  <span style="color:rgb(51,51,51);font-family:Arial,Verdana,sans-serif;font-size:small;text-align:center;background-color:rgb(255,255,255)">&nbsp;Have a suggestion on how to improve this website?&nbsp;</span>
	  <a href="https://docs.google.com/forms/d/1XRW_WQa_nUlMQ_Y4G_F0VJ6pxkW-Hnl8kxqCi5e1bvk/edit" style="color:rgb(51,102,153);font-family:Arial,Verdana,sans-serif;font-size:small;text-align:center;background-color:rgb(255,255,255)">Please share your feedback and recommendations!</a>
	 </div>
   </div>
   </body>
   """

   cprd = """
  <div style="width:601px;margin-left:100px;height:850px;position:relative;font-family:Roboto;font-size:medium;">
  <h1>Please grant me access to CPRD</h1>
  </div>
   """

  # LETS TRY AN IF
   if msgtemp == 'cprd':
      msghtml = msghead+cprd+ruok+msgfoot
   else:
      if msgtemp == 'anno':
         msghtml = msghead+anno+msgfoot
      else:
	      if msgtemp == 'sys':
	         msghtml = msghead+sys+msgfoot
	      else:
		      if msgtemp == 'basic':
		         msghtml = msghead+basic+msgfoot
		      else:
			      if msgtemp == 'advanced':
			         msghtml = msghead+advanced+msgfoot
			      else:
			         msghtml = msghead+info+msgfoot

   # msghtml = str(msghead+request.values.get("msgtemp"))

   # msg = Message('Hello ', html=msgtype,sender = 'marcus.mjh@gmail.com', recipients = ['marcus.mjh@gmail.com'])
   msg = Message('Hello', html=msghtml, recipients = ['marcus.mjh@gmail.com'])
   mail.send(msg)

   return render_template('ru.html')

if __name__ == '__main__':
   app.run(debug = True)
