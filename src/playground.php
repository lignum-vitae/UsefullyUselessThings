<?php
$title = "";
ob_start();
include "nav/playground.html";
$content = ob_get_clean();
ob_end_clean();
?>

<?php include "includes/landing.php" ?>
