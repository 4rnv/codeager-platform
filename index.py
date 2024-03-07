from flask import Flask, render_template, jsonify, request, redirect, url_for

#Use tailwind CDN for the css stuff
#Add image and quote for each question, mayb use tuple

app = Flask(__name__)

questions = ["What is the capital of France?",
        "What is 2 + 2?",
        "What is the largest mammal?",
        "What planet is known as the Red Planet?",
        "What is the chemical symbol for gold?",
        "Who wrote 'To Kill a Mockingbird'?",
        "What is the hardest natural substance on Earth?",
        "What is the capital of Italy?"
]

answers=["Paris", "4", "Blue whale", "Mars", "Au", "Harper Lee", "Diamond", "Rome"]

q_no = 1

@app.route("/")
def index():
  return render_template('index.html', question= q_no)

@app.route("/chapter/<q_no>/")
def q(q_no):
   q_no = int(q_no)
   if q_no >= 0:
      array_index = int(q_no) -1
      return render_template('q.html', question= questions[array_index], form_link = q_no)
   else:
      return redirect("/", code=302)

@app.route("/chapter/0/", methods=["GET"])
def redirect_internal():
    return redirect("/", code=302)

@app.route('/chapter/<q_no>/submit', methods=['POST'])
def check_ans(q_no):
   array_index = int(q_no) - 1
   user_answer= request.form['answer'].strip()
   if (user_answer.lower() == answers[array_index].lower()):
      if array_index >= 7:
         return render_template('result.html', bane = 'Congratulations! You have completed the challenge', cia = 0, link_msg = 'Go home')
      else:
        return render_template('result.html', bane = 'Congratulations! That is the correct answer', cia = int(q_no)+1, link_msg = 'Continue your story')
   else:
      return render_template('result.html', bane = 'Too bad! You\'ve failed', cia = int(q_no), link_msg = 'Try again')

@app.route('/credits/')
def credits():
   return render_template('credits.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)