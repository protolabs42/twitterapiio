---
name: twitterapiio
description: TwitterAPI.io REST API documentation. Use when working with Twitter data retrieval, tweet search, user profiles, followers, lists, communities, and Twitter API integration.
---

# TwitterAPI.io

## When to Use This Skill

Trigger this skill when:
- Fetching Twitter data (tweets, users, followers, trends)
- Implementing Twitter search functionality
- Building social media monitoring tools
- Analyzing Twitter user networks and relationships
- Creating Twitter bots or automation
- Setting up real-time Twitter streams with webhooks
- Working with Twitter communities and lists
- Integrating Twitter data into applications

## Quick Reference

### Authentication
All API requests require the `x-api-key` header:

```http
x-api-key: YOUR_API_KEY
```

The API key is available as the `TWITTERAPIIO_API_KEY` environment variable (set by the plugin config).
Use `$TWITTERAPIIO_API_KEY` in curl commands or `os.environ["TWITTERAPIIO_API_KEY"]` in Python.
Configure it in the plugin settings or get one from the [TwitterAPI.io Dashboard](https://twitterapi.io/dashboard).

### Common Endpoints

**Get Tweet by ID:**
```http
GET /twitter/tweets?ids=TWEET_ID_1,TWEET_ID_2
```

**Advanced Tweet Search:**
```http
GET /twitter/tweet/advanced_search?query=keyword&cursor=CURSOR
```
Returns up to 20 tweets per page with cursor pagination.

**Get User Info:**
```http
GET /twitter/user/info?username=SCREEN_NAME
```

**Get User Followers:**
```http
GET /twitter/user/followers?userId=USER_ID&cursor=CURSOR
```
Returns 200 followers per page, newest first.

**Get User Followings:**
```http
GET /twitter/user/followings?userId=USER_ID&cursor=CURSOR
```
Returns 200 followings per page, newest first.

**Tweet Replies:**
```http
GET /twitter/tweet/replies?tweetId=TWEET_ID&cursor=CURSOR
```
Returns up to 20 replies per page, newest first.

**Tweet Quotes:**
```http
GET /twitter/tweet/quotes?tweetId=TWEET_ID&cursor=CURSOR
```
Returns 20 quotes per page, newest first.

### Real-Time Streaming

**Add User to Monitor:**
```http
POST /oapi/x_user_stream/add_user_to_monitor_tweet
```
Monitor tweets from specific accounts in real-time.

**Add Tweet Filter Rule:**
```http
POST /oapi/tweet_filter/add_rule
```
Create webhook/websocket filters for tweet streaming.

**Get Filter Rules:**
```http
GET /oapi/tweet_filter/get_rules
```

## Key Concepts

1. **API Authentication** - All requests require `x-api-key` header with your API key from the dashboard. No OAuth flow needed.

2. **Cursor Pagination** - Most endpoints return data in pages with a `cursor` parameter. Save the cursor from the response to fetch the next page. Page sizes vary by endpoint (20-200 items).

3. **Rate Limits & Pricing** - Supports up to 200 QPS per client. Pricing: $0.15/1k tweets, $0.18/1k user profiles, $0.15/1k followers. Minimum charge: $0.00015 per request.

4. **Real-Time Streams** - Monitor specific users or use filter rules to receive tweets via webhook or WebSocket. Rules can be managed via API or web dashboard.

5. **Performance** - Average response time of 700ms. Proven with over 1000K API calls. Use batch endpoints (e.g., batch user info) for cost optimization.

## Working with This Skill

### Beginner Path

Start with authentication and basic data retrieval:
1. **references/getting_started.md** - Authentication, API overview, pricing
2. **references/tweets.md** - Get tweets by ID, basic search
3. **references/users.md** - Get user profiles and basic info

### Intermediate Path

Explore relationships and advanced search:
- **references/users.md** - Followers, followings, verified followers, follow relationships
- **references/tweets.md** - Advanced search, replies, quotes, retweeters, thread context
- **references/lists.md** - List management and members
- **references/communities.md** - Community tweets and members

### Advanced Path

Implement real-time monitoring and automation:
- **references/tweets.md** - Webhook/WebSocket filter rules, user monitoring streams
- **references/other.md** - Login API, tweet creation, advanced operations
- **references/trends.md** - Trending topics and content

## Reference Files

Comprehensive documentation organized by topic:

- **getting_started.md** (2 pages) - Authentication, API overview, pricing model
- **tweets.md** (18 pages) - Tweet retrieval, search, replies, quotes, real-time streams, webhooks
- **users.md** (10 pages) - User profiles, followers, followings, relationships, login
- **lists.md** (2 pages) - List operations, members, followers
- **communities.md** (2 pages) - Community tweets and members
- **trends.md** (1 page) - Trending topics
- **other.md** (4 pages) - Advanced features, login, tweet creation

**Navigation Tips:**
- Start with `getting_started.md` for authentication setup
- Use `tweets.md` for all tweet-related operations (search, replies, streams)
- Check `users.md` for user data and network analysis
- Refer to Quick Reference above for common API patterns
- All endpoints use RESTful design following OpenAPI specifications

**Pagination Pattern:**
Most endpoints use cursor-based pagination:
1. Make initial request without cursor
2. Response includes `cursor` field
3. Pass cursor in next request to get next page
4. Repeat until no cursor returned

**Cost Optimization:**
- Use batch endpoints when fetching multiple items (e.g., `batch_info_by_ids` for 100+ users)
- Bulk requests offer better pricing (10 credits vs 18 credits per user)
- Monitor your usage on the dashboard

<!-- SKILL AUTHORING NOTE:
This SKILL.md follows progressive disclosure principles:
- Level 1: Metadata (YAML) - always loaded (~100 words)
- Level 2: SKILL.md body - loaded when skill triggers (<500 lines)
- Level 3: references/ - loaded as needed (detailed docs)

Keep SKILL.md concise. Move detailed content to references/.
-->

<!-- DEGREES OF FREEDOM:
Documentation skills use MEDIUM freedom (templates + patterns):
- Provide structured examples (Quick Reference)
- Show common patterns (Code Examples)
- Guide navigation (Working with This Skill)
- Link to detailed references (Reference Files)

NOT low freedom (scripts) - users need flexibility
NOT high freedom (principles only) - users need concrete examples
-->
