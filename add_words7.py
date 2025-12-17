import json
import requests
import time

API_KEY = 'AIzaSyCWW8OXnc7QwIUTs_W0FCEVrZEm3qliDzk'

def translate_batch(texts, target_lang):
    if not texts:
        return []
    url = f'https://translation.googleapis.com/language/translate/v2?key={API_KEY}'
    results = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        payload = {'q': batch, 'target': target_lang, 'source': 'en'}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                translations = [t['translatedText'] for t in data['data']['translations']]
                results.extend(translations)
            else:
                results.extend(batch)
        except:
            results.extend(batch)
    return results

# Final batch to reach exactly 3600
WORDS = [
    ('miscellaneous', 'adj', 'various', 'Miscellaneous expenses.'),
    ('misconception', 'noun', 'wrong idea', 'Common misconception.'),
    ('misconduct', 'noun', 'wrongdoing', 'Professional misconduct.'),
    ('miserable', 'adj', 'very unhappy', 'Miserable failure.'),
    ('misery', 'noun', 'suffering', 'Economic misery.'),
    ('misfortune', 'noun', 'bad luck', 'Business misfortune.'),
    ('misguided', 'adj', 'mistaken', 'Misguided strategy.'),
    ('mishandle', 'verb', 'to handle badly', 'Mishandle situation.'),
    ('misinformation', 'noun', 'false information', 'Spread misinformation.'),
    ('misinterpret', 'verb', 'to understand wrongly', 'Misinterpret data.'),
    ('mislead', 'verb', 'to deceive', 'Mislead customers.'),
    ('misleading', 'adj', 'deceptive', 'Misleading advertising.'),
    ('mismanagement', 'noun', 'poor management', 'Financial mismanagement.'),
    ('mismatch', 'noun', 'poor fit', 'Skill mismatch.'),
    ('misplace', 'verb', 'to lose', 'Misplace documents.'),
    ('misrepresent', 'verb', 'to describe wrongly', 'Misrepresent facts.'),
    ('misrepresentation', 'noun', 'false description', 'Material misrepresentation.'),
    ('miss', 'verb', 'to fail to hit', 'Miss deadline.'),
    ('missing', 'adj', 'absent', 'Missing information.'),
    ('mission', 'noun', 'purpose', 'Company mission.'),
    ('mistake', 'noun', 'error', 'Costly mistake.'),
    ('mistaken', 'adj', 'wrong', 'Mistaken belief.'),
    ('mistreat', 'verb', 'to treat badly', 'Mistreat employees.'),
    ('misunderstand', 'verb', 'to understand wrongly', 'Misunderstand instructions.'),
    ('misunderstanding', 'noun', 'wrong understanding', 'Clear misunderstanding.'),
    ('misuse', 'verb', 'to use wrongly', 'Misuse funds.'),
    ('mitigate', 'verb', 'to lessen', 'Mitigate risk.'),
    ('mitigation', 'noun', 'lessening', 'Risk mitigation.'),
    ('mix', 'noun', 'combination', 'Product mix.'),
    ('mixed', 'adj', 'combined', 'Mixed results.'),
]

with open('assets/data/words.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    existing = data.get('words', data)

print(f'기존 단어: {len(existing)}개')
word_set = {w['word'].lower() for w in existing}
new_words = [(w,p,m,e) for w,p,m,e in WORDS if w.lower() not in word_set]
print(f'추가할 새 단어: {len(new_words)}개')

if not new_words:
    print('추가할 단어 없음')
    exit()

langs = ['ko','ja','zh','es','pt','de','fr','vi','ar','id']
trans_by_lang = {}
print('번역 중...')
for lang in langs:
    print(f'  {lang}...', end=' ', flush=True)
    trans_by_lang[lang] = translate_batch([w[2] for w in new_words], lang)
    print('완료')
    time.sleep(0.2)

count = len(existing)
total = count + len(new_words)
for i, (word, pos, meaning, example) in enumerate(new_words):
    word_id = count + i + 1
    if word_id <= total // 4:
        level = '0-400'
    elif word_id <= total // 2:
        level = '400-600'
    elif word_id <= total * 3 // 4:
        level = '600-800'
    else:
        level = '800-990'
    trans = {lang: trans_by_lang[lang][i] if i < len(trans_by_lang[lang]) else meaning for lang in langs}
    existing.append({'id': word_id, 'word': word, 'meaning': meaning, 'example': example, 'pos': pos, 'level': level, 'translations': trans})

with open('assets/data/words.json', 'w', encoding='utf-8') as f:
    json.dump({'words': existing}, f, ensure_ascii=False, indent=2)

level_counts = {}
for w in existing:
    lv = w.get('level', '0-400')
    level_counts[lv] = level_counts.get(lv, 0) + 1

print(f'\n총 단어 수: {len(existing)}개')
for lv in ['0-400', '400-600', '600-800', '800-990']:
    print(f'  {lv}: {level_counts.get(lv, 0)}개')
