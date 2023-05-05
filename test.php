<?php

# $hostname = "adres_serwera_sql.mysql.database.azure.com";
# $username = "admin";
# $password = "tajne_haslo";

$link = mysql_connect('localhost', 'mysql_user', 'mysql_password');
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
echo 'Connected successfully';
mysql_close($link);

?>
