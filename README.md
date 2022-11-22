# Get tweets

## Requirements

### Modules

To install all the requirements, run

```
pip install -r requirements.txt
```

### Tokens

The only required token is the bearer token, that can be obtained through the [Developer Portal](https://developer.twitter.com/).
With this token, create a .env file:

```
BEARER_TOKEN="<YOUR TOKEN>"
```

## Search Query

The query can be a single keyword, or a more advanced composition of search params.

**Pro Tip**

Use the twitter interface to create an Advanced Search query and use it in the code.

<img width="601" alt="image" src="https://user-images.githubusercontent.com/39441856/203329132-fc3ea4b2-64a4-4530-bdb8-7c1522a9e05c.png">

<img width="456" alt="image" src="https://user-images.githubusercontent.com/39441856/203329175-a7ef23b1-0d2a-4944-9607-774b009bedd9.png">

Query:
```
"world cup" lang:en
```


