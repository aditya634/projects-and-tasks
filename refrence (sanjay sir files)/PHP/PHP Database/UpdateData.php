<!-- Query : INSERT INTO `students` (`name`, `email`, `password`, `std`, `phone`) VALUES ('Admin', 'admin@test.com', '12345', '12', '1234567890'); -->

<?php
if (!isset($_POST["submitData"])) {
    // echo "Not Clicked !!";
    header("Location:updateForm.html");
} else {
    // print_r($_POST);

    // echo "Button Clicked !!";

    // echo "uName : ".$_POST["uName"];
    // echo "uEmail : ".$_POST["uEmail"];
    // echo "uPassword : ".$_POST["uPassword"];
    // echo "uStd : ".$_POST["uStd"];
    // echo "uPhone : ".$_POST["uPhone"];

    $oldEmail = $_POST["oldEmail"];
    $newName = $_POST["uName"];
    $newEmail = $_POST["uEmail"];
    $newPassword = $_POST["uPassword"];
    $newStd = $_POST["uStd"];
    $newPhone = $_POST["uPhone"];

    $host = 'localhost:3306';
    $user = 'root';
    $pass = '';
    $dbname = 'studRecords';

    $conn = mysqli_connect($host, $user, $pass, $dbname);
    if (!$conn) {
        die('Could not connect: ' . mysqli_connect_error());
    }
    // echo 'Connected successfully<br/>';

    $sql = "UPDATE `students` SET `name` = '".$newName."', `email` = '".$newEmail."', `password` = '".$newPassword."', `std` = '".$newStd."', `phone` = '".$newPhone."' WHERE `students`.`email` = '".$oldEmail."'"; 
    if (mysqli_query($conn, $sql)) {
        echo "<script>alert('Record Updated successfully');</script>";
        echo "Record Updated";
        echo "<a href='updateForm.html'> Go Back </a>";
        // header("Location:updateForm.html");
    } else {
        echo "<script>alert('Could not Updated record: " . mysqli_error($conn) . "');</script>";
        echo "Record Could not Updated";
        echo "<a href='updateForm.html'> Go Back </a>";
        // header("Location:updateForm.html");
    }

    mysqli_close($conn);
}
