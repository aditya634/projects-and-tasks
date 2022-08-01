<!DOCTYPE html>
<html lang="en">
<head>
    <title>PHP Functions</title>
</head>
<link rel="stylesheet" href="style.css">
<body>
    <div class="container">
        <h1>Lets Learn about PHP Strings</h1> 
        <?php
            $fname="Sanjay";
            $lname="Sukhwani";
            $mname="Ashok";
        
            echo "<br><b>First name : </b>".$fname;
            echo "<br><b>Middle name : </b>".$mname;
            echo "<br><b>Last name : </b>".$lname;

            echo "<br><br><b>Printing full name using dot operator : </b>";
            echo "<br><br><b>Full name : </b>".$fname." ".$mname." ".$lname;

            // string concatation
            $fullname = $fname." ".$mname." ".$lname;

            // strlen()
            echo "<br><br><b>Printing length of full name using strlen() : </b>";
            echo "<br>The length of full name is ". strlen($fullname) . " characters.";

            // str_word_count()
            echo "<br><br><b>Printing number of words in full name using str_word_count() : </b>";
            echo "<br>The number of words in full name is ". str_word_count($fullname) . " words.";

            // strrev()
            echo "<br><br><br><b>Printing reversed string of full name using strrev() : </b>";
            echo "<br>The reversed string is ". strrev($fullname);

            // strpos()
            echo "<br><br><br><b>Searching word \"Ashok\" in full name using strpos() : </b>";
            echo "<br>The search for \"Ashok\" in this string is ". strpos($fullname, "Ashok") . " position in fullname";
            
            echo "<br><br><br><b>Searching word \"Mayur\" in full name using strpos() : </b>";
            echo "<br>The search for \"Mayur\" in this string is ". strpos($fullname, "Mayur") . " position in fullname";
            // if it is not present it will not print anything !
            
            //str_replace()
            echo "<br><br><br><b>Replacing word \"Ashok\" to \"Ashokkumar\" in full name using str_replace() : </b>";
            echo "<br>The replaced string is ". str_replace("Ashok", "Ashokkumar", $fullname);
            // echo $lenn;
        ?>
    </div>
</body>
</html>