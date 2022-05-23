# WikiArticleSummarization
Wikipedia pages can be lengthy and take a long time to read through. This class summarizes a Wikipedia page using [Hugging Face's DistilBart text summarization model](https://huggingface.co/sshleifer/distilbart-cnn-12-6) given a valid article.

Example article used: https://en.wikipedia.org/wiki/World_War_II

[Notebook](https://github.com/carrnick/WikiArticleSummarization/blob/main/Wikipedia_Article_Summarization.ipynb)

[Python file](https://github.com/carrnick/WikiArticleSummarization/blob/main/wikipedia_article_summarization.py)

### How it works/How to use:
1.   Instantiate WikiSummarizer
```
      w = WikiSummarizer()
```
2.   Pass in a URL to the `summary` method of the instantiated object
```
      url = 'https://en.wikipedia.org/wiki/Ww2'
      w.summarize(url)
```

3. Optionally pass in an integer for max_splits. This parameter defines how long the summarization should be. The `distilbart-cnn-12-6` model can only summarize 500 words at a time. By default `max_splits` is 1, so the first 500 words will be summarized. Setting `max_splits` to 2 will summarize and return the first 1000 words, and so on. It may take a while to run anything over the default setting, so be conservative with this parameter.
```
      w.summarize(url, max_splits=2)
```

### Output:
```
w = WikiSummarizer()
url = 'https://en.wikipedia.org/wiki/World_War_II'
w.summarize(url)

World War II or the Second World War, often abbreviated as WWII or WW2, was a 
global war that lasted from 1939 to 1945 . It involved the vast majority of 
the world's countries, including all of the great powers, forming two opposing 
military alliances: the Allies and the Axis powers . Aircraft played a major role 
in the conflict, enabling the strategic bombing of population centres and the only 
two uses of nuclear weapons in war . It resulted in 70 to 85 million fatalities, 
a majority being civilians .
```

```
w.summarize(url, max_splits=3)

 World War II or the Second World War, often abbreviated as WWII or WW2, was a 
 global war that lasted from 1939 to 1945 . It involved the vast majority of the 
 world's countries, including all of the great powers, forming two opposing military 
 alliances: the Allies and the Axis powers . Aircraft played a major role in the 
 conflict, enabling the strategic bombing of population centres and the only two 
 uses of nuclear weapons in war . It resulted in 70 to 85 million fatalities, a 
 majority being civilians .  World War II changed the political alignment and social 
 structure of the globe . The United Nations was established to foster international 
 co-operation and prevent future conflicts . The Soviet Union and the United States 
 emerged as rival superpowers, setting the stage for the Cold War . The influence of 
 its great powers waned, triggering the decolonisation of Africa and Asia .  The exact 
 date of the war's end is also not universally agreed upon . It was generally accepted 
 at the time that the war ended with the armistice of 14 August 1945 (V-J Day) rather 
 than with the formal surrender of Japan on 2 September 1945 . A peace treaty between 
 Japan and the Allies was signed in 1951 . A 1990 treaty regarding Germany's future 
 allowed the reunification of East and West Germany to take place .
```
