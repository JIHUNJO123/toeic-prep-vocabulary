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

# Final batch - M, N, O, P words to reach 3600
WORDS = [
    ('machine', 'noun', 'device', 'Vending machine.'),
    ('machinery', 'noun', 'machines', 'Heavy machinery.'),
    ('mad', 'adj', 'angry', 'Mad rush.'),
    ('madness', 'noun', 'craziness', 'Market madness.'),
    ('magazine', 'noun', 'publication', 'Trade magazine.'),
    ('magic', 'noun', 'wonder', 'Marketing magic.'),
    ('magical', 'adj', 'wonderful', 'Magical moment.'),
    ('magnet', 'noun', 'attractor', 'Customer magnet.'),
    ('magnetic', 'adj', 'attractive', 'Magnetic personality.'),
    ('magnificent', 'adj', 'splendid', 'Magnificent results.'),
    ('magnitude', 'noun', 'size', 'Order of magnitude.'),
    ('mail', 'noun', 'letters', 'Direct mail.'),
    ('mailing', 'noun', 'sending mail', 'Mailing list.'),
    ('mainstream', 'adj', 'conventional', 'Mainstream market.'),
    ('maintain', 'verb', 'to keep', 'Maintain quality.'),
    ('maintenance', 'noun', 'upkeep', 'Maintenance cost.'),
    ('major', 'adj', 'important', 'Major client.'),
    ('majority', 'noun', 'greater part', 'Majority stake.'),
    ('make', 'verb', 'to create', 'Make decision.'),
    ('maker', 'noun', 'creator', 'Decision maker.'),
    ('makeup', 'noun', 'composition', 'Staff makeup.'),
    ('making', 'noun', 'creation', 'Decision making.'),
    ('malfunction', 'noun', 'failure', 'Equipment malfunction.'),
    ('mall', 'noun', 'shopping center', 'Shopping mall.'),
    ('malpractice', 'noun', 'wrongdoing', 'Professional malpractice.'),
    ('man', 'noun', 'person', 'Right man.'),
    ('manage', 'verb', 'to control', 'Manage team.'),
    ('manageable', 'adj', 'controllable', 'Manageable workload.'),
    ('management', 'noun', 'control', 'Senior management.'),
    ('manager', 'noun', 'supervisor', 'Project manager.'),
    ('managerial', 'adj', 'relating to management', 'Managerial skills.'),
    ('mandate', 'noun', 'order', 'Legal mandate.'),
    ('mandatory', 'adj', 'required', 'Mandatory training.'),
    ('maneuver', 'verb', 'to move skillfully', 'Market maneuver.'),
    ('manifest', 'verb', 'to show', 'Manifest interest.'),
    ('manifestation', 'noun', 'display', 'Clear manifestation.'),
    ('manipulate', 'verb', 'to control unfairly', 'Manipulate data.'),
    ('manipulation', 'noun', 'unfair control', 'Market manipulation.'),
    ('mankind', 'noun', 'humanity', 'Benefit mankind.'),
    ('manner', 'noun', 'way', 'Professional manner.'),
    ('manpower', 'noun', 'workers', 'Manpower shortage.'),
    ('manual', 'noun', 'handbook', 'User manual.'),
    ('manually', 'adv', 'by hand', 'Manually process.'),
    ('manufacture', 'verb', 'to make', 'Manufacture goods.'),
    ('manufacturer', 'noun', 'producer', 'Equipment manufacturer.'),
    ('manufacturing', 'noun', 'production', 'Manufacturing sector.'),
    ('manuscript', 'noun', 'written document', 'Submit manuscript.'),
    ('map', 'noun', 'diagram', 'Road map.'),
    ('mapping', 'noun', 'charting', 'Process mapping.'),
    ('marathon', 'noun', 'long event', 'Marathon session.'),
    ('marble', 'noun', 'stone', 'Marble flooring.'),
    ('march', 'verb', 'to walk', 'March forward.'),
    ('margin', 'noun', 'edge', 'Profit margin.'),
    ('marginal', 'adj', 'slight', 'Marginal improvement.'),
    ('marginally', 'adv', 'slightly', 'Marginally better.'),
    ('marine', 'adj', 'relating to sea', 'Marine industry.'),
    ('mark', 'noun', 'sign', 'Trademark.'),
    ('markdown', 'noun', 'price reduction', 'Seasonal markdown.'),
    ('marked', 'adj', 'noticeable', 'Marked improvement.'),
    ('marker', 'noun', 'indicator', 'Key marker.'),
    ('market', 'noun', 'place to buy/sell', 'Target market.'),
    ('marketable', 'adj', 'saleable', 'Marketable skills.'),
    ('marketer', 'noun', 'one who markets', 'Digital marketer.'),
    ('marketing', 'noun', 'promotion', 'Marketing strategy.'),
    ('marketplace', 'noun', 'market', 'Online marketplace.'),
    ('markup', 'noun', 'price increase', 'Standard markup.'),
    ('marriage', 'noun', 'union', 'Corporate marriage.'),
    ('marry', 'verb', 'to unite', 'Marry ideas.'),
    ('marvel', 'noun', 'wonder', 'Engineering marvel.'),
    ('marvelous', 'adj', 'wonderful', 'Marvelous achievement.'),
    ('mask', 'verb', 'to hide', 'Mask problems.'),
    ('mass', 'noun', 'large amount', 'Mass production.'),
    ('massive', 'adj', 'huge', 'Massive growth.'),
    ('massively', 'adv', 'hugely', 'Massively successful.'),
    ('master', 'noun', 'expert', 'Master plan.'),
    ('masterpiece', 'noun', 'great work', 'Marketing masterpiece.'),
    ('mastery', 'noun', 'expertise', 'Mastery of skills.'),
    ('match', 'verb', 'to equal', 'Match offer.'),
    ('matching', 'adj', 'corresponding', 'Matching funds.'),
    ('mate', 'noun', 'partner', 'Running mate.'),
    ('material', 'noun', 'substance', 'Raw material.'),
    ('materialize', 'verb', 'to happen', 'Deal materialized.'),
    ('matter', 'noun', 'issue', 'Important matter.'),
    ('mature', 'adj', 'fully developed', 'Mature market.'),
    ('maturity', 'noun', 'full development', 'Bond maturity.'),
    ('maximize', 'verb', 'to increase', 'Maximize profit.'),
    ('maximum', 'noun', 'highest amount', 'Maximum capacity.'),
    ('maze', 'noun', 'complex network', 'Legal maze.'),
    ('meadow', 'noun', 'field', 'Green meadow.'),
    ('meal', 'noun', 'food', 'Business meal.'),
    ('mean', 'verb', 'to intend', 'Mean business.'),
    ('meaning', 'noun', 'significance', 'Deep meaning.'),
    ('meaningful', 'adj', 'significant', 'Meaningful change.'),
    ('meaningless', 'adj', 'without meaning', 'Meaningless data.'),
    ('means', 'noun', 'method', 'By all means.'),
    ('meantime', 'noun', 'meanwhile', 'In the meantime.'),
    ('meanwhile', 'adv', 'at same time', 'Meanwhile continue.'),
    ('measurable', 'adj', 'quantifiable', 'Measurable results.'),
    ('measure', 'noun', 'action', 'Cost-cutting measure.'),
    ('measurement', 'noun', 'measuring', 'Performance measurement.'),
    ('mechanic', 'noun', 'repair person', 'Auto mechanic.'),
    ('mechanical', 'adj', 'relating to machines', 'Mechanical failure.'),
    ('mechanism', 'noun', 'system', 'Control mechanism.'),
    ('medal', 'noun', 'award', 'Gold medal.'),
    ('media', 'noun', 'communication channels', 'Social media.'),
    ('mediate', 'verb', 'to intervene', 'Mediate dispute.'),
    ('mediation', 'noun', 'intervention', 'Conflict mediation.'),
    ('mediator', 'noun', 'intervener', 'Professional mediator.'),
    ('medical', 'adj', 'relating to medicine', 'Medical insurance.'),
    ('medication', 'noun', 'medicine', 'Pain medication.'),
    ('medicine', 'noun', 'treatment', 'Take medicine.'),
    ('mediocre', 'adj', 'average', 'Mediocre performance.'),
    ('medium', 'noun', 'middle', 'Advertising medium.'),
    ('meet', 'verb', 'to encounter', 'Meet deadline.'),
    ('meeting', 'noun', 'gathering', 'Board meeting.'),
    ('megabyte', 'noun', 'data unit', 'File size megabyte.'),
    ('melt', 'verb', 'to dissolve', 'Ice melt.'),
    ('meltdown', 'noun', 'collapse', 'Market meltdown.'),
    ('member', 'noun', 'participant', 'Team member.'),
    ('membership', 'noun', 'belonging', 'Club membership.'),
    ('memo', 'noun', 'note', 'Office memo.'),
    ('memorable', 'adj', 'unforgettable', 'Memorable event.'),
    ('memorandum', 'noun', 'written note', 'Legal memorandum.'),
    ('memorial', 'noun', 'monument', 'Memorial service.'),
    ('memorize', 'verb', 'to learn by heart', 'Memorize speech.'),
    ('memory', 'noun', 'recollection', 'Computer memory.'),
    ('menace', 'noun', 'threat', 'Security menace.'),
    ('mend', 'verb', 'to repair', 'Mend relationship.'),
    ('mental', 'adj', 'relating to mind', 'Mental health.'),
    ('mentality', 'noun', 'mindset', 'Growth mentality.'),
    ('mentally', 'adv', 'in the mind', 'Mentally prepared.'),
    ('mention', 'verb', 'to refer to', 'Worth mentioning.'),
    ('mentor', 'noun', 'advisor', 'Business mentor.'),
    ('mentoring', 'noun', 'advising', 'Mentoring program.'),
    ('menu', 'noun', 'list', 'Options menu.'),
    ('merchandise', 'noun', 'goods', 'Retail merchandise.'),
    ('merchandising', 'noun', 'promoting goods', 'Visual merchandising.'),
    ('merchant', 'noun', 'trader', 'Online merchant.'),
    ('mercy', 'noun', 'compassion', 'At mercy of.'),
    ('mere', 'adj', 'only', 'Mere fraction.'),
    ('merely', 'adv', 'only', 'Merely suggest.'),
    ('merge', 'verb', 'to combine', 'Merge companies.'),
    ('merger', 'noun', 'combination', 'Company merger.'),
    ('merit', 'noun', 'worth', 'On merit.'),
    ('meritorious', 'adj', 'worthy', 'Meritorious work.'),
    ('mess', 'noun', 'disorder', 'Financial mess.'),
    ('message', 'noun', 'communication', 'Marketing message.'),
    ('messenger', 'noun', 'carrier', 'Instant messenger.'),
    ('messy', 'adj', 'disorderly', 'Messy situation.'),
    ('metal', 'noun', 'material', 'Precious metal.'),
    ('metaphor', 'noun', 'comparison', 'Business metaphor.'),
    ('meter', 'noun', 'measuring device', 'Parking meter.'),
    ('method', 'noun', 'way', 'Payment method.'),
    ('methodical', 'adj', 'systematic', 'Methodical approach.'),
    ('methodology', 'noun', 'system of methods', 'Research methodology.'),
    ('meticulous', 'adj', 'careful', 'Meticulous planning.'),
    ('metric', 'noun', 'measurement', 'Key metric.'),
    ('metropolitan', 'adj', 'urban', 'Metropolitan area.'),
    ('microphone', 'noun', 'sound device', 'Conference microphone.'),
    ('microscope', 'noun', 'viewing device', 'Under microscope.'),
    ('mid', 'adj', 'middle', 'Mid-year review.'),
    ('middle', 'noun', 'center', 'Middle management.'),
    ('midway', 'adv', 'halfway', 'Midway through.'),
    ('might', 'noun', 'power', 'Economic might.'),
    ('mighty', 'adj', 'powerful', 'Mighty corporation.'),
    ('migrate', 'verb', 'to move', 'Migrate data.'),
    ('migration', 'noun', 'movement', 'Data migration.'),
    ('mild', 'adj', 'gentle', 'Mild criticism.'),
    ('mildly', 'adv', 'gently', 'Mildly concerned.'),
    ('milestone', 'noun', 'important event', 'Project milestone.'),
    ('military', 'adj', 'relating to armed forces', 'Military contract.'),
    ('mill', 'noun', 'factory', 'Paper mill.'),
    ('million', 'noun', 'number', 'Millions in sales.'),
    ('millionaire', 'noun', 'wealthy person', 'Self-made millionaire.'),
    ('mimic', 'verb', 'to copy', 'Mimic competitors.'),
    ('mind', 'noun', 'brain', 'Peace of mind.'),
    ('mindful', 'adj', 'aware', 'Mindful of costs.'),
    ('mindset', 'noun', 'attitude', 'Growth mindset.'),
    ('mine', 'noun', 'mineral source', 'Data mine.'),
    ('mineral', 'noun', 'natural substance', 'Mineral resources.'),
    ('mingle', 'verb', 'to mix', 'Mingle at event.'),
    ('minimal', 'adj', 'very small', 'Minimal risk.'),
    ('minimize', 'verb', 'to reduce', 'Minimize costs.'),
    ('minimum', 'noun', 'smallest amount', 'Minimum wage.'),
    ('mining', 'noun', 'extraction', 'Data mining.'),
    ('minister', 'noun', 'government official', 'Finance minister.'),
    ('ministry', 'noun', 'government department', 'Ministry of Finance.'),
    ('minor', 'adj', 'small', 'Minor issue.'),
    ('minority', 'noun', 'smaller part', 'Minority stake.'),
    ('mint', 'noun', 'money maker', 'Make a mint.'),
    ('minus', 'prep', 'less', 'Minus expenses.'),
    ('minute', 'noun', 'time unit', 'Meeting minutes.'),
    ('miracle', 'noun', 'wonder', 'Economic miracle.'),
    ('miraculous', 'adj', 'wonderful', 'Miraculous recovery.'),
    ('mirror', 'verb', 'to reflect', 'Mirror trends.'),
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
