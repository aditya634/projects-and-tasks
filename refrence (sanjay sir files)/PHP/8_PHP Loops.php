<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Loops</title>
</head>
<link rel="stylesheet" href="style.css">
<body>
    <div class="container">
        <h1>Lets Learn about PHP Loops</h1> 
        <?php
            $a=1;
            echo "<br><b>Printing numbers from 1 to 10 using while loop</b><br>";
            echo "<br>The value of a before the loop :";
            echo $a;
            while($a<=10)
            {
                echo "<br>The value of a is:";
                echo $a;
                $a++;
            }
            echo "<br>The value of a after the loop :";
            echo $a;
        ?>
        <?php
            $a=1;
            echo "<br><br><b>Printing numbers from 1 to 10 using do while loop</b><br>";
            echo "<br>The value of a before the loop :";
            echo $a;
            do
            {
                echo "<br>The value of a is:";
                echo $a;
                $a++;
            }while($a<=10);
            echo "<br>The value of a after the loop :";
            echo $a;
        ?>
        <?php
            $a=200;
            echo "<br><br><b>Printing numbers from 1 to 10 using do while loop</b><br>";
            echo "<br>The value of a before the loop :";
            echo $a;
            do
            {
                echo "<br>The value of a is:";
                echo $a;
                $a++;
            }while($a<=10);
            echo "<br>The value of a after the loop :";
            echo $a;

            echo "<br><br><b><u>NOTE :</u></b> do while loop will always do one iteration whether the condition is false or true !";
        ?>
        <?php
            echo "<br><br><b>Printing numbers from 1 to 10 using for loop</b><br>";
            for ($a=1; $a <= 20; $a++) 
            { 
                echo "<br>The value of a is:";
                echo $a;
            }
            echo "<br>The value of a after the loop :";
            echo $a;

            echo "<br><br><b><u>NOTE :</u></b> In for loop, we not need to increment the variable and also no need to initialize it before all things will be done in for brackets.";
        ?>
        <?php
            echo "<br><br><b>Printing arrays element using foreach loop</b><br>";
            $fruits=array("Apple","Mango","Pear","Banana","Pineapple","Kiwi");

            // fruit will act as the pointer in the fruits array which will print all the values
            foreach ($fruits as $fruit) 
            { 
                echo "<br>The value of <i>fruit</i> from fruits is:";
                echo $fruit;
            }
            echo "<br>The value of <i>fruit</i> after the loop :";
            echo $fruit;

            echo "<br><br><b><u>NOTE :</u></b> foreach loop is mostly used over arrays to iterate easily compared to other loops";
        ?>


        </b>
    </div>
</body>
</html>