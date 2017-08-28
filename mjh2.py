from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mail import Mail, Message


app =Flask(__name__)
mail=Mail(app)
app.secret_key = "secret_key_123"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'marcus.mjh@gmail.com'
app.config['MAIL_PASSWORD'] = 'Grifter319412'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'marcus.mjh@gmail.com'
mail = Mail(app)


# THE INITIAL PAGE
@app.route("/")
def tasks ():
	return render_template('blank.html')


@app.route("/mail",methods=['GET', 'POST'])
def index():
   msg:str
   msghead:str
   info:str
   welcome:str
   anno:str
   msghtml:str

   # GET VALUES FROM FORM
   msgtemp=str(request.values.get("msgtemp"))
   msgto=request.values.get("sendto")
   msgtext=request.values.get("msgtext")

   # INFO
   infotitle=str(request.values.get("infotitle"))
   infomsgtext=str(request.values.get("infomsgtext"))

   # SYS
   systitle=str(request.values.get("systitle"))
   sysserver=str(request.values.get("sysserver"))
   sysdate=str(request.values.get("sysdate"))
   sysmsgtext=str(request.values.get("sysmsgtext"))


   msghead = """
   <head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>html title</title>
     <style type="text/css" media="screen">
       table{
           background-color: #AAD373;
           empty-cells:hide;
       }
       td.cell{
           background-color: white;
       }
     </style>
   </head>
   <body>
   <div style="width:600px;background-color:#ADD8E6;">
   """
   msgfoot = """
   </div>
   </body>
   """

   welcome = """
     <div style="justify-content:center;">
     <table style="border: blue 1px solid;">
       <tr><td class="cell">Cell 1.1</td><td class="cell">Cell 1.2</td></tr>
       <tr><td class="cell">Cell 2.1</td><td class="cell">"""+msgtext+"""</td></tr>
     </table>
	 </div>
   """
   info = """
    <h1 style="text-align:center;">"""+infotitle+"""</h1>
    """+infomsgtext+"""
  """
   anno = """
  <h1 style="text-align:center;">Medical Data Hub Announcement!</h1>
  <p>lorem est</p>
  """
   sys = """
   <div style="justify-content:center;">
    <h1 style="text-align:center;">"""+systitle+"""</h1>
     <table style="border: blue 1px solid;">
       <tr><td class="cell">Maintainence date :</td><td class="cell">"""+sysdate+"""</td></tr>
       <tr><td class="cell">Affected system</td><td class="cell">"""+sysserver+"""</td></tr>
     </table>
	<p>"""+sysmsgtext+"""</div>"""

  # LETS TRY AN IF
   if msgtemp == 'welcome':
      msghtml = msghead+welcome+msgfoot
   else:
      if msgtemp == 'anno':
         msghtml = msghead+anno+msgfoot
      else:
	      if msgtemp == 'sys':
	         msghtml = msghead+sys+msgfoot
	      else:
	         msghtml = msghead+info+msgfoot

   # msghtml = str(msghead+request.values.get("msgtemp"))

   # msg = Message('Hello ', html=msgtype,sender = 'marcus.mjh@gmail.com', recipients = ['marcus.mjh@gmail.com'])
   msg = Message('Hello', html=msghtml, recipients = [msgto])
   mail.send(msg)

   return render_template('blank.html')

if __name__ == '__main__':
   app.run(debug = True)
