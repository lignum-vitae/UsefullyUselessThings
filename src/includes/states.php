<?php /*All files relative to files in src/countries/US/states/... */ ?>
<?php
    ob_start();
    require "../../../includes/states_header.html";
    $buffer = ob_get_clean();
    $state_title = str_replace("_", " ", $state);
    $buffer = preg_replace('/(<title>)(.*?)(<\/title>)/i', '$1' . $state_title . '$3', $buffer);
    echo $buffer;
?>
<?php require "../../../includes/heading.html" ?>
<?php require "../../../includes/state_flag_and_header.php" ?>
<?php require "../../../nav/navbar.html" ?>
<?php require "../states_html/" . $state . ".html" ?>
<?php
if (isset($data)) {
    echo "<ul style=\"list-style:none;\">$data</ul>";
}
if (isset($cards)) {
    echo "<ul style=\"list-style:none;\">$cards</ul>";
}
?>
<?php require "../../../includes/states_footer.html" ?>
