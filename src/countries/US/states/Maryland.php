<?php 
$state = "Maryland";
$data = shell_exec('py ../../../scripts/data/baydata.py 2>&1')
?>
<?php include "../../../includes/states.php" ?>
