# Add  a twitter user to monitor his tweets
Source: https://docs.twitterapi.io/api-reference/endpoint/add_user_to_monitor_tweet

POST /oapi/x_user_stream/add_user_to_monitor_tweet
Add a user to monitor real-time tweets.Monitor tweets from specified accounts, including directly sent tweets, quoted tweets, reply tweets, and retweeted tweets. Please ref:https://twitterapi.io/twitter-stream



# Add Webhook/Websocket Tweet Filter Rule
Source: https://docs.twitterapi.io/api-reference/endpoint/add_webhook_rule

POST /oapi/tweet_filter/add_rule
Add a tweet filter rule. Default rule is not activated.You must call update_rule to activate the rule.



# Batch Get User Info By UserIds
Source: https://docs.twitterapi.io/api-reference/endpoint/batch_get_user_by_userids

get /twitter/user/batch_info_by_ids
Batch get user info by user ids. Pricing:

- Single user request: 18 credits per user
- Bulk request (100+ users): 10 credits per user

Note: For cost optimization, we recommend batching requests when fetching multiple user profiles.



# Check Follow Relationship
Source: https://docs.twitterapi.io/api-reference/endpoint/check_follow_relationship

get /twitter/user/check_follow_relationship
Check if the user is following/followed by the target user. Trial operation price: 100 credits per call.



# Post/reply/quote a tweet
Source: https://docs.twitterapi.io/api-reference/endpoint/create_tweet

POST /twitter/create_tweet
Create a tweet.Need to login first.Trial operation price: $0.001 per call.



# Delete Webhook/Websocket Tweet Filter Rule
Source: https://docs.twitterapi.io/api-reference/endpoint/delete_webhook_rule

DELETE /oapi/tweet_filter/delete_rule
Delete a tweet filter rule. You must set all parameters.



# Search Tweets From All Community 
Source: https://docs.twitterapi.io/api-reference/endpoint/get_all_community_tweets

GET /twitter/community/get_tweets_from_all_community
get tweets from all communities,each page returns up to 20 tweets. Use cursor for pagination.



# Get Article
Source: https://docs.twitterapi.io/api-reference/endpoint/get_article

GET /twitter/article
get article by tweet id. cost 100 credit per article



# Get Community Info By Id
Source: https://docs.twitterapi.io/api-reference/endpoint/get_community_by_id

GET /twitter/community/info
Get community info by community id. Price: 20 credits per call. Note: This API is a bit slow, we are still optimizing it.



# Get Community Members
Source: https://docs.twitterapi.io/api-reference/endpoint/get_community_members

GET /twitter/community/members
Get members of a community. Page size is 20.



# Get Community Moderators
Source: https://docs.twitterapi.io/api-reference/endpoint/get_community_moderators

GET /twitter/community/moderators
Get moderators of a community. Page size is 20.



# Get Community Tweets
Source: https://docs.twitterapi.io/api-reference/endpoint/get_community_tweets

GET /twitter/community/tweets
Get tweets of a community. Page size is 20. Order by creation time desc. 



# Get List Followers
Source: https://docs.twitterapi.io/api-reference/endpoint/get_list_followers

GET /twitter/list/followers
Get followers of a list. Page size is 20.



# Get List Members
Source: https://docs.twitterapi.io/api-reference/endpoint/get_list_members

GET /twitter/list/members
Get members of a list. Page size is 20.



# Get My Account Info
Source: https://docs.twitterapi.io/api-reference/endpoint/get_my_info

GET /oapi/my/info
Get my info



# Get Trends
Source: https://docs.twitterapi.io/api-reference/endpoint/get_trends

GET /twitter/trends
Get trends by woeid



# Get Tweets by IDs
Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_by_ids

GET /twitter/tweets
get tweet by tweet ids



# Get Tweet Quotations
Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_quote

GET /twitter/tweet/quotes
get tweet quotes by tweet id.Each page returns exactly 20 quotes. Use cursor for pagination. Order by quote time desc



# Get Tweet Replies
Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_reply

GET /twitter/tweet/replies
get tweet replies by tweet id.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination. Order by reply time desc



# Get Tweet Retweeters
Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_retweeter

GET /twitter/tweet/retweeters
get tweet retweeters by tweet id.Each page returns about 100 retweeters. Use cursor for pagination. Order by retweet time desc



# Get Tweet Thread Context
Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_thread_context

