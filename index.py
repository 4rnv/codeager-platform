from flask import Flask, render_template, request, redirect

#Use tailwind CDN for the css stuff

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

quote_img = [('\"A is A, but sometimes, A is G.\"','1.png'),
             ('\"Late late says the White Rabbit.\"','2.png'),
             ('Somewhere, Under a Starry Sky.','3.png'),
             ('Old Home','4.png'),
             ('The Leaning Tower of Babel','5.png'),
             ('Arrakis','6.png'),
             ('...','7.png'),
             ('Decretum','8.png')]

q_no = 1

@app.route("/")
def index():
  return render_template('index.html', question= q_no)

@app.route("/chapter/<q_no>/")
def q(q_no):
   q_no = int(q_no)
   array_index = int(q_no) -1
   quote_ani_image = quote_img[array_index]
   x = '/static/images/'
   if q_no >= 0:
      return render_template('q.html', episode=q_no, question= questions[array_index], form_link = q_no, quote = quote_ani_image[0], image= x+quote_ani_image[1])
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
         return render_template('result.html', ans_feedback = 'Congratulations! You have completed the challenge', question_pointer = 0, link_msg = 'Go home')
      else:
        return render_template('result.html', ans_feedback = 'Congratulations! That is the correct answer', question_pointer = int(q_no)+1, link_msg = 'Continue your story')
   else:
      return render_template('result.html', ans_feedback = 'Too bad! You\'ve failed', question_pointer = int(q_no), link_msg = 'Try again')

@app.route('/credits/')
def credits():
   return render_template('credits.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)