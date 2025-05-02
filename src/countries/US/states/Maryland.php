<?php
$state = "Maryland";
ob_start();
require "../state_data/Maryland_data.php";
$bayData = ob_get_clean();
if ($bayData === null) {
    error_log("Failed to load bay_data.json or run python script");
    $bayData = "{}";
}
ob_start();
require "../states_html/information_cards/Maryland_cards.html";
$cards = ob_get_clean();
?>

<script>
    window.bayData = <?php echo $bayData ?: '{}'; ?>;
</script>
<?php require "../../../includes/states.php" ?>
