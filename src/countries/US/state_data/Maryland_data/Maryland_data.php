<?php
function getBayData()
{
    // ALL FUNCTION CALLS HAPPEN FROM MARYLAND.PHP
    // Cache created relative to Maryland_data.php
    $cacheDir = __DIR__ . '/cache';
    $cacheFile = $cacheDir . '/bay_data.json';
    $logFile = $cacheDir . '/bay_data.log';
    $pyScriptFile = '../state_data/Maryland_data/eotb_Bay_Data.py';

    // Ensure cache directory exists
    if (!file_exists($cacheDir)) {
        mkdir($cacheDir, 0755, true);
    }

    // If cache exists, return it immediately
    if (file_exists($cacheFile)) {
        return file_get_contents($cacheFile);
    }

    // No cache: run blocking call and return result
    $descriptorspec = [
        0 => ['pipe', 'r'],
        1 => ['pipe', 'w'],
        2 => ['pipe', 'w'],
    ];

    $process = proc_open('python3 ' . $pyScriptFile, $descriptorspec, $pipes);

    if (!is_resource($process)) {
        error_log("Failed to start Python process.", 3, $logFile);
        return null;
    }

    $stdout = stream_get_contents($pipes[1]);
    fclose($pipes[1]);

    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[2]);

    $exitCode = proc_close($process);

    if ($exitCode !== 0) {
        error_log("Python script error (exit code $exitCode): $stderr", 3, $logFile);
        return null;
    }

    file_put_contents($cacheFile, $stdout);
    return $stdout;
}

$bayData = getBayData();
echo $bayData;
?>
