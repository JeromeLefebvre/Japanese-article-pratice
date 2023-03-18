import pykakasi
import re

def contains_kanji(text:str) -> bool:
    kanji_pattern = re.compile(r'[\u4e00-\u9faf]')
    return bool(kanji_pattern.search(text))

def filter_kanji(result:list) -> list:
    return [k for k in result if contains_kanji(k['orig'])]

def convert(text: str, all_fields= False, kanji_only=False) -> str:
    kks = pykakasi.kakasi()
    kks_output = kks.convert(text)
    if not all_fields:
        kks_output = [{'orig': k['orig'], 'hira': k['hira']} for k in kks_output]
    if kanji_only:
        kks_output = filter_kanji(kks_output)
    return kks_output
