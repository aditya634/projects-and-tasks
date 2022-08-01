<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP If-Else</title>
</head>
<style>
    *
    {
        margin:0;
        padding:0;
        box-sizing: border-box;
    }
    .container
    {
        max-width: 80%;
        background-color: rgb(250, 200, 208);
        margin:auto;
        padding: 25px;
    }
</style>
<body>
    <div class="container">
        <h1>Lets Learn about PHP Array</h1> 
        <?php
            $languages = array("Python","C++","PHP","NodeJs","Java","C");
            
            // Using Method {will understand more in detail later}
            echo "Number of elements in Array : ";
            echo count($languages);

            echo "<br><br>Language at location 0 : ";
            echo $languages[0];
            echo "<br>Language at location 1 : ";
            echo $languages[1];
            echo "<br>Language at location 2 : ";
            echo $languages[2];
            echo "<br>Language at location 3 : ";
            echo $languages[3];
            echo "<br>Language at location 4 : ";
            echo $languages[4];
            echo "<br>Language at location 5 : ";
            echo $languages[5];
        ?>
        </b>
    </div>
</body>
</html>