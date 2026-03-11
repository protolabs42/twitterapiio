# Twitterapiio - Tweets

**Pages:** 18

---

## Update Webhook/Websocket Tweet Filter Rule

**URL:** llms-txt#update-webhook/websocket-tweet-filter-rule

Source: https://docs.twitterapi.io/api-reference/endpoint/update_webhook_rule

POST /oapi/tweet_filter/update_rule
Update a tweet filter rule. You must set all parameters.

---

## Add  a twitter user to monitor his tweets

**URL:** llms-txt#add--a-twitter-user-to-monitor-his-tweets

Source: https://docs.twitterapi.io/api-reference/endpoint/add_user_to_monitor_tweet

POST /oapi/x_user_stream/add_user_to_monitor_tweet
Add a user to monitor real-time tweets.Monitor tweets from specified accounts, including directly sent tweets, quoted tweets, reply tweets, and retweeted tweets. Please ref:https://twitterapi.io/twitter-stream

---

## Post/reply/quote a tweet

**URL:** llms-txt#post/reply/quote-a-tweet

Source: https://docs.twitterapi.io/api-reference/endpoint/create_tweet

POST /twitter/create_tweet
Create a tweet.Need to login first.Trial operation price: $0.001 per call.

---

## Get Tweets by IDs

**URL:** llms-txt#get-tweets-by-ids

Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_by_ids

GET /twitter/tweets
get tweet by tweet ids

---

## Get Tweet Retweeters

**URL:** llms-txt#get-tweet-retweeters

Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_retweeter

GET /twitter/tweet/retweeters
get tweet retweeters by tweet id.Each page returns about 100 retweeters. Use cursor for pagination. Order by retweet time desc

---

## Get Tweet Thread Context

**URL:** llms-txt#get-tweet-thread-context

Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_thread_context

GET /twitter/tweet/thread_context
Get the thread context of a tweet.Suppose a tweet thread consists of t1, t2 (replying to t1), t3 (replying to t2), and t4, t5, t6 (all replying to t3). If we provide an API where you input t3 and receive t1, t2, t3, t4, t5, t6.Pagination is supported.The pagination size cannot be set (due to Twitter's limitations), and the data returned per page is not fixed.

---

## Add Webhook/Websocket Tweet Filter Rule

**URL:** llms-txt#add-webhook/websocket-tweet-filter-rule

Source: https://docs.twitterapi.io/api-reference/endpoint/add_webhook_rule

POST /oapi/tweet_filter/add_rule
Add a tweet filter rule. Default rule is not activated.You must call update_rule to activate the rule.

---

## Advanced Search

**URL:** llms-txt#advanced-search

Source: https://docs.twitterapi.io/api-reference/endpoint/tweet_advanced_search

GET /twitter/tweet/advanced_search
Advanced search for tweets.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination.

---

## Delete Webhook/Websocket Tweet Filter Rule

**URL:** llms-txt#delete-webhook/websocket-tweet-filter-rule

Source: https://docs.twitterapi.io/api-reference/endpoint/delete_webhook_rule

DELETE /oapi/tweet_filter/delete_rule
Delete a tweet filter rule. You must set all parameters.

---

## Get ALL test Webhook/Websocket Tweet Filter Rules

**URL:** llms-txt#get-all-test-webhook/websocket-tweet-filter-rules

Source: https://docs.twitterapi.io/api-reference/endpoint/get_webhook_rules

GET /oapi/tweet_filter/get_rules
Get all tweet filter rules.Rule can be used in webhook and websocket.You can also modify the rule in our web page.

---

## Get Tweet Replies

**URL:** llms-txt#get-tweet-replies

Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_reply

GET /twitter/tweet/replies
get tweet replies by tweet id.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination. Order by reply time desc

---

## Get Tweet Quotations

**URL:** llms-txt#get-tweet-quotations

Source: https://docs.twitterapi.io/api-reference/endpoint/get_tweet_quote

GET /twitter/tweet/quotes
get tweet quotes by tweet id.Each page returns exactly 20 quotes. Use cursor for pagination. Order by quote time desc

---

## Search Tweets From All Community

**URL:** llms-txt#search-tweets-from-all-community

Source: https://docs.twitterapi.io/api-reference/endpoint/get_all_community_tweets

GET /twitter/community/get_tweets_from_all_community
get tweets from all communities,each page returns up to 20 tweets. Use cursor for pagination.

---

## Search user by keyword

**URL:** llms-txt#search-user-by-keyword

Source: https://docs.twitterapi.io/api-reference/endpoint/search_user

GET /twitter/user/search
Search user by keyword

---

## Reweet a tweet

**URL:** llms-txt#reweet-a-tweet

Source: https://docs.twitterapi.io/api-reference/endpoint/retweet_tweet

POST /twitter/retweet_tweet
Retweet a tweet.Need to login first. Trial operation price: $0.001 per call.

---

## Get Community Tweets

**URL:** llms-txt#get-community-tweets

Source: https://docs.twitterapi.io/api-reference/endpoint/get_community_tweets

GET /twitter/community/tweets
Get tweets of a community. Page size is 20. Order by creation time desc.

---

## Like a tweet

**URL:** llms-txt#like-a-tweet

Source: https://docs.twitterapi.io/api-reference/endpoint/like_tweet

POST /twitter/like_tweet
Like a tweet.Need to login first. Trial operation price: $0.001 per call.

---

## Get User Last Tweets

**URL:** llms-txt#get-user-last-tweets

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_last_tweets

GET /twitter/user/last_tweets
Retrieve tweets by user name.Sort by created_at. Results are paginated, with each page returning up to 20 tweets.If you only need to fetch the latest tweets from a single user very frequently, do not use this API—it will cost you a lot. Instead, please refer to https://twitterapi.io/blog/how-to-monitor-twitter-accounts-for-new-tweets-in-real-time. If you have more than 20 Twitter accounts requiring real-time tweet updates, use https://twitterapi.io/twitter-stream which is the most cost-effective solution.

---
