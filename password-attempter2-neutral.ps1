$lines = Get-Content "output.txt" 
foreach ($line in $lines) {
    steghide extract -sf "Path\To\File\Filename.bmp" --passphrase $line
    Start-Sleep -Milliseconds 10
}