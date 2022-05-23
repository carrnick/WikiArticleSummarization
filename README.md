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