GET /twitter/tweet/thread_context
Get the thread context of a tweet.Suppose a tweet thread consists of t1, t2 (replying to t1), t3 (replying to t2), and t4, t5, t6 (all replying to t3). If we provide an API where you input t3 and receive t1, t2, t3, t4, t5, t6.Pagination is supported.The pagination size cannot be set (due to Twitter's limitations), and the data returned per page is not fixed.



# Get User Info
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_by_username

get /twitter/user/info
Get unser info by screen name



# Get User Followers
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_followers

GET /twitter/user/followers
Get user followers in reverse chronological order (newest first). Returns exactly 200 followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.



# Get User Followings
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_followings

GET /twitter/user/followings
Get user followings. Each page returns exactly 200 followings. Use cursor for pagination.Sorted by follow date. Most recent followings appear on the first page. 



# Get User Last Tweets
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_last_tweets

GET /twitter/user/last_tweets
Retrieve tweets by user name.Sort by created_at. Results are paginated, with each page returning up to 20 tweets.If you only need to fetch the latest tweets from a single user very frequently, do not use this API—it will cost you a lot. Instead, please refer to https://twitterapi.io/blog/how-to-monitor-twitter-accounts-for-new-tweets-in-real-time. If you have more than 20 Twitter accounts requiring real-time tweet updates, use https://twitterapi.io/twitter-stream which is the most cost-effective solution.



# Get User Mentions
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_mention

GET /twitter/user/mentions
get tweet mentions by user screen name.Each page returns exactly 20 mentions. Use cursor for pagination. Order by mention time desc



# Get User Verified Followers
Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_verified_followers

GET /twitter/user/verifiedFollowers
Get user verified followers in reverse chronological order (newest first). Returns exactly 20 verified followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.$0.3 per 1000 followers



# Get ALL test Webhook/Websocket Tweet Filter Rules
Source: https://docs.twitterapi.io/api-reference/endpoint/get_webhook_rules

GET /oapi/tweet_filter/get_rules
Get all tweet filter rules.Rule can be used in webhook and websocket.You can also modify the rule in our web page.



# Like a tweet
Source: https://docs.twitterapi.io/api-reference/endpoint/like_tweet

POST /twitter/like_tweet
Like a tweet.Need to login first. Trial operation price: $0.001 per call.



# Login Step 2: by 2fa code
Source: https://docs.twitterapi.io/api-reference/endpoint/login_by_2fa

POST /twitter/login_by_2fa
Deprecated soon. Please use login V2 instead, as it is more stable.Login Step 2: by 2fa code.Trial operation price: $0.003 per call. 



# Login Step 1: by email or username
Source: https://docs.twitterapi.io/api-reference/endpoint/login_by_email_or_username

POST /twitter/login_by_email_or_username
Login Step 1: by email or username.Recommend to use email.Trial operation price: $0.003 per call. Please read the guide: https://twitterapi.io/blog/twitter-login-and-post-api-guide



# Remove a user from  monitor list
Source: https://docs.twitterapi.io/api-reference/endpoint/remove_user_to_monitor_tweet

POST /oapi/x_user_stream/remove_user_to_monitor_tweet
Remove a user from monitor real-time tweets.Please ref:https://twitterapi.io/twitter-stream



# Reweet a tweet
Source: https://docs.twitterapi.io/api-reference/endpoint/retweet_tweet

POST /twitter/retweet_tweet
Retweet a tweet.Need to login first. Trial operation price: $0.001 per call.



# Search user by keyword
Source: https://docs.twitterapi.io/api-reference/endpoint/search_user

GET /twitter/user/search
Search user by keyword



# Advanced Search
Source: https://docs.twitterapi.io/api-reference/endpoint/tweet_advanced_search

GET /twitter/tweet/advanced_search
Advanced search for tweets.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination.



# Update Webhook/Websocket Tweet Filter Rule
Source: https://docs.twitterapi.io/api-reference/endpoint/update_webhook_rule

POST /oapi/tweet_filter/update_rule
Update a tweet filter rule. You must set all parameters.



# Upload Image
Source: https://docs.twitterapi.io/api-reference/endpoint/upload_tweet_image

POST /twitter/upload_image
upload image to twitter.Need to login first. Trial operation price: $0.001 per call.



# Authentication
Source: https://docs.twitterapi.io/authentication

Learn how to authenticate your API requests using API keys

## API Authentication

Every API request requires authentication using an API key in the HTTP headers.

### Getting Your API Key

1. Log in to your [TwitterApiIO Dashboard](https://twitterapi.io/dashboard)
2. Find your API key displayed on the dashboard homepage

### Using Your API Key

All API requests must include the `x-api-key` header for authentication.

Header format:

```
x-api-key: YOUR_API_KEY
```

Example requests:

#### cURL

```bash  theme={null}
curl --location 'https://api.twitterapi.io/twitter/user/followings?userName=KaitoEasyAPI' \
--header 'x-api-key: my_test_xxxxx'
```

#### Python

```python  theme={null}
import requests

url = 'https://api.twitterapi.io/twitter/user/followings?userName=KaitoEasyAPI'
headers = {'x-api-key': 'my_test_xxxxx'}
response = requests.get(url, headers=headers)
print(response.json())
```

#### Java

```java  theme={null}
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

OkHttpClient client = new OkHttpClient();

Request request = new Request.Builder()
    .url("https://api.twitterapi.io/twitter/user/followings?userName=KaitoEasyAPI")
    .addHeader("x-api-key", "my_test_xxxxx")
    .build();

try (Response response = client.newCall(request).execute()) {
    System.out.println(response.body().string());
} catch (Exception e) {
    e.printStackTrace();
}
```


# Introduction
Source: https://docs.twitterapi.io/introduction

twitterapi.io docs.The best third-party Twitter API: reliable, high-performance, supports high QPS, and cost-effective.

* **Stability**: Proven with over 1000K API calls
* **Performance**: Average response time of 700ms
* **High QPS**: Supports up to 200 QPS per client
* **Ease of Use**: RESTful API design following standard OpenAPI specifications
* **Cost-effective pricing**:
  * \$0.15/1k tweets
  * \$0.18/1k user profiles
  * \$0.15/1k followers
  * Minimum charge: \$0.00015 per request (even if no data returned)
* **Special Offer**: Discounted rates for students and research institutions 🎓

## API Overview

Our Twitter API provides comprehensive endpoints for accessing Twitter data. Here's what you can do:

<CardGroup cols={2}>
  <Card title="Tweet Endpoints" icon="message" href="/api-reference/endpoint/get_tweet_by_ids">
    Search tweets, get tweet details, and analyze tweet metrics
  </Card>

  <Card title="User Endpoints" icon="user" href="/api-reference/endpoint/get_user_by_username">
    Get user profiles, followers, and following lists
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Tweet Search" icon="magnifying-glass" href="/api-reference/endpoint/tweet_advanced_search">
    Advanced search with filters for dates, keywords and more
  </Card>

  <Card title="User Networks" icon="users" href="/api-reference/endpoint/get_user_followers">
    Access follower and following relationships
  </Card>
</CardGroup>


