# Solution 
The goal of the challenge is to get the passcode for the server. Using a true brute force (10 ^ 9 possibilities) is too many possibilities. However, the verification of the passcode leaks data via a side channel. A side channel is information that exposing data that is not an issue with the algorithm itself but with the implementation. Common examples of this are timing information (this challenge), power consumption, electromagnetic information or sound.

In this case, the side channel is time. In order to solve this challenge, use the timing difference between a correct character and an incorrect character. There is a 1 second sleep on each correct character guess. 
For example, ‘./client 0XXXXXXXX’ will return instantly. However, ‘./client 1XXXXXXXX’ will return about a second later because the character 1 is the correct character for the first character in the passcode.

The maximum amount of attempts to solve this problem has gone from 10 ^ 9 to 9 x 10, or just 90! This challenge can be automated (such as the solve.py file in this repo) or done by hand during the timing differences between two calls with the time binary as shown above.

Flag: 140329823
