from flask import Flask, render_template, request, Markup
import newspaper
 
import pykakasi
 
# Initialize pykakasi with options
kks = pykakasi.kakasi()
#kks.set_options(kakasi_no_defaults=True, mode='J', output_type='hiragana')
 
import re
 
# Define a regular expression pattern for Kanji characters
kanji_pattern = re.compile(r'[\u4e00-\u9faf]')
 
# Define a function to check if a given string contains any Kanji characters
def contains_kanji(text):
    return bool(kanji_pattern.search(text))
 
# Define a function to add Furigana to a given text
def add_furigana(text):
    # Convert Japanese text to Hiragana using pykakasi
    hiragana_text = kks.convert(text)
    print(hiragana_text)
    txt = ''
    # <p>日本語の<ruby>漢字<rt>かんじ</rt></ruby>は難しいです。</p>
    for replacement in hiragana_text:
        if contains_kanji(replacement['orig']):
            txt += f"""<ruby>{replacement['orig']}<rt><input type="text" oninput="checkFurigana(this, '{replacement['hira']}')" /></rt></ruby>"""
            #onkeypress="handleKeyPress(event)">
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
