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


@app.route("/mail")
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
   """

   welcome = """
   <body>
     <table style="border: blue 1px solid;">
       <tr><td class="cell">Cell 1.1</td><td class="cell">Cell 1.2</td></tr>
       <tr><td class="cell">Cell 2.1</td><td class="cell">"""+msgtext+"""</td></tr>
     </table>
   </body>
   """
   info = """
  <body>
    <h1>Teradata Information</h1>
    <p> We are happy to welcome you to </p>
<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
  <tr>
    <td>Ernst Handel</td>
    <td>Roland Mendel</td>
    <td>Austria</td>
  </tr>
  <tr>
    <td>Island Trading</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
  <tr>
    <td>Laughing Bacchus Winecellars</td>
    <td>Yoshi Tannamuri</td>
    <td>Canada</td>
  </tr>
  <tr>
    <td>Magazzini Alimentari Riuniti</td>
    <td>Giovanni Rovelli</td>
    <td>Italy</td>
  </tr>
</table>
  </body>
  """
   anno = """
  <body>
  <h1>Medical Data Hub Announcement!</h1>
  <p>lorem est</p>
  </body>
  """

  # LETS TRY AN IF

   if msgtemp == 'welcome':
      msghtml = msghead+welcome
   else:
      if msgtemp == 'anno':
          msghtml = msghead+anno
      else:
          msghtml = msghead+info

   # msghtml = str(msghead+request.values.get("msgtemp"))

   # msg = Message('Hello ', html=msgtype,sender = 'marcus.mjh@gmail.com', recipients = ['marcus.mjh@gmail.com'])
   msg = Message('Hello', html=msghtml, recipients = [msgto])
   mail.send(msg)
   # return "Sent"
   # flash('Email sent', 'success')
   return render_template('blank.html')

if __name__ == '__main__':
   app.run(debug = True)
