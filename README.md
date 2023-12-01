
# Tiktok Marketing and Data Management Software

Full stack software developed in Python using Flet for GUI and Mongo DB for storing data.

## Browse

Browse through your collected marketing data by table with the ability to filter and sort based on the 15 collected fields.

## Scraper
TikTok Scraper that pulls all videos made with a provided Sound ID. Data scraped includes the following fields: username, secUid, link,nickname, followers, posts under sound, bio,posts in last 28 days, median views in last 28 days, mean views in last 28 days, median likes in last 28 days, median comments in last 28 days, median views per follower, tags, index


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Authors

- [@AidanAlr](https://www.github.com/AidanAlr)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

