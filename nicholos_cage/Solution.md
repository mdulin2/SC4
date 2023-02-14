## Solution
- SQL is used for querying databases.
- Input commonly comes directly from users. This input is combined with the SQL query to do something on the website.
- Because the queries are being dynamically generated it is possible inject other characters into the query that can alter the query itself.
- The query looks like this: `select * FROM login WHERE username = 'input1' AND password = 'input2'`.
- By adding single quotes we can alter the query. Putting a single ' into the login form will return an error message (notice that 400 error).
- Now, in order to alter the query so that we login, we need to create a valid query that circumvents all of the logic!
- Adding a single quote in the username will close this string. Then, we can have a value that always returns true. Finally, we will use a comment in order to make the rest of the query useless.

### Solution 1
- Login as SOME user. 
- `' OR 1=1 --`
- This input is in the username.
- `select * FROM login WHERE username = '' OR 1=1 -- AND password = 'input2'` is how the query actually turns out
- Flag: SC4{An0therM0vi3_sTAr1ng_Mr.CaGGe!}

### Solution 2
- Login as the admin user.
- ``admin`` for the username 
- `' OR 1=1 --` for the password
- `select * FROM login WHERE username = 'admin' AND password = ''OR 1=1 --'` is how the query actually turns out. 
- Flag: SC4{An0therM0vi3_sTAr1ng_Mr.CaGGe!}