<!DOCTYPE html>
<html>
<head> 
        <link rel="stylesheet" href="style.css" type="text/css">
  <title>Upload your files</title>
</head>
<body>
  <form enctype="multipart/form-data" action="upload.php" method="POST">
    <p>Upload your file</p>
    <input type="file" name="uploaded_file"></input><br />
    <input type="submit" value="Upload"></input>
  </form>
<p>
	<a href="cats.php?path=./text/data.txt">Back to Cats!</a>
</p>
</body>
</html>
<?PHP

echo "Filename: " . $_FILES['uploaded_file']['name'];

// Logic for uploading a file
  if(!empty($_FILES['uploaded_file']))
  {

    echo $_FILES['uploaded_file']['name']; 
    if(!str_ends_with($_FILES['uploaded_file']['name'],'.txt') and !str_ends_with($_FILES['uploaded_file']['name'],'.md')){
      echo "<p>Error in upload...illegal file</p>";    
      exit;
    }

	  // The insert path
    $path = "/var/www/html/text/";
    $path = $path . basename( $_FILES['uploaded_file']['name']);
	
    // Add the actual file
    if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) {
      echo "<p>Your text about cats has been written!</p>"; 
    } else{	
	    echo "<p>Error in upload...</p>";    
    }
  }
?>
