## Solution 

This challenge, as shown by the title, is about the *Cesar Cipher*. This is an ancient form of encryption done by assigning each character a number (0-25) then adding a number to this value for the encryption. After the transformation, turn the number back into a number.

As an example, the letter 'A' would become 1. If the key is 3, then we would move from 1 to 4, which is 'D'. If the addition is larger than 26, then simply wrap around back to 1 via the modulus operation. To decrypt, reverse the process by subtracting by the key.

The key in our case is 13. The first character is 'F'. So, we move from 5 ('F') and subtract 13 with modulus 25 to give us 19. 19 on the character for the cease cipher is S, which is the first letter of the message. For 'P'(16), we subtract 13 in order to get 'C' (3). Do these operations for EVERY one of the alphabetic characters to get the message.

Flag: SC4{CesarSaladsAreSecure!}
