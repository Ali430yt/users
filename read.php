<?php
$host = "remotemysql.com";
$user = "WTaUK7bNkM";
$pass = "iMD7dgW9nG";
$db = "WTaUK7bNkM";
@$cont = mysqli_connect($host,$user,$pass,$db);
$src_read = "SELECT ip FROM users_tool";
$rew = mysqli_query($cont,$src_read);
$data = array();
while( $r = mysqli_fetch_assoc($rew)){
    $data[] = $r["ip"];
}
echo json_encode($data);
?>