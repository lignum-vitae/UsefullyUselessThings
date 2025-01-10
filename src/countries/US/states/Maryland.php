<?php 
$state = "Maryland";
$data = shell_exec('py ../../../scripts/data/get_data/baydata.py 2>&1');

ob_start();
include "../states_html/information_cards/Maryland_cards.html";
$cards = ob_get_clean();
?>
<?php include "../../../includes/states.php" ?>
