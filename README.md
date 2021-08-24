# Cryptocurrency Sentiment Analysis
A Real-Time Cryptocurrency Price and  Twitter Sentiments Analysis. The goal of this project is to analyze the correlation between cryptocurrencies' price in USD and a score based on the sentiment analysis of tweets, the number of followers of the user, the number of retweets and the number of likes.

- In the first part I will make an historical analysis of the correlation.

- In the second part I will take realtime visualisation of the evolution of tweets scores with cryptocurrency's price in USD.

## Steps of the project:

- 1. Retrieval of the tweets from the Twitter API.
- 2. Retrieval of the cryptocurrencies change to USD historical data by interval of 1 minute from the binance API.
- 3. Sentiment analysis of the tweets using the VADER algorithm.
- 4. Computation of a score based on the sentiment, the number of likes, the number of tweets in a time range and the number of followers of the person who tweeted.
- 5. Computation and visualisation of a cross-correlation score with different lag values between the tweets scores and the cryptocurrency's change in USD.
- 6. Real-time visualisation of the correlation between the tweets and cryptocurrency's change.

## Data sources and quantity:

### Twitter

The Twitter API is the source for all the tweets. It is limited to 450 requests of maximum 100 tweets per 15 minutes with the App login. It can only retrieve tweets of 7 days old at most. To make searches in the Twitter API you must use the query operators to match on multiple keywords. Here is an example of a query for the Bitcoin related tweets. bitcoin OR #BTC OR #bitcoin OR $BTC OR $bitcoin

For each tweets I extracted the following informations:

- ID
- Text
- Username
- Number of followers of the user
- Number of retweets
- Number of likes
- Creation date

At this step I also filtered the non english tweets by specifying it to the Twitter API.

### Cryptocurrencies

The [Binance API](https://www.binance.com/en-IN/support/faq/360002502072) was used to retrieve the crypto currencies that I analyzed. Different endpoints are available to retrieve historical data every minute up until 7 days, after what I can retrieve currencies hourly or daily.

The data retrieved contains the following fields:

- time: when the data was emitted
- close: the price at the end of the time frame (minutely, hourly or daily depending the targeted endpoint)
- high: the highest price reached during the time frame
- low: the lowest price reached during the time frame
- open: the price at the opening of the time frame


The smallest time unit I have is every minute. I didn't find any free API that offers smaller time units like every second even if I considered some others like Coinbase/Bitstamp/Kraken/ITBIT.

With the Binance API I was able to retrieve currencies minutely for the five different cryptos:

- ADA
- BCH
- D
- USDT
- SOL

Even if I have the currencies grouped minutely with an OHLCV (Open High Low Close Volume) system, it is sufficient to use the closing price to study the correlation.

## Preprocessing

For the preprocessing, I removed all of the useless data from the tweets, such as HTTP links, @pseudo tags, images, videos and hashtags (#happy->happy). I finally stored them in a CSV file.

Once the cleaned files are obtained, I processed the sentiment analysis on each textual content of the tweet to obtain a sentiment score named compound. This compound is then multiplied by the number of followers of the user and the number of likes to emphasize the importance of the sentiment. Here is the calculation made on the compound to obtain the tweet's score:

tweet's score = (#like + #follower) * compound

If the tweet comes from an influencer, the number of followers will be high, so the score will be. If it is retweeted by a lambda person with a dozen of followers, the score will be small. We don't consider the number of retweet because it is the same for the original tweet and for any of its retweet: we don't want that a lambda person could have an impact on the score by considering the number of retweet in the tweet's score calculation.

Finally, after the tweets have been fully processed, we end up with two features:

- the creation date of the tweet
- the score of the tweet where a negative value indicates a bad sentiment, a positive a good sentiment and a zero indicates a neutral sentiment.

## Techniques and algorithms

In this section are listed the techniques and algorithms we used to find a correlation and to analyze the sentiments of the tweets.

### Cross-correlation analysis

Applying a correlation on the series (tweets' scores and crypto currency) is not enough. That's why we need cross-correlation. The difference is that cross-correlation adds a lag which permit to shift one of the timeseries left or right to find, maybe, a better correlation. This is coherent with our problem as the currency changes come after the tweets' sentiments. So we are fully allowed to operate it.

Now the correlation's method we use can be either Pearson, Kendall or Spearman. We tried all of them and their are pretty equivalent. However Spearman obtains globally better results because it is able to correlate on linear and non-linear data.

Sentiment analysis - vaderSentiment
For the analysis of the sentiment we use the VADER algorithm. There is a great implementation in Python called [vaderSentiment](https://github.com/cjhutto/vaderSentiment).

Here is a description of the 3 sentiment analysis algorithms that we considered.

### Polarity classification

Since the rise of social media, a large part of the current research has been focused on classifying natural language as either positive or negative sentiment. Polarity classification have been found to achieve high accuracy in predicting change or trends in public sentiment, for a myriad of domains (e.g. stock price prediction).

### Lexicon-based approach

A lexicon is a collection of features (e.g. words and their sentiment classification). The lexicon-based approach is a common method used in sentiment analysis where a piece of text is compared to a lexicon and attributed sentiment classifications. Lexicons can be complex to create, but once created require little resources to use. Well designed lexicons can achieve a high accuracy and are held in high regard in the scientific community.

### VADER

Valence Aware Dictionary and sEntiment Reasoner (VADER) is a combined lexicon and rule-based sentiment analytic software, developed by Hutto and Gilbert. VADER is capable of both detecting the polarity (positive, neutral, negative) and the sentiment intensity in text. The authors have published the lexicon and python specific module under an MIT License, thus it is considered open source and free to use.

The VADER algorithm uses negations et contractions (not good, wasn’t good), ponctuation (good!!!), capital letters, emotes :), emojis, intensificators (very, kind of), acronyms (lol) and other factors to calculate the scores. It outputs a compound score between -1 (negative) and 1 (positive).

## Tools and libraries

### Python

We have used the Python programming language for this project in version 3.6.

### Jupyter notebooks

Jupyter Notebook (formerly IPython Notebooks) is a web-based interactive computational environment for creating, executing, and visualizing Jupyter notebooks. We have used it to structure, document and execute/visualise our code.

### Pandas

Pandas is the library we have used the most. It proposes useful functions to read data from our csv files, to write to them, to create and make mathematical operations on dataframes and time series. We have used it for the cross-correlation analysis.

### Twython

Twython is a library used to interact with the Twitter API. It proposes useful functions login and make queries on the API.

### Matplotlib

We have used this library for most of our plots.

### Plotly

Plotly is another library used for plots.

### tqdm

We have used tqdm to show progress bars for long running operations, such a retrieval of the tweets from the Python API and the preprocessing of the tweets. It took around 14 hours to preprocess the tweets but then we switched to a multi-threaded method which didn't support tqdm.

### Numpy

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. We used numpy for some of the operations on the dataframes.

### Other libraries

We have used many other small Python libraries which can be found in the Jupyter notebooks at the root of this project.
