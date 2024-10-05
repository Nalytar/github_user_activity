# Check if python and pip is installed
if ((!(Get-Command python -ErrorAction SilentlyContinue)) -or (!(Get-Command pip -ErrorAction SilentlyContinue))) {
    Write-Host "Python or pip is not installed" -ForegroundColor Red
    exit
}

# Install requirements, skip already satisfied (--no-deps and use-feature=fast-deps options)
pip install --no-deps --use-feature=fast-deps -r "$PSScriptRoot\requirements.txt"

# Define the function
$functionBody = @"
function github-activity {
    param([string]`$username)
    python \"$PSScriptRoot\github_activity.py\" `$username
}
"@

# Get the profile file location
$profileFile = $PROFILE.AllUsersCurrentHost

# Check if the profile file exist
if (!(Test-Path -path $profileFile)) {
    # If not, create one
    New-Item -type file -path $profileFile -force
}

# Add the function to the profile file, if it doesn't exist
if (!(Select-String -Path $profileFile -Pattern 'function github-activity')) {
    Out-File -FilePath $profileFile -Append -InputObject $functionBody
}

# Source the profile file to make the function available immediately
. $profileFile