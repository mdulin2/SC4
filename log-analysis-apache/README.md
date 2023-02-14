# Log Analysis - Get a Grep!

We're a media company, not a bunch of computer nerds! Computers are computers, right? Get one of our software developers to find a suspicious request in our access logs.

There are many fake flags in the logs. The real one has the following format:

```
SC4{WWWW-XXXX-YYYY-ZZZZ}

Where:
WWWW = 10 random alphanumeric characters
XXXX = 4 random characters between A-F, including 'A' and 'F'
YYYY = 4 random numbers
ZZZZ = 10 random alphanumeric characters 
```

The flag is case-sensitive.

## Setup

Upload and provide a link to `challenge.zip`, which contains 10 log files, each containing 10,000 lines.

## Solution

Flag: `SC4{wH3rEs0the-BEEF-1337-sp0k4n3CyB}`

Unzip `challenge.zip`, and in the directory containing the extracted log files, do:

```
grep -E '[a-zA-Z0-9]{10}-[A-F]{4}-\d{4}-[a-zA-Z0-9]{10}' challenge*.log
```

There is only one string that matches this. That is the flag.

```
challenge7.log:156.207.146.191 - huel8466 [23/Jan/2023:12:23:55 -0800] "TRACE SC4{wH3rEs0the-BEEF-1337-sp0k4n3CyB} HTTP/2.0" 201 14958 "https://www.forwardinfomediaries.org/clicks-and-mortar/transparent/distributed/mindshare" "Opera/9.49 (Macintosh; PPC Mac OS X 10_9_8; en-US) Presto/2.10.222 Version/10.00"
```

Notice TRACE? It's a valid HTTP verb, but it's very rarely implemented. It simply reflects the full request back to the requestor, enabling attacks such as bypassing HttpOnly to steal cookies using scripts, hence why it's rarely implemented. A presence of this HTTP verb usually indicates that there are shenanigans afoot and the requestor is sussy wussy.

So there's an alternative solution: simply search for "TRACE".

