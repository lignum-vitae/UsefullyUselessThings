<?php include "../includes/states_header.html" ?>
<?php include "../includes/heading.html" ?>
<?php include "../includes/state_flag.php" ?>
<?php include "../nav/navbar.html" ?>
<?php include "../states_html/" . $state . ".html" ?>
<?php
if (isset($data)) {
    echo "<ul style=\"list-style:none;\">$data</ul>";
}
?>
<?php include "../includes/states_footer.html" ?>
