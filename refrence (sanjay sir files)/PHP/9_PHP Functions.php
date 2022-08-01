<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Functions</title>
</head>
<link rel="stylesheet" href="style.css">
<body>
    <div class="container">
        <h1>Lets Learn about PHP Functions</h1> 
        <?php
            echo "<br><b>Calling Function without any argument :</b><br>";
            echo "<br>The task of function is to print \"Hello World\"";

            function print_text()
            {
                echo "<br>Hello World !";
            }

            // calling the function 5 times to execute the code 5 times:
            print_text();
            print_text();
            print_text();
            print_text();
            print_text();
        ?>
        <?php
            echo "<br><br><b>Calling Function with argument :</b><br>";
            echo "<br>The task of function is to print number which is passed";

            function print_num($num)
            {
                echo "<br>Number Passed : ",$num;
            }

            // calling the function 5 times to execute the code 5 times:
            print_num(23);
            echo "&nbsp;&nbsp;&nbsp;<b>// code : print_num(23);</b>";
            print_num(34);
            echo "&nbsp;&nbsp;&nbsp;<b>// code : print_num(34);</b>";
            print_num(45);
            echo "&nbsp;&nbsp;&nbsp;<b>// code : print_num(45);</b>";
            print_num(56);
            echo "&nbsp;&nbsp;&nbsp;<b>// code : print_num(56);</b>";
            print_num(16);
            echo "&nbsp;&nbsp;&nbsp;<b>// code : print_num(16);</b>";

            echo "<br><br><b>NOTE : Similar we can do other operation as required !</b>";
        ?>
    </div>
</body>
<html>