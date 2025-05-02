<?php
function getBayData()
{
    $cacheDir = __DIR__ . '/cache';
    $cacheFile = $cacheDir . '/bay_data.json';
    $cacheExpiry = 3; // 1 day (in seconds)

    // Ensure cache directory exists
    if (!file_exists($cacheDir)) {
        mkdir($cacheDir, 0755, true);
    }

    // Check if cache exists and is fresh
    if (file_exists($cacheFile) && (time() - filemtime($cacheFile) < $cacheExpiry)) {
        return file_get_contents($cacheFile);
    }

    // Cache doesn't exist or is stale, run Python script
    $output = shell_exec('python3 ../../../scripts/data/get_data/baydata.py');

    if ($output === null) {
        return null;
    }

    // Save to cache
    file_put_contents($cacheFile, $output);
    return $output;
}

$bayData = getBayData();
echo $bayData;
?>
