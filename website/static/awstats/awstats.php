<?php
/**
* Copyright (c) 2005 - Javier Infante
* All rights reserved.   This program and the accompanying materials
* are made available under the terms of the 
* GNU General Public License (GPL) Version 2, June 1991, 
* which accompanies this distribution, and is available at: 
* http://www.opensource.org/licenses/gpl-license.php 
*
* Description: Example of usage of class.awfile.php
*
* Author: Javier Infante (original author)
* Email: jabi (at) irontec (dot) com
**/	
	require("class.awfile.php");
	
	$unique_visit = 0;
	$total_visit = 0;
	$page_loads = 0;
	// Path to the AWSTATS DATA FILE	
	for($i=1;$i<=12;$i++){
	    for($j=2013;$j<=2015;$j++){
		$file = '/var/lib/awstats/awstats'.$i.$j.'.python.fossee.in.txt';
		if($i < 10){
		    $file = '/var/lib/awstats/awstats0'.$i.$j.'.python.fossee.in.txt';
		}
		if(file_exists($file)){
		     $aw = new awfile($file);
	             if ($aw->Error()) die($aw->GetError());
		     $total_visit += $aw->GetVisits();
		     $unique_visit += $aw->GetUniqueVisits();
		    // echo "<b> Unique</b>" . $unique_visit . "<br>";
		     foreach ($aw->GetDays() as $day=>$pages)
                	$page_loads += $pages;
		     
		}
	    }
	}
	$output = array('unique_visit' => $unique_visit, 'total_visit' => $total_visit, 'total_page_loads' => $page_loads);
//	var_dump($output);
	echo json_encode($output);
	return $output;
/*	
	$aw = new awfile($file);
	if ($aw->Error()) die($aw->GetError());

	echo "<strong>Showing contents [".$file."]</strong><br />";

	echo "The site first visit in the month: ".$aw->GetFirstVisit()."<br /><br />";
	echo "Total visits this month: ".$aw->GetVisits()."<br /><br />";
	echo "Total unique visits this month: ".$aw->GetUniqueVisits()."<br /><br />";
	/*echo "Pages viewed / hours:<br />";
	foreach ($aw->GetHours() as $hour=>$pages)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".str_pad($hour, 2, "0", STR_PAD_LEFT).": ".$pages." pages viewed.</em><br />";
		
	echo "Pages viewed / days:<br />";
	foreach ($aw->GetDays() as $day=>$pages)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".$day.": ".$pages." pages viewed.</em><br />";
	echo "<br />";

	$betterDay = $aw->GetBetterDay();
	echo "The day with more visitors(".$betterDay[1].") was the ".$betterDay[0].".<br /><br />";

	echo "hits / os:<br />";
	foreach ($aw->GetOs() as $os=>$hits)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".$os.": ".$hits." hits.</em><br />";
	echo "<br />";	
	
	echo "hits / browser:<br />";
	foreach ($aw->GetBrowser() as $browser=>$hits)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".$browser.": ".$hits." hits.</em><br />";
	echo "<br />";
		
	echo "Distinct Referers:<br />";
	foreach ($aw->GetReferers() as $referer=>$hits)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".$referer.": ".$hits." hits.</em><br />";
	echo "<br />";
		
	echo "Visits / Session Ranges:<br />";
	foreach ($aw->GetRanges() as $range=>$visits)
		echo "&nbsp;&nbsp;&nbsp;&nbsp;<em>".$range.": ".$visits." visits.</em><br />";
	echo "<br />";*/

?>
