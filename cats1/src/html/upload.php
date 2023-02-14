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
	<a href="cats.php?id=0">Back to Cats!</a>
</p>
</body>
</html>
<?PHP

echo "Filename: " . $_FILES['uploaded_file']['name'];

// Logic for uploading a file
  if(!empty($_FILES['uploaded_file']))
  {

	  // The insert path
    $path = "/var/www/html/pictures/";
    $path = $path . basename( $_FILES['uploaded_file']['name']);
	
    // Add the actual file
    if(move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) {
      echo "<p>The file ".  basename( $_FILES['uploaded_file']['name']). 
      " has been uploaded. Click <a href='pictures/". basename( $_FILES['uploaded_file']['name']) . "'>here <a/> to view the file!</p>";
    } else{	
	    echo "<p>Error in upload...</p>";    
    }
  }
?>
