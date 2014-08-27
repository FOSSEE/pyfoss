<html>
	<head>
		<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
		<style>
			.pylogo {
				width: 100px;
			}
			.pytitle {
				display: inline;
			}
		</style>
	</head>
</html>
<body>
<?php 
	$connection = mysql_connect("176.9.7.40", "scilabuser", "SciLab203*user");
	if(!$connection) {
		die("Database connection failed" . mysql_error());
	}
	$mysql_select = mysql_select_db("workshop_info", $connection);
	if(!$mysql_select) {
		die("Database selection failed" . mysql_error());
	}
	$query = "select wr.id, wr.workshop_code, wr.cfm_wkshop_date, wr.foss_category, ac.institution_name, ac.city, wd.no_of_participants from workshop_requests wr, academic_center ac, workshop_details wd where wr.foss_category='Python' and wr.status=2 and ac.academic_code=wr.academic_code and wd.workshop_code=wr.workshop_code";
	$result = mysql_query($query);
?>
	<div class="container">
		<center>
			<br><br>
			<img class="pylogo" src="http://python.fossee.in/static/website/images/pylogo.png"><h3 class="pytitle"> Python - Conducted Workshop List</h3>
			<br><br>
		</center>
		
		<table class="table table-striped table-bordered">
			<thead>
				<th>#</th>
				<th>Workshop Date</th>
				<th>Institution Name</th>
				<th>City</th>
				<th>No. of participants</th>
			</thead>
			<tbody>
				<?php
					$count = 1;
					while($row = mysql_fetch_object($result)) {
						echo "<tr>";
							echo "<td>{$count}</td>";
							echo "<td>{$row->cfm_wkshop_date}</td>";
							echo "<td>{$row->institution_name}</td>";
							echo "<td>{$row->city}</td>";
							echo "<td>{$row->no_of_participants}</td>";
						echo "</tr>";
						$count++;
					}
				?>
			</tbody>
		</table>
	</div>
</body>
</html>
