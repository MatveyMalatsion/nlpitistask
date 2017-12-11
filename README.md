# nlpitistask

# Sentiment analysis in twitter

This is an attempt to reiterate the Task ["Sentiment analysis in twitter" from Semeaval-2013](https://www.cs.york.ac.uk/semeval-2013/task2.html) (Subtask A)

This repo contains:

* metatables from organizers with data in format: "\<SID>\<tab>\<UID>\<tab>\<START_WORD_POSITION>\<tab>\<END_WORD_POSITION>\<tab>\<positive|negative|neutral|objective>\<tab>"
* modified python script, that is able to download raw tweet's text by its ID from metatable to .csv file
* downloaded and prepared dataset with ~23k of tweets with sentiment scores

To download data manually, please use
```sh
$easy_install beautifulsoup4
$sudo python download_tweets.py <<input_file_name>>
```

You can see results of my experiments in a private Microsoft Azure ML Studio experiment that is available at [this link](https://gallery.cortanaintelligence.com/Experiment/MMMalatsionSentimentAnalysysAttempt) 






