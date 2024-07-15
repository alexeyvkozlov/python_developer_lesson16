#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\python_developer_lesson16
# cd d:\python_developer\python_developer_lesson16
#~~~~~~~~~~~~~~~~~~~~~~~~
# python main.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template, request

from hh_json import parce

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ объявление главной переменной
app = Flask(__name__)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ вывод (рендеринг) главной страницы
@app.get('/index')
@app.get('/')
def index():
  return render_template('index.html')


#~ вывод страницы формы
@app.route('/form/')
def form():
  return render_template('form.html')


@app.post('/result/')
def result():
  """
  Вывод результата обработки запроса
  :return: страница с результатами
  """
  vac = request.form
  data = parce(**vac)
  dat = {**data, **vac}  # data | vac - в Python 3.10 можно сделать так
  print(dat)
  return render_template('about.html', res=dat)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~ запуск
if __name__ == "__main__":
  app.run(debug=True)