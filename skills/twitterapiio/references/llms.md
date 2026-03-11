# KaitoTwitterAPI

## Docs

- [Add  a twitter user to monitor his tweets](https://docs.twitterapi.io/api-reference/endpoint/add_user_to_monitor_tweet.md): Add a user to monitor real-time tweets.Monitor tweets from specified accounts, including directly sent tweets, quoted tweets, reply tweets, and retweeted tweets. Please ref:https://twitterapi.io/twitter-stream
- [Add Webhook/Websocket Tweet Filter Rule](https://docs.twitterapi.io/api-reference/endpoint/add_webhook_rule.md): Add a tweet filter rule. Default rule is not activated.You must call update_rule to activate the rule.
- [Batch Get User Info By UserIds](https://docs.twitterapi.io/api-reference/endpoint/batch_get_user_by_userids.md): Batch get user info by user ids. Pricing:

- Single user request: 18 credits per user
- Bulk request (100+ users): 10 credits per user

Note: For cost optimization, we recommend batching requests when fetching multiple user profiles.
- [Check Follow Relationship](https://docs.twitterapi.io/api-reference/endpoint/check_follow_relationship.md): Check if the user is following/followed by the target user. Trial operation price: 100 credits per call.
- [Post/reply/quote a tweet](https://docs.twitterapi.io/api-reference/endpoint/create_tweet.md): Create a tweet.Need to login first.Trial operation price: $0.001 per call.
- [Delete Webhook/Websocket Tweet Filter Rule](https://docs.twitterapi.io/api-reference/endpoint/delete_webhook_rule.md): Delete a tweet filter rule. You must set all parameters.
- [Search Tweets From All Community ](https://docs.twitterapi.io/api-reference/endpoint/get_all_community_tweets.md): get tweets from all communities,each page returns up to 20 tweets. Use cursor for pagination.
- [Get Article](https://docs.twitterapi.io/api-reference/endpoint/get_article.md): get article by tweet id. cost 100 credit per article
- [Get Community Info By Id](https://docs.twitterapi.io/api-reference/endpoint/get_community_by_id.md): Get community info by community id. Price: 20 credits per call. Note: This API is a bit slow, we are still optimizing it.
- [Get Community Members](https://docs.twitterapi.io/api-reference/endpoint/get_community_members.md): Get members of a community. Page size is 20.
- [Get Community Moderators](https://docs.twitterapi.io/api-reference/endpoint/get_community_moderators.md): Get moderators of a community. Page size is 20.
- [Get Community Tweets](https://docs.twitterapi.io/api-reference/endpoint/get_community_tweets.md): Get tweets of a community. Page size is 20. Order by creation time desc. 
- [Get List Followers](https://docs.twitterapi.io/api-reference/endpoint/get_list_followers.md): Get followers of a list. Page size is 20.
- [Get List Members](https://docs.twitterapi.io/api-reference/endpoint/get_list_members.md): Get members of a list. Page size is 20.
- [Get My Account Info](https://docs.twitterapi.io/api-reference/endpoint/get_my_info.md): Get my info
- [Get Trends](https://docs.twitterapi.io/api-reference/endpoint/get_trends.md): Get trends by woeid
- [Get Tweets by IDs](https://docs.twitterapi.io/api-reference/endpoint/get_tweet_by_ids.md): get tweet by tweet ids
- [Get Tweet Quotations](https://docs.twitterapi.io/api-reference/endpoint/get_tweet_quote.md): get tweet quotes by tweet id.Each page returns exactly 20 quotes. Use cursor for pagination. Order by quote time desc
- [Get Tweet Replies](https://docs.twitterapi.io/api-reference/endpoint/get_tweet_reply.md): get tweet replies by tweet id.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination. Order by reply time desc
- [Get Tweet Retweeters](https://docs.twitterapi.io/api-reference/endpoint/get_tweet_retweeter.md): get tweet retweeters by tweet id.Each page returns about 100 retweeters. Use cursor for pagination. Order by retweet time desc
- [Get Tweet Thread Context](https://docs.twitterapi.io/api-reference/endpoint/get_tweet_thread_context.md): Get the thread context of a tweet.Suppose a tweet thread consists of t1, t2 (replying to t1), t3 (replying to t2), and t4, t5, t6 (all replying to t3). If we provide an API where you input t3 and receive t1, t2, t3, t4, t5, t6.Pagination is supported.The pagination size cannot be set (due to Twitter's limitations), and the data returned per page is not fixed.
- [Get User Info](https://docs.twitterapi.io/api-reference/endpoint/get_user_by_username.md): Get unser info by screen name
- [Get User Followers](https://docs.twitterapi.io/api-reference/endpoint/get_user_followers.md): Get user followers in reverse chronological order (newest first). Returns exactly 200 followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.
- [Get User Followings](https://docs.twitterapi.io/api-reference/endpoint/get_user_followings.md): Get user followings. Each page returns exactly 200 followings. Use cursor for pagination.Sorted by follow date. Most recent followings appear on the first page. 
- [Get User Last Tweets](https://docs.twitterapi.io/api-reference/endpoint/get_user_last_tweets.md): Retrieve tweets by user name.Sort by created_at. Results are paginated, with each page returning up to 20 tweets.If you only need to fetch the latest tweets from a single user very frequently, do not use this API—it will cost you a lot. Instead, please refer to https://twitterapi.io/blog/how-to-monitor-twitter-accounts-for-new-tweets-in-real-time. If you have more than 20 Twitter accounts requiring real-time tweet updates, use https://twitterapi.io/twitter-stream which is the most cost-effective solution.
- [Get User Mentions](https://docs.twitterapi.io/api-reference/endpoint/get_user_mention.md): get tweet mentions by user screen name.Each page returns exactly 20 mentions. Use cursor for pagination. Order by mention time desc
- [Get User Verified Followers](https://docs.twitterapi.io/api-reference/endpoint/get_user_verified_followers.md): Get user verified followers in reverse chronological order (newest first). Returns exactly 20 verified followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.$0.3 per 1000 followers
- [Get ALL test Webhook/Websocket Tweet Filter Rules](https://docs.twitterapi.io/api-reference/endpoint/get_webhook_rules.md): Get all tweet filter rules.Rule can be used in webhook and websocket.You can also modify the rule in our web page.
- [Like a tweet](https://docs.twitterapi.io/api-reference/endpoint/like_tweet.md): Like a tweet.Need to login first. Trial operation price: $0.001 per call.
- [Login Step 2: by 2fa code](https://docs.twitterapi.io/api-reference/endpoint/login_by_2fa.md): Deprecated soon. Please use login V2 instead, as it is more stable.Login Step 2: by 2fa code.Trial operation price: $0.003 per call. 
- [Login Step 1: by email or username](https://docs.twitterapi.io/api-reference/endpoint/login_by_email_or_username.md): Login Step 1: by email or username.Recommend to use email.Trial operation price: $0.003 per call. Please read the guide: https://twitterapi.io/blog/twitter-login-and-post-api-guide
- [Remove a user from  monitor list](https://docs.twitterapi.io/api-reference/endpoint/remove_user_to_monitor_tweet.md): Remove a user from monitor real-time tweets.Please ref:https://twitterapi.io/twitter-stream
- [Reweet a tweet](https://docs.twitterapi.io/api-reference/endpoint/retweet_tweet.md): Retweet a tweet.Need to login first. Trial operation price: $0.001 per call.
- [Search user by keyword](https://docs.twitterapi.io/api-reference/endpoint/search_user.md): Search user by keyword
- [Advanced Search](https://docs.twitterapi.io/api-reference/endpoint/tweet_advanced_search.md): Advanced search for tweets.Each page returns up to 20 replies(Sometimes less than 20,because we will filter out ads or other not  tweets). Use cursor for pagination.
- [Update Webhook/Websocket Tweet Filter Rule](https://docs.twitterapi.io/api-reference/endpoint/update_webhook_rule.md): Update a tweet filter rule. You must set all parameters.
- [Upload Image](https://docs.twitterapi.io/api-reference/endpoint/upload_tweet_image.md): upload image to twitter.Need to login first. Trial operation price: $0.001 per call.
- [Authentication](https://docs.twitterapi.io/authentication.md): Learn how to authenticate your API requests using API keys
- [Introduction](https://docs.twitterapi.io/introduction.md): twitterapi.io docs.The best third-party Twitter API: reliable, high-performance, supports high QPS, and cost-effective.
