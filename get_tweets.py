import os
import tweepy
import pandas as pd
from dotenv import load_dotenv


class TwitterScraper:
    def __init__(self):
        load_dotenv()
        bearer_token = os.getenv("BEARER_TOKEN")
        self.client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    def search_tweets(self, query: str, max_results: int=1000, output_path: str=None) -> pd.DataFrame:
        """Search tweets using the Twitter API and save them to a CSV file.

        Args:
            query (str): The search query.
            max_results (int, optional): The maximum number of results to return. Defaults to 1000.
            output_path (str, optional): The path to the CSV file. Defaults to None (df is not written).
        
        Returns:
            pd.DataFrame: A DataFrame containing the tweets.
        """
        data = []

        tweets = tweepy.Paginator(
            self.client.search_recent_tweets,
            query=query,
            max_results=100,
            tweet_fields=[
                "id",
                "author_id",
                "created_at",
                "text",
                "lang",
                "public_metrics",
            ],
        ).flatten(limit=max_results)

        for tweet in tweets:
            try:
                tweet_data = {
                    "id": tweet["id"],
                    "author_id": tweet["author_id"],
                    "created_at": tweet["created_at"],
                    "lang": tweet["lang"],
                    "text": tweet["text"],
                    "retweet_count": tweet["public_metrics"]["retweet_count"],
                    "reply_count": tweet["public_metrics"]["reply_count"],
                    "like_count": tweet["public_metrics"]["like_count"],
                    "quote_count": tweet["public_metrics"]["quote_count"],
                }
            except:
                continue

            data.append(tweet_data)

        df = pd.DataFrame(data)

        if output_path:
            df.to_csv(output_path, index=False)

        return df


if __name__ == "__main__":
    scraper = TwitterScraper()
    scraper.search_tweets("world cup lang: en", output_path="tweets.csv")
