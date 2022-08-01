<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Operators</title>
</head>
<body>
    <?php

        // constant value :
        define('PI',3.14);

        $num1 = 10;
        $num2 = 20;

        echo "Number 1 :";
        echo $num1;
        echo "<br>Number 2 :";
        echo $num2;

        // Arithmetic Operations :

        echo "<br><b>Doing Arithmetic Operations on Two variables</b>";
        echo "<br><br>Adding two Variables :";
        echo "<br>num1+num2 = ";
        echo $num1+$num2;
        
        echo "<br><br>";    // will print on next li<br>ne

        echo "Subtracting two Variables :";
        echo "<br>num1-num2 = ";
        echo $num1-$num2;
        
        echo "<br><br>";

        echo "Multiplicing two Variables :";
        echo "<br>num1*num2 = ";
        echo $num1*$num2;

        echo "<br><br>";

        echo "Dividing two Variables :";
        echo "<br>num1/num2 = ";
        echo $num1/$num2;

        echo "<br><br>";

        echo "Finding Remainder of two Variables :";
        echo "<br>num1%num2 = ";
        echo $num1%$num2;

        // Assignment Operators :

        echo "<br><br><b>Doing Assignment Operations on Two variables</b>";

        $new_var=$num1;
        echo "<br><br>New variable value :";
        echo $new_var;

        echo "<br><br>Adding 1 to the value";
        echo "<br>New Variable Value :";
        $new_var += 1;
        echo $new_var;
        echo "<br>";

        echo "<br>Subtracting 1 to the value";
        echo "<br>New Variable Value :";
        $new_var += 1;
        echo $new_var;
        echo "<br>";

        echo "<br>Multiplicing 1 to the value";
        echo "<br>New Variable Value :";
        $new_var += 1;
        echo $new_var;
        echo "<br>";

        echo "<br>Dividing 1 to the value";
        echo "<br>New Variable Value :";
        $new_var += 1;
        echo $new_var;
        echo "<br>";

        // Comparsion Operaton :

        echo "<br><br><b>Doing Comparision Operations on Two variables</b><br>";

        echo "<br>Is 1==4 ? ";
        echo var_dump(1==4);    // var_dump() : 
        echo "<br>Is 1!=4 ? ";
        echo var_dump(1!=4);
        echo "<br>Is 1>=4 ? ";
        echo var_dump(1>=4);
        echo "<br>Is 1<=4 ? ";
        echo var_dump(1<=4);

        // Increment / Decrement Operators :
        echo "<br><br><b>Doing Increment / Decrement Operations </b><br>";
        
        // print the value first then increment it
        echo "<br> Post Incrementing :<br>";
        echo "num1 : ";
        echo $num1;
        echo "<br>num1++ =";
        echo $num1++;
        echo "<br>num1 =";
        echo $num1;

        // increment the value first and then print it

        echo "<br><br> Pre Incrementing :<br>";
        echo "num1 : ";
        echo $num1;
        echo "<br>++num1 =";
        echo ++$num1;
        echo "<br>num1 =";
        echo $num1;

        // print the value first then decrement it
        echo "<br><br> Post decrementing :<br>";
        echo "num1 : ";
        echo $num1;
        echo "<br>num1-- =";
        echo $num1--;
        echo "<br>num1 =";
        echo $num1;

        // decrement the value first and then print it

        echo "<br><br> Pre decrementing :<br>";
        echo "num1 : ";
        echo $num1;
        echo "<br>--num1 =";
        echo --$num1;
        echo "<br>num1 =";
        echo $num1;

        // Logical Operators :
        echo "<br><br><b>Doing Logical Operations </b><br>";
        
        // we can use either && / and
        $my_var = (true and true);
        echo "<br>true and true = ";
        echo var_dump($my_var);

        $my_var = (true and false);
        echo "<br>true and false = ";
        echo var_dump($my_var);

        $my_var = (false and false);
        echo "<br>false and false = ";
        echo var_dump($my_var);

        // we can use either or / ||
        $my_var = (true or true);
        echo "<br>true or true = ";
        echo var_dump($my_var);

        $my_var = (true or false);
        echo "<br>true or true = ";
        echo var_dump($my_var);

        // xor = exclusive or
        // if both are same then it will return false
        // else it will return true

        $my_var = (true xor true);
        echo "<br>true xor true = ";
        echo var_dump($my_var);

        $my_var = (true xor false);
        echo "<br>true xor false = ";
        echo var_dump($my_var);

        $my_var = (false xor false);
        echo "<br>false xor false = ";
        echo var_dump($my_var);

        // constant value :
        echo "<br><br> Constant Variable :<br>";
        echo "PI : ";
        echo PI;
        echo "<br>PI+=1 : error";
        // PI+=1; // Not possible to do as it is constant and we cannot change the value
        echo "<br>PI + 1=";
        echo PI+1;
    ?>
</body>
</html>