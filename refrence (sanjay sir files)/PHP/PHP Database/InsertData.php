<!-- Query : INSERT INTO `students` (`name`, `email`, `password`, `std`, `phone`) VALUES ('Admin', 'admin@test.com', '12345', '12', '1234567890'); -->

<?php
if (!isset($_POST["submitData"])) {
    // echo "Not Clicked !!";
    header("Location:InsertForm.html");
} else {
    // print_r($_POST);

    echo "Button Clicked !!";

    // echo "uName : ".$_POST["uName"];
    // echo "uEmail : ".$_POST["uEmail"];
    // echo "uPassword : ".$_POST["uPassword"];
    // echo "uStd : ".$_POST["uStd"];
    // echo "uPhone : ".$_POST["uPhone"];

    $Name = $_POST["uName"];
    $Email = $_POST["uEmail"];
    $Password = $_POST["uPassword"];
    $Std = $_POST["uStd"];
    $Phone = $_POST["uPhone"];

    $host = 'localhost:3306';
    $user = 'root';
    $pass = '';
    $dbname = 'studRecords';

    $conn = mysqli_connect($host, $user, $pass, $dbname);
    if (!$conn) {
        die('Could not connect: ' . mysqli_connect_error());
    }
    echo 'Connected successfully<br/>';

    $sql = "INSERT INTO `students` (`name`, `email`, `password`, `std`, `phone`) VALUES ('" . $Name . "', '" . $Email . "', '" . $Password . "', '" . $Std . "', '" . $Phone . "');";
    if (mysqli_query($conn, $sql)) {
        echo "<script>alert('Record inserted successfully');</script>";
        echo "Record Inserted";
        echo "<a href='InsertForm.html'> Go Back </a>";
        // header("Location:InsertForm.html");
    } else {
        echo "<script>alert('Could not insert record: " . mysqli_error($conn) . "');</script>";
        echo "Record Could not Inserted";
        echo "<a href='InsertForm.html'> Go Back </a>";
        // header("Location:InsertForm.html");
    }

    mysqli_close($conn);
}
