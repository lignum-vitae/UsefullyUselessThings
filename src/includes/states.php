<?php /*All files relative to files in src/countries/US/states/... */ ?>
<?php include "../../../includes/states_header.html" ?>
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
