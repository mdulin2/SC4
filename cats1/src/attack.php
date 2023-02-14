<?php

$fh = fopen('/flag.txt','r');
while ($line = fgets($fh)) {

   echo($line);
}
fclose($fh);
?>
