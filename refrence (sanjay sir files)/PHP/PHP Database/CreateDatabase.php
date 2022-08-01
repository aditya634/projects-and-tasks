<?php
$host = 'localhost:3306';
$user = 'root';
$pass = '';
$conn = mysqli_connect($host, $user, $pass);
if (!$conn) {
    die('Could not connect: ' . mysqli_connect_error());
}
echo 'Connected successfully<br/>';

$sql = 'CREATE Database studRecords';
if (mysqli_query($conn, $sql)) {
    echo "Database studRecords created successfully.";
} else {
    echo "Sorry, database creation failed " . mysqli_error($conn);
}
mysqli_close($conn);
