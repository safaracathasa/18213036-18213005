<?php
	$opt = array('location' => 'http://localhost/soap-server.php', 'uri' => 'http://localhost/');
	$api = new SoapClient (NULL, $opt);
	
	echo $api -> helloworld();
	echo "<br>";
	echo $api -> addition(2,3);
	echo "<br>";
	echo $api -> getData();
?>
