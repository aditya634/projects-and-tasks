<!-- Query : INSERT INTO `students` (`name`, `email`, `password`, `std`, `phone`) VALUES ('Admin', 'admin@test.com', '12345', '12', '1234567890'); -->

<?php
if (!isset($_POST["submitData"])) {
    // echo "Not Clicked !!";
    header("Location:DeleteForm.html");
} else {
    // print_r($_POST);

    // echo "Button Clicked !!";

    // echo "uName : ".$_POST["uName"];
    // echo "uEmail : ".$_POST["uEmail"];
    // echo "uPassword : ".$_POST["uPassword"];
    // echo "uStd : ".$_POST["uStd"];
    // echo "uPhone : ".$_POST["uPhone"];

    $Email = $_POST["uEmail"];

    $host = 'localhost:3306';
    $user = 'root';
    $pass = '';
    $dbname = 'studRecords';

    $conn = mysqli_connect($host, $user, $pass, $dbname);
    if (!$conn) {
        die('Could not connect: ' . mysqli_connect_error());
    }
    // echo 'Connected successfully<br/>';

    $sql = "DELETE FROM `students` WHERE `students`.`email` = '".$Email."'"; 
    if (mysqli_query($conn, $sql)) {
        echo "<script>alert('Record Deleted ! successfully');</script>";
        echo "Record Deleted !";
        echo "<a href='DeleteForm.html'> Go Back </a>";
        // header("Location:DeleteForm.html");
    } else {
        echo "<script>alert('Could not Deleted ! record: " . mysqli_error($conn) . "');</script>";
        echo "Record Could not Deleted !";
        echo "<a href='DeleteForm.html'> Go Back </a>";
        // header("Location:DeleteForm.html");
    }

    mysqli_close($conn);
}
