<?php
$title = "Welcome!";
ob_start();
include "nav/index.html";
$content = ob_get_clean();
?>
<?php include "includes/landing.php" ?>
