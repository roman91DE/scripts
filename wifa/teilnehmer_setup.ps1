# setup script for user accounts (needs admin priviliges)
# hoehn@dozenten.wifa.de
# ----------------------


# install choco packet manager
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# install packages
choco install firefox -y
choco install microsoft-teams -y
choco install pdf24 -y
choco install adobereader -y

