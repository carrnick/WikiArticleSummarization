# WikiArticleSummarization
This class summarizes a Wikipedia page using [Hugging Face's DistilBart text summarization model](https://huggingface.co/sshleifer/distilbart-cnn-12-6) given a valid article.

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
