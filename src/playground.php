<?php
$title = "";
ob_start();
require "nav/playground.html";
$content = ob_get_clean();
?>

<?php require "includes/landing.php" ?>
