<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP If-Else</title>
</head>
<link rel="stylesheet" href="style.css">
<body>
    <div class="container">
        <h1>Lets Learn about PHP If-Else Condition</h1> 
        <p><b>Your Voting Status : </p>
        <?php
            $User_Age=-90;
            if($User_Age>=18)
            {
                echo "You Can Vote !";
            }
            else if($User_Age<0)
            {
                echo "Invalid Age !";
            }
            else
            {
                echo "You Cannot Vote !";
                echo "<br>Wait for ";
                echo 18-$User_Age;
                echo " Years";
            }
        ?>
        </b>
    </div>
</body>
</html>