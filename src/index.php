<?php
$title = "Welcome!";
ob_start();
require "nav/index.html";
$content = ob_get_clean();
?>
<?php require "includes/landing.php" ?>
