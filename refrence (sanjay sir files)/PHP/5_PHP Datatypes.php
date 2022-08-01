<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Datatypes</title>
</head>
<body>
    <?php
        // Datatypes in PHP :
        // 1. Strings
        // 2. Integer
        // 3. Float
        // 4. Boolean
        // 5. Array
        // 6. Object
        
        echo "<b>Datatypes in PHP :</b><br><br>";

        echo "String Datatype :<br>";
        $str = "Hello, This is a String !";
        echo "str = ";
        echo $str;
        echo "<br>";
        echo var_dump($str);

        echo "<br><br>Integer Datatype :<br>";
        $int_num = 34;
        echo "int_num = ";
        echo $int_num;
        echo "<br>";
        echo var_dump($int_num);

        echo "<br><br>Float Datatype :<br>";
        $float_num = 3.14;
        echo "float_num = ";
        echo $float_num;
        echo "<br>";
        echo var_dump($float_num);

        echo "<br><br>Boolean Datatype :<br>";
        $bool_val = true;
        echo "bool_val = ";
        echo $bool_val;
        echo "<br>";
        echo var_dump($bool_val);

        echo "<br><br>Array Datatype :<br>";
        $arr = [10,45,56,67];
        echo "arr = [10,45,56,67]";
        echo "<br>";
        echo var_dump($arr);
    ?>
</body>
</html>