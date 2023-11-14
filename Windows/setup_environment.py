import subprocess
import sys
import zipfile
import urllib.request
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def download_webdriver():
    edge_driver_url = "https://msedgedriver.azureedge.net/119.0.2151.58/edgedriver_win64.zip"
    edge_driver_zip = "edgedriver_win64.zip"
    urllib.request.urlretrieve(edge_driver_url, edge_driver_zip)
    
    with zipfile.ZipFile(edge_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()

    os.remove(edge_driver_zip)

# Install selenium package
print("Installing Selenium...")
install("selenium")

# Download Edge WebDriver
print("Downloading Microsoft Edge WebDriver...")
download_webdriver()

print("Environment setup complete.")
