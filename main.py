from flask import Flask
import datetime

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def portfolioPage():
  page = f"""
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Max's Portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />


</head>

  <body>
  <h1>Max's Portfolio</h1>
  <h2>Day 72 Solution</h2>
  <p>This is a solution to the replit challenge for day 72.  It is a program that allows you to add a user and their password to a database for a private Diary.  It is also possible to view the database, and also delete users.</p>
  <a href = "https://replit.com/@getubamax/Day72100Days#main.py"><img src="static/images/day72.png" width = "50%"></a>
<p><a href = "/linktree">Go to my linktree</a></p>

  <script src="script.js"></script>


</body>

</html>"""
  return page

@app.route('/linktree') 
def linktree(): 
  today = datetime.date.today()
  page = f"""
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style1.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src="static/images/Max_Getuba_headshot.jpg" width = "200px" height = "200px">
  <h1>Max Getuba</h1>
  <h2>About Me</h2>
  <h3>Date:{today}</h3>
  <p>A legendary thinker, innovator and founder who's on a mission to elevate the culture of enterprise in Afica for a brighter, more prosperous Africa </p>
  <h2>My Work</h2>
  <p>I am a founder of <a href="https://theimpactfulcapitalist.substack.com/"> The Impactful Capitalists movement </p>
  <h2>Contact Me</h2>
  <p>Email: maxgetuba@gmail.com</p>
  <p>Phone: +254708793485</p>
  <script src="script.js"></script>
  
  

 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
  
</body>

</html> """
  # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
