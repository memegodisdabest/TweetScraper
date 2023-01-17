# TweetScraper
A Python script to scrape tweets from Twitter

The script requires that you have a valid Twitter account and API/access keys. You can obtain these by signing up for a developer account on Twitter.

Once you have the API keys, you can use the script to make requests to the Twitter API. The script will then scrape the tweets and store them in a JSON file.

You can use the following command to run the script:

python3 tweetscraper.py --query <query> --output <filename>

The --query option allows you to specify the search query you want to use. The --output option allows you to specify the filename of the output JSON file.

For example, you can use the following command to scrape tweets containing the hashtag #Python:

python3 tweetscraper.py --query "#Python" --output "tweets.json"

The script will scrape the tweets and store them in the tweets.json file.

You can then use the data in the JSON file to further analyze the tweets, such as sentiment analysis, keyword extraction, etc.

This version of TweetScraper includes the following features:

Scrape tweets from Twitter using a search query
Store scraped tweets in a JSON file
Ability to specify search query and output file name
Automatically convert response data to JSON
To use this version of TweetScraper, you will need to have a valid Twitter account and API/access keys. You can obtain these by signing up for a developer account on Twitter.

If you encounter any issues while using TweetScraper, please file an issue on GitHub.
