import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random
# nltk.download("twitter_samples")
pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')
print('Number of positive tweets: ', len(pos_tweets))
print('Number of negative tweets: ', len(neg_tweets))
print('\nThe type of all_positive_tweets is: ', type(pos_tweets))
print('The type of a tweet entry is: ', type(neg_tweets[0]))

print('\033[92m' + pos_tweets[random.randint(0,5000)])
print('\033[91m' + neg_tweets[random.randint(0,5000)])

# fig = plt.figure(figsize=(5, 10))
# labels = 'ML', 'IP', 'AL'

# sizes = [40, 35, 25]
# plt.pie(sizes, labels=labels, autopct='%.2f%%',shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

# fig = plt.figure(figsize=(5, 5))
# labels = 'Positives', 'Negative'
# sizes = [len(pos_tweets), len(neg_tweets)]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%',
# shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

tweet = pos_tweets[2277]
print(tweet)