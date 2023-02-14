## Solution - Cats 3
- Prior to this, we were specifying the URL and total file location being used. 
- Now, a string is being concatenated with another string to get the path. 
- ``/var/www/html/text/`` + filename in URL = file to grab
- We can use ``../`` repeatedly to *traverse* from the ``text`` directory all the way to root!
- Directory traversal in the URL - ``path=../../../../../../flag.txt``
- Flag: SC4{I_Just_Want_T0_Sh0w_oFf_My_cats_plzzz_st0p!}