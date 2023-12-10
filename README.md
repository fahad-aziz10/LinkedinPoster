# LinkedinPoster


## Step 1: Enter cookies values

Open bard.google.com and login to start your session. Press F12 to inspect and go to application tab and copy the following values and paste in the placeholders in file 'keys.json'. You can visit repo https://github.com/dsdanielpark/Bard-API for further clarification.

```python
cookie_dict = {
    "__Secure-1PSID": "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "__Secure-1PSIDTS": "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "__Secure-1PSIDCC": "xxxxxxxxxxxxxxxxxxxxxxxxx"
    # Any cookie values you want to pass session object.
}
```

## Step 2: Get Linkedin Access token 

Get Linkedin access token and paste it in the placeholder.
```python
access_token = "xxxxxxxxxxxxxxxxxxxxxxxxx"
```
## Step 3: Cater prompt

In the prompt give the appropriate and relevent prompt as your own requirement and taste.
```python
BardOutput = (bard.get_answer("Act as a professional Linkedin content writer who has expertise in writing authentic and engaging content. You will write an linkedin post on "+str(topic)+",trying to maximize likes and comments. You can use historical stories as well as future predictions.")['content'])
```