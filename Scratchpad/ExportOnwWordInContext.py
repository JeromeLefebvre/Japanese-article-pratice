import pykakasi
import re

def contains_kanji(text:str) -> bool:
    kanji_pattern = re.compile(r'[\u4e00-\u9faf]')
    return bool(kanji_pattern.search(text))

def filter_kanji(result:list) -> list:
    return [k for k in result if contains_kanji(k['orig'])]

def convert(text: str, all_fields= False) -> str:
    kks = pykakasi.kakasi()
    kks_output = kks.convert(text)
    if not all_fields:
        kks_output = [{'orig': k['orig'], 'hira': k['hira']} for k in kks_output]
    return filter_kanji(kks_output)


text = "辛い食べ物だけを１時間食べ続けるなんて、私には辛すぎる。"
tokens = convert(text, all_fields=True)
for t in tokens:
    print(t)