import requests
from bs4 import BeautifulSoup
import re
from transformers import pipeline

class WikiSummarizer():
  def __init__(self):
    pass
  
  def __remove_tags(self, t):
    '''
    Removes HTML tags and removes unneeded characters from text.
    '''
    t = str(t)
    t = t.replace('\\', '')
    t = t.replace('\n', '')
    t = re.sub('\[\d+]', '', t)
    t = re.sub('<[^>]+>', '', t)
    return t

  def __retrieve_and_clean_text(self, url):
    '''
    Retrieves text from Wikipedia article, cleans it, and returns the full page as a string.
    '''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.find_all('p')

    return ' '.join(list(map(self.__remove_tags, text)))


  def summarize(self, url, max_splits: int = 1):
    '''
    Summarizes Wikipedia article.
    '''

    # Checks if URL is a string and if URL is valid.
    assert type(url) == str, 'url parameter must be a string.'
    assert 'https://en.wikipedia.org/wiki' in url, 'Must be a valid wikipedia article.'
    

    # Sets the minimum and maximum length of the document.
    MIN_LENGTH = 56
    MAX_LENGTH = 142
    summarized_list, start, end, iter = [], 0, 500, 500

    # Cleans text
    text = self.__retrieve_and_clean_text(url)

    # If the document length is smaller than the max length of the model, the max length is reduced to avoid unnecessary computation.
    doc_length = len(text.split())
    if doc_length < MAX_LENGTH:
      MAX_LENGTH, MIN_LENGTH, end = doc_length, 0, doc_length

    # Instantiates HuggingFace's DistilBart model for text summarization.
    summary_model = pipeline('summarization', 
                             model='sshleifer/distilbart-cnn-12-6',
                             max_length = MAX_LENGTH,
                             min_length = MIN_LENGTH)
    
    # Summarizes text 500 words at a time, depending on max_splits parameter.
    for s in range(0, max_splits):
      summary = summary_model(' '.join(text.split()[start:end]))
      summarized_list.append(summary[0]['summary_text'])
      start = end
      end = end + iter
      # If the end of the article is reached but there are stil more loops to go through.
      if end > len(text.split()):
        break

    # Returns summarized text as a string
    return ' '.join(summarized_list)

w = WikiSummarizer()
url = 'https://en.wikipedia.org/wiki/World_War_II'
w.summarize(url)

w.summarize(url, max_splits=3)
