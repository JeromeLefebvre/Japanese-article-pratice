from flask import Flask, render_template, request, Markup
import newspaper
import re 
from pykakasi_helper import convert, contains_kanji
from SM2 import Learnerdatabase

# Define a function to add Furigana to a given text
def add_furigana(text):
    L = Learnerdatabase()
    # Convert Japanese text to Hiragana using pykakasi
    hiragana_text = convert(text, all_fields=False, kanji_only=False)
    print(hiragana_text)
    txt = ''
    for replacement in hiragana_text:
        if contains_kanji(replacement['orig']):
            should_study = L.should_study(replacement['orig'])
            if should_study:
                txt += f"""<ruby>{replacement['orig']}<rt><input type="text" oninput="checkFurigana(this, '{replacement['hira']}')" /></rt></ruby>"""
            else:
                txt += replacement['orig']
        else:
            txt += replacement['orig']
    return txt

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    data = request.form.get('data')
    # Process the data here
    result = "Processed data: " + data
    return result

@app.route('/', methods=['POST'])
def parse_article():
    url = request.form['url']
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return render_template('index.html', article_text=Markup(add_furigana(article.text)))
 
if __name__ == '__main__':
    app.run(debug=True)
