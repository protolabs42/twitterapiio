# Twitterapiio - Users

**Pages:** 10

---

## Remove a user from  monitor list

**URL:** llms-txt#remove-a-user-from--monitor-list

Source: https://docs.twitterapi.io/api-reference/endpoint/remove_user_to_monitor_tweet

POST /oapi/x_user_stream/remove_user_to_monitor_tweet
Remove a user from monitor real-time tweets.Please ref:https://twitterapi.io/twitter-stream

---

## Get User Info

**URL:** llms-txt#get-user-info

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_by_username

get /twitter/user/info
Get unser info by screen name

---

## Get User Verified Followers

**URL:** llms-txt#get-user-verified-followers

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_verified_followers

GET /twitter/user/verifiedFollowers
Get user verified followers in reverse chronological order (newest first). Returns exactly 20 verified followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.$0.3 per 1000 followers

---

## Get User Followings

**URL:** llms-txt#get-user-followings

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_followings

GET /twitter/user/followings
Get user followings. Each page returns exactly 200 followings. Use cursor for pagination.Sorted by follow date. Most recent followings appear on the first page.

---

## Get User Mentions

**URL:** llms-txt#get-user-mentions

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_mention

GET /twitter/user/mentions
get tweet mentions by user screen name.Each page returns exactly 20 mentions. Use cursor for pagination. Order by mention time desc

---

## Get User Followers

**URL:** llms-txt#get-user-followers

Source: https://docs.twitterapi.io/api-reference/endpoint/get_user_followers

GET /twitter/user/followers
Get user followers in reverse chronological order (newest first). Returns exactly 200 followers per page, sorted by follow date. Most recent followers appear on the first page. Use cursor for pagination through the complete followers list.

---

## Batch Get User Info By UserIds

**URL:** llms-txt#batch-get-user-info-by-userids

Source: https://docs.twitterapi.io/api-reference/endpoint/batch_get_user_by_userids

get /twitter/user/batch_info_by_ids
Batch get user info by user ids. Pricing:

- Single user request: 18 credits per user
- Bulk request (100+ users): 10 credits per user

Note: For cost optimization, we recommend batching requests when fetching multiple user profiles.

---

## Login Step 1: by email or username

**URL:** llms-txt#login-step-1:-by-email-or-username

Source: https://docs.twitterapi.io/api-reference/endpoint/login_by_email_or_username

POST /twitter/login_by_email_or_username
Login Step 1: by email or username.Recommend to use email.Trial operation price: $0.003 per call. Please read the guide: https://twitterapi.io/blog/twitter-login-and-post-api-guide

---

## Check Follow Relationship

**URL:** llms-txt#check-follow-relationship

Source: https://docs.twitterapi.io/api-reference/endpoint/check_follow_relationship

get /twitter/user/check_follow_relationship
Check if the user is following/followed by the target user. Trial operation price: 100 credits per call.

---

## Get List Followers

**URL:** llms-txt#get-list-followers

Source: https://docs.twitterapi.io/api-reference/endpoint/get_list_followers

GET /twitter/list/followers
Get followers of a list. Page size is 20.

---
