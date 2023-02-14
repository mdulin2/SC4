# Solutions

Flag: `SC4{g3t-th3-tick3ts-sw1ftly}`

This is a botting/scripting challenge.

To get the flag, a request to purchase a ticket must be processed within 100 milliseconds of the countdown timer going to 0.

This can be achieved with simple scripting. Firefox and Chrome both have a Network tab from which the POST request for a ticket
purchase can be copied as a cURL command. Repeat the command many times when the countdown is about the reach zero:

Example using `repeat` in zsh:

```
repeat 100 {
curl 'http://localhost:5002/' -X POST \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'Cookie: session=valid_cookie_here' \
    --data-raw 'quantity=1'
}
```
