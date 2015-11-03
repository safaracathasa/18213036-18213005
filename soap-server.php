<?php
	class API
	{
		function helloworld()
		{
			return "Hello World!";
		}
		
		function addition($a,$b)
		{
			return ($a+$b);
		}
		
		function getData()
		{	
			mysql_connect('localhost','root','');
			mysql_select_db('wordpress');
			$result = mysql_query('SELECT * FROM wp_users');
				while ($row = mysql_fetch_array ($result,MYSQL_ASSOC))
					{
						foreach ($row as $column)
						{
							$var = $column;
						}
					}
			return $var;
		}
	}
	$opt = array('uri'=>'http://localhost');
	$server = new SoapServer (NULL,$opt);
	$server -> setClass ('API');
	$server -> handle();
	
?>
