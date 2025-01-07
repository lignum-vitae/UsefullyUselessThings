<?php
$title = "";
ob_start();
include "nav/playground.html";
$content = ob_get_clean();
?>

<?php include "includes/landing.php" ?>
