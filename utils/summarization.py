from transformers import pipeline
import requests
from bs4 import BeautifulSoup as bs

def get_model():
    summerizer = pipeline('summarization')
    return summerizer

def get_chunks(url):
    chunk_size = 500
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    text = soup.find_all(['h1','p'])
    text = [t.text for t in text]
    blog = ' '.join(text)
    blog = blog.replace('\n', ' ')
    blog = blog.replace('\r', ' ')
    blog = blog.replace('\t', ' ')
    blog = blog.replace('.','.<eos>')
    blog = blog.replace('?','?<eos>')
    blog = blog.replace('!','!<eos>')
    lines = blog.split('<eos>')
    chunks ,cc = [], 0
    for line in lines:
        if len(chunks) == cc+1:
            if len(chunks[cc]) + len(line.split(' ')) <= chunk_size:
                chunks[cc].extend(line.split(' '))
            else:
                cc += 1
                chunks.append(line.split(' '))
        else:
            chunks.append(line.split(' '))
    for i in range(len(chunks)):
        chunks[i] = ' '.join(chunks[i])
    return chunks
                 
def get_summary_text(text):
    summerizer = get_model()
    result = summerizer(text, max_length=120, min_length=30, do_sample=False)
    return result
