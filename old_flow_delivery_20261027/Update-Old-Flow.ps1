param([string]$TargetRoot = '', [switch]$CheckOnly, [string]$RestoreBackup = '')
$ErrorActionPreference = 'Stop'
try {
    if (-not $TargetRoot) {
        $nearby = @()
        $parent = Split-Path -Parent $PSScriptRoot
        if (Test-Path -LiteralPath (Join-Path $parent 'ready_manifest.json')) { $nearby += $parent }
        Get-ChildItem -LiteralPath $parent -Directory | ForEach-Object {
            if (Test-Path -LiteralPath (Join-Path $_.FullName 'ready_manifest.json')) { $nearby += $_.FullName }
        }
        if ($nearby.Count -eq 1) { $TargetRoot = $nearby[0] }
        else {
            Add-Type -AssemblyName System.Windows.Forms
            $picker = New-Object System.Windows.Forms.FolderBrowserDialog
            $picker.Description = 'Select the OLD chatbot folder containing Start-Chatbot.cmd, runtime and system.'
            if ($picker.ShowDialog() -ne [System.Windows.Forms.DialogResult]::OK) { return }
            $TargetRoot = $picker.SelectedPath
        }
    }
    $TargetRoot = (Resolve-Path -LiteralPath $TargetRoot).Path
    $python = Join-Path $TargetRoot 'runtime\python\python.exe'
    if (-not (Test-Path -LiteralPath $python)) { throw 'Select the chatbot folder, not the ZIP or the system subfolder.' }
    $arguments = @('-I', '-B', (Join-Path $PSScriptRoot 'update_old_flow.py'), '--target', $TargetRoot)
    if ($CheckOnly) { $arguments += '--check-only' }
    if ($RestoreBackup) { $arguments += @('--restore', $RestoreBackup) }
    & $python @arguments
    if ($LASTEXITCODE -ne 0) { throw 'Update was not completed. See the reason above. Local changes were not silently overwritten.' }
    if (-not $CheckOnly) { Write-Host 'Done. Open Start-Chatbot.cmd in the OLD chatbot folder.' }
} catch {
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}
