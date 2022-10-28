<!DOCTYPE html>
<html>
<head>
<title>搜尋</title>
</head>
<body>

<?php
// define variables and set to empty values
$GS = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $GS = $_POST['GS']
	$string = explode(" ", $GS);
    $result = "https://scholar.google.com.tw/scholar?hl=zh-TW&as_sdt=0%2C5&q=".$string[0]."+".$string[1]."+".$string[2]."+".$string[3];
    header ($result);
	
}
?>

<form method="post">
 <p>Google Scholar<input type="text" name="GS">
 </p>

 
 <p><input type="submit" value="送出"></p>
 
</form>

</body>
</html>