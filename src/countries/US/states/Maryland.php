<?php 
$state = "Maryland";
ob_start();
include "../state_data/Maryland_data.php";
$data = ob_get_clean();
ob_start();
include "../states_html/information_cards/Maryland_cards.html";
$cards = ob_get_clean();
?>
<?php include "../../../includes/states.php" ?>
