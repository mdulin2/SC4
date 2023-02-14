<html>
<head> 
	<link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
        <center>
        <h1>
        Cats3!
        </h1>
        </center>
<?php

// Get all of the pictures of wonderful cats from the pictures directory.
$dir    = '/var/www/html/text/';
$allFiles = scandir($dir);
$files = array_diff($allFiles, array('.','..'));

// The path of the picture to read
$file_path = htmlspecialchars($_GET["path"]);


// Find the ID of the image
$index = 0;
$file_id = 0;
foreach ($files as $key => $pic){
	if(str_ends_with($file_path, $pic)){
		$file_id = $index;
	}
	
	$index = $index + 1; 
}

// Iterate through the directory,to display correct information
$index = 0;

foreach ($files as $key => $text_file){
	
	// Display the previous click link
	if($file_id == $index + 1 ){
		echo '<a href ="cats.php?path='.($text_file).'">See Previous   </a>';
	}

	// Displays our text
	elseif($file_id == $index){
		# Display the data!
		$myfile = fopen($dir . $file_path, "r"); 
		echo "<center><p>" . fread($myfile,filesize($dir . $file_path)); "</p></center>"; 		
	}

	// Display the next click link
	elseif($file_id == $index - 1){
		echo '<a href ="cats.php?path='.($text_file).'"> See Next   </a>';
	}
	
	$index = $index +1;
}

?> 
<p>
	<center>
		<a href= "upload.php">Click here to upload cats!</a>
	</center>
</p>
</body>
</html>
