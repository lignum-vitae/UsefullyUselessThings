<?php /*All files relative to files in src/countries/US/states/... */ ?>
<?php
    ob_start();
    include("../../../includes/states_header.html");
    $buffer = ob_get_clean();
    $buffer = preg_replace('/(<title>)(.*?)(<\/title>)/i', '$1' . $state . '$3', $buffer);
    echo $buffer;
?>
<?php include "../../../includes/heading.html" ?>
<?php include "../../../includes/state_flag.php" ?>
<?php include "../../../nav/navbar.html" ?>
<?php include "../states_html/" . $state . ".html" ?>
<?php
if (isset($data)) {
    echo "<ul style=\"list-style:none;\">$data</ul>";
}
if (isset($cards)) {
    echo "<ul style=\"list-style:none;\">$cards</ul>";
}
?>
<?php include "../../../includes/states_footer.html" ?>
