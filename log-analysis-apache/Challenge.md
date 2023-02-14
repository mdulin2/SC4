## Challenge 

We're a media company, not a bunch of computer nerds! Get one of our computer guys to find the "suspicious request" in our access logs, whatever the heck that means!

There are many fake flags in the logs. The real one has the following format:

```
SC4{WWWW-XXXX-YYYY-ZZZZ}

Where:
WWWW = 10 random alphanumeric characters
XXXX = 4 random characters between A-F, including 'A' and 'F'
YYYY = 4 random numbers
ZZZZ = 10 random alphanumeric characters 
```

Hint:
- Regular expressions will help you here! `grep -E 'your regex here' challenge*.log`, or use a text editor with regex search capabilities!