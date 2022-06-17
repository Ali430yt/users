<?php
if(isset($_GET["ip"])){

$ip = $_GET["ip"];
$host = "remotemysql.com";
$user = "WTaUK7bNkM";
$pass = "iMD7dgW9nG";
$db = "WTaUK7bNkM";

@$cont = mysqli_connect($host,$user,$pass,$db);
$src_add = "INSERT INTO users_tool(ip) VALUES('$ip')";
$rew = mysqli_query($cont,$src_add);
if ($rew){
echo "done";
}else{
echo "error";
}
}
?>