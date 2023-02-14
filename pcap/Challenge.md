## PCAP

## Part 1
- We've captured some suspicious activities from our employee, so we captured some of his network packets. Let's see if he
had attempted to log into our super-secure FTP server. Using Wireshark or a similar tool, analyze the packet captures to
find the password used in an FTP login attempt.

- Hint:
  - Try "Follow TCP stream"; if you do this on any packet from an FTP session, you can see the whole session! The tricky
    part is finding the packets of interest.

## Part 2
We think this employee is keeping secrets from us, which is explicitly disallowed per our employee handbook. Looks like he
downloaded something super secret yet super safe. Find out what it is that he downloaded, and deliver those secrets to us!
Thank you, your loyalty shall be rewarded.

- Hint:
  - FTP is a plaintext protocol; file transfers appear in Wireshark appear as a separate protocol, FTP-DATA.
  - Files have "magic bytes", bytes at the beginning of the file indicating its format. For JPEG, it's 0xF8D8. For ZIP, it's "PK".