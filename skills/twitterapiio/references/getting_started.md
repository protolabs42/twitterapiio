# Twitterapiio - Getting Started

**Pages:** 2

---

## Authentication

**URL:** llms-txt#authentication

**Contents:**
- API Authentication
  - Getting Your API Key
  - Using Your API Key

Source: https://docs.twitterapi.io/authentication

Learn how to authenticate your API requests using API keys

## API Authentication

Every API request requires authentication using an API key in the HTTP headers.

### Getting Your API Key

1. Log in to your [TwitterApiIO Dashboard](https://twitterapi.io/dashboard)
2. Find your API key displayed on the dashboard homepage

### Using Your API Key

All API requests must include the `x-api-key` header for authentication.

**Examples:**

Example 1 (unknown):
```unknown
x-api-key: YOUR_API_KEY
```

Example 2 (unknown):
```unknown
#### Python
```

Example 3 (unknown):
```unknown
#### Java
```

---

## Introduction

**URL:** llms-txt#introduction

**Contents:**
- API Overview

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

---
