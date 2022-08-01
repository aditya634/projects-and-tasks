<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Show All</title>
	<style>
		table{
			font-size: 18px;
		}
	</style>
</head>
<body>
    <h1>All Students</h1>
    <hr>
	<?php
	$host = 'localhost:3306';
    $user = 'root';
    $pass = '';
    $dbname = 'studRecords';

    $con = mysqli_connect($host, $user, $pass, $dbname);

	if ($con) {
		echo "Connection Successfully Established";
		echo "<hr>";
		echo "Database Connection Successfully";
		$result = mysqli_query($con, "select * from students"); //simple data

		echo "<hr>";
		var_dump($result);

		echo "<hr>";
		$rowCount = mysqli_num_rows($result); // counting row from result data
		$colCount = mysqli_num_fields($result); // counting col from result data
		echo "Total Rows = " . $rowCount;
		echo "<br>" . "Total cols = " . $colCount;
		echo "<hr>";
		// echo "Total Rows = " . $result["num_rows"];
		// echo "<br>" . "Total cols = " . $result["field_count"];
		// echo "<hr>";

		echo "<table bgcolor='black' cellspacing='1' cellpadding='20' width='60%' align='center'>";
		echo "<tr bgcolor='grey' align='center'>";
		for ($i=0;$i<$colCount;$i++) { 
			// using field_name we print the title
			echo "<br>";
			echo "<td><b>".strtoupper(mysqli_fetch_field($result)->name)."</b></td>";
		}
		echo "</tr>";
		echo "<tbody bgcolor='gold'>";

		while ($ans = mysqli_fetch_row($result)) {
			// echo $ans;
			// echo "<br>";
			// print_r($ans);
			// echo "<br><br><br>";
			echo "<tr>";
			for ($i = 0; $i < $colCount; $i++) {
				echo "<td>" . $ans[$i] . "</td>";
			}
			echo "</tr>";
		}
		echo "</tbody>";
		echo "<tfoot bgcolor='pink'>";
		echo "<tr><th colspan=5><a href='InsertForm.html'>Insert New Record</a></th></tr>";
		echo "<tr><th colspan=5><a href='updateForm.html'>Update Existing Records</a></th></tr>";
		echo "<tr><th colspan=5><a href='DeleteForm.html'>Delete Existing Records</a></th></tr>";
		echo "</tfoot>";
		echo "</table>";
	} else {
		echo "Connection Failed";
	}
	?>
</body>
</html>