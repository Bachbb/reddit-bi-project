"""
Script: clean_reddit_keywords.py
Input : reddit_cleaned__1_.csv
Output: reddit_keywords_cleaned.csv
"""

import pandas as pd
from collections import Counter
import re

# ── 1. Đọc file gốc ──────────────────────────────────────────────
df = pd.read_csv('reddit_cleaned__1_.csv')

# ── 2. Stopwords ──────────────────────────────────────────────────
stopwords = set([
    # Đại từ / giới từ / liên từ
    'the','and','that','this','with','for','are','was','not','but','have',
    'you','your','they','from','what','will','just','been','also','more',
    'can','its','all','one','out','get','has','had','her','his','him',
    'she','our','we','do','did','so','it','is','in','of','a','to',
    'i','he','be','at','by','an','or','as','if','my','me','no','up','on',
    'like','would','there','their','about','when','into','than','some',
    'were','them','then','could','which','even','after','over','think',
    'know','people','because','going','dont','very','really','make',
    # Từ phổ biến không có nghĩa phân tích
    'time','does','only','other','being','right','here','want','good',
    'someone','well','these','those','thing','work','much','still',
    'said','back','need','look','come','made','take','many','each',
    'same','such','most','while','way','see','between','every','where',
    'through','never','always','without','around','actually','pretty',
    'stuff','things','anyone','anything','nothing','something','everything',
    'first','better','ever','sure','probably','everyone','getting',
    'before','down','year','years','person','doing','tell','should',
    # Từ tục / không phân tích được
    'fucking','shit','fuck','damn','hell','crap','ass','bullshit',
    # Reddit-specific
    'reddit','post','comment','repost','downvote','upvote','thread',
    # URL artifacts
    'http','https','www',
])

# ── 3. Hàm trích xuất keywords ────────────────────────────────────
def extract_keywords(texts, top_n=30):
    all_text = ' '.join(texts.dropna()).lower()
    words = re.findall(r'\b[a-z]{4,}\b', all_text)
    words = [w for w in words if w not in stopwords]
    return Counter(words).most_common(top_n)

# ── 4. Trích xuất theo nhóm ───────────────────────────────────────
results = []

# Tổng thể
for rank, (word, count) in enumerate(extract_keywords(df['text'], 30), 1):
    results.append({'keyword': word, 'count': count, 'subreddit': 'All', 'rank': rank})

# Theo từng subreddit
for sub in sorted(df['subreddit'].unique()):
    sub_texts = df[df['subreddit'] == sub]['text']
    for rank, (word, count) in enumerate(extract_keywords(sub_texts, 20), 1):
        results.append({'keyword': word, 'count': count, 'subreddit': sub, 'rank': rank})

# ── 5. Tạo DataFrame & làm sạch ──────────────────────────────────
out = pd.DataFrame(results)
out['keyword']   = out['keyword'].str.strip().str.lower()
out['subreddit'] = out['subreddit'].str.strip()
out = out.drop_duplicates()
out = out.sort_values(['subreddit', 'rank']).reset_index(drop=True)

# ── 6. Xuất file ──────────────────────────────────────────────────
out.to_csv('reddit_keywords_cleaned.csv', index=False, encoding='utf-8-sig')

print(f"✅ Đã xuất: reddit_keywords_cleaned.csv")
print(f"   Tổng rows : {len(out)}")
print()
print(out.to_string(index=False))
