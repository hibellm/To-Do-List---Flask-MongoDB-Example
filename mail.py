from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)
app.secret_key = "secret_key_123878678"
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
   basic:str
   advanced:str
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

   # BASIC
   basiclocation=str(request.values.get("basiclocation"))
   basicdate=str(request.values.get("basicdate"))

   # ADVANCED
   advancedlocation=str(request.values.get("advancedlocation"))
   advanceddate=str(request.values.get("advanceddate"))

   msghead = """
   <head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>html title</title>
     <style type="text/css" media="screen">
	   #divbody{
	        width:800px;
	   		background-color: #432422;
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

   welcome = """
<div style="width:601px;margin-left:100px;height:850px;position:relative;font-family:Roboto;font-size:medium;">

 <div style="text-align:center;width:auto;height:auto;position:relative;">
    <!--img border="0" src="https://sites.google.com/a/roche.com/mdh-portal/_/rsrc/1489652167705/home/Capture3.PNG" style="width:100%"-->
    <img border="0" src="https://www.dropbox.com/s/g3jevj4oksmii9q/banner.jpg?dl=0" style="width:100%">
 </div>
 <div style="text-align:center;width:auto;height:auto;position:relative;font-family:Roboto;">

  <h1>Welcome to the Medical Data Hub</h1>
  <span>
  <a target="_blank" href="https://calendar.google.com/calendar/event?action=TEMPLATE&amp;tmeid=NG42MGgzcmRlOTZsbTNjZ3JodnBmdGVpMGsgbWFyY3VzLmhpYmVsbEByb2NoZS5jb20&amp;tmsrc=marcus.hibell%40roche.com">
  <img border="0" src="https://www.google.com/calendar/images/ext/gc_button1_en-GB.gif">
  </a>
  </span>
  <p>We are looking forward to your attendance at the MDH Basics Instructor-Led course on [ENTER DATE AND TIME].  Here are the pre-requisite activities:</p>
  <h3>To do:</h3>
  <p>Complete the MDH Overview e-Learning: http://pdwebdev01.gene.com/groups/devo/multimedia/MDH_Overview/story.html (optional, if you would like credit in your learning management system please bring a screen shot or printout of the summary page to class)</p>
  <h3>Reminder:</h3>
  <ul style="text-align:left;"><li>Bring your laptop and power cord to class (mandatory)</li>
                               <li>This is a <strong>Face-to-Face class</strong>, no WebEx will be provided</li>
                               <li>Meals and snacks are to be provided</li>
  </ul>
  <p>Attached is the participant guide for the course.  Feel free to look through it and bring any questions you have to the session!</p>
  <p>Please complete the actions above as soon as you can.
  <p>See you on [ENTER DAY].
  <p>Regards,<br>Medical Data Hub<br>
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

   basic = """
<div style="width:601px;margin-left:100px;height:800px;position:relative;font-family:Roboto;font-size:medium;">

 <div style="text-align:center;width:auto;height:auto;position:relative;">
    <!--img border="0" src="https://sites.google.com/a/roche.com/mdh-portal/_/rsrc/1489652167705/home/Capture3.PNG" style="width:100%"-->
    <img border="0" src="https://www.dropbox.com/s/g3jevj4oksmii9q/banner.jpg?dl=0" style="width:100%">
 </div>
 <div style="text-align:center;width:auto;height:auto;position:relative;font-family:Roboto;">

  <h1>Hello Medical Data Hub <br>Basics ILT Learners</h1>
  <span>
  <a target="_blank" href="https://calendar.google.com/calendar/event?action=TEMPLATE&amp;tmeid=NG42MGgzcmRlOTZsbTNjZ3JodnBmdGVpMGsgbWFyY3VzLmhpYmVsbEByb2NoZS5jb20&amp;tmsrc=marcus.hibell%40roche.com">
  <img border="0" src="https://www.google.com/calendar/images/ext/gc_button1_en-GB.gif">
  </a>
  </span>
  <table id="tableb">
	<tr><td class="cell">When?</td><td class="cell">"""+basicdate+"""</td></tr>
	<tr><td class="cell">Where?</td><td class="cell">"""+basiclocation+"""</td></tr>
  </table>
  <p>We are looking forward to your attendance at the MDH Basics Instructor-Led course.<br>Here are the pre-requisite activities:</p>
  <h3>To do:</h3>
  <p>Complete the MDH Overview e-Learning: http://pdwebdev01.gene.com/groups/devo/multimedia/MDH_Overview/story.html <br>(optional, if you would like credit in your learning management system please bring a screen shot or printout of the summary page to class)</p>
  <h3>Reminder:</h3>
  <ul style="text-align:left;"><li>Bring your laptop and power cord to class (mandatory)</li>
                               <li>This is a <strong>Face-to-Face class</strong>, no WebEx will be provided</li>
                               <li>Meals and snacks to be provided</li>
  </ul>
  <p>Attached is the participant guide for the course. Feel free to look through it and bring any questions you have to the session!</p>
  <p>Please complete the actions above as soon as you can.
  <p>See you on <strong>"""+basicdate+"""</strong>.
  <p>Regards,</p><h3 id="mdhsig">Medical Data Hub</h3><br>
   """
   advanced = """
  <div style="width:601px;margin-left:100px;height:850px;position:relative;font-family:Roboto;font-size:medium;">

  <div style="text-align:center;width:auto;height:auto;position:relative;">
    <!--img border="0" src="https://sites.google.com/a/roche.com/mdh-portal/_/rsrc/1489652167705/home/Capture3.PNG" style="width:100%"-->
    <img border="0" src="https://www.dropbox.com/s/g3jevj4oksmii9q/banner.jpg?dl=0" style="width:100%">
  </div>
  <div style="text-align:center;width:auto;height:auto;position:relative;font-family:Roboto;">

  <h1>Hello Medical Data Hub<br>Advanced ILT Learners</h1>
  <span>
  <a target="_blank" href="https://calendar.google.com/calendar/event?action=TEMPLATE&amp;tmeid=NG42MGgzcmRlOTZsbTNjZ3JodnBmdGVpMGsgbWFyY3VzLmhpYmVsbEByb2NoZS5jb20&amp;tmsrc=marcus.hibell%40roche.com">
    <img border="0" src="https://www.google.com/calendar/images/ext/gc_button1_en-GB.gif">
  </a>
  </span>
  <p>We are looking forward to your attendance at the MDH Advanced Instructor-Led course.  Here are the pre-requisite activities:</p>
  <h3>To do:</h3>
  <p>Complete the MDH Overview e-Learning: http://pdwebdev01.gene.com/groups/devo/multimedia/MDH_Overview/story.html (optional, if you would like credit in your learning management system please bring a screen shot or printout of the summary page to class)</p>
  <h3>Reminder:</h3>
  <ul style="text-align:left;"><li>Bring your laptop and power cord to class (mandatory)</li>
                               <li>This is a <strong>Face-to-Face class</strong>, no WebEx will be provided</li>
                               <li>Meals and snacks are to be provided</li>
  </ul>
  <p>Attached is the participant guide for the course.  Feel free to look through it and bring any questions you have to the session!</p>
  <p>Please complete the actions above as soon as you can.
  <p>See you on <strong>"""+advanceddate+"""</strong>.
  <p>Regards,</p><h3 id="mdhsig">Medical Data Hub</h3><br>
   </div>
   """




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
		      if msgtemp == 'basic':
		         msghtml = msghead+basic+msgfoot
		      else:
			      if msgtemp == 'advanced':
			         msghtml = msghead+advanced+msgfoot
			      else:
			         msghtml = msghead+info+msgfoot

   # msghtml = str(msghead+request.values.get("msgtemp"))

   # msg = Message('Hello ', html=msgtype,sender = 'marcus.mjh@gmail.com', recipients = ['marcus.mjh@gmail.com'])
   msg = Message('Hello', html=msghtml, recipients = [msgto])
   mail.send(msg)

   return render_template('blank.html')

if __name__ == '__main__':
   app.run(debug = True)
