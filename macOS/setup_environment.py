import subprocess

def install(package):
    subprocess.check_call(["pip3", "install", package])

# Install Selenium package
print("Installing Selenium...")
install("selenium")

print("Environment setup complete.")

print("\nPlease follow these steps to enable Remote Automation in Safari:")
print("1. Open Safari.")
print("2. Go to the 'Safari' menu (next to the Apple logo on the menu bar) and choose 'Preferences.'")
print("3. Navigate to the 'Advanced' tab.")
print("4. At the bottom, check the box next to 'Show Develop menu in menu bar.'")
print("5. Now, in the 'Develop' menu that appears in the menu bar, select 'Allow Remote Automation.'")
