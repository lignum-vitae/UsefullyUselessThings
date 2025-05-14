<?php
$state_flag = $state . "_flag";

echo <<< FLAGBLOCK
    <div class="center">
    <img style="min-width: 200px; width: 16vw; max-width: 500px; padding-top: 3em;" alt="Flag of $state_title"
    src="../state_flags/$state_flag.png">
    <h1 style="padding-bottom: 1.5em">$state_title</h1>
    </div>
    FLAGBLOCK;
?>
