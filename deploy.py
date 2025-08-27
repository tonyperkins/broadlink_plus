import os
import shutil
from pathlib import Path
import argparse
import requests
import json

def copy_files(source_dir, target_dir, extensions=None):
    """Copy files from source to target directory, optionally filtering by extension."""
    source = Path(source_dir)
    target = Path(target_dir)
    
    # Create target directory if it doesn't exist
    target.mkdir(parents=True, exist_ok=True)
    
    # Copy files
    for item in source.glob('*'):
        if item.is_file() and (extensions is None or item.suffix.lower() in extensions):
            print(f"Copying {item.name} to {target}")
            shutil.copy2(item, target / item.name)

def restart_home_assistant(ha_url, token):
    """Restart Home Assistant via API call."""
    service_url = f"{ha_url.rstrip('/')}/api/services/homeassistant/restart"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    try:
        print("\nAttempting to restart Home Assistant...")
        response = requests.post(service_url, headers=headers, timeout=10)
        response.raise_for_status()
        print("Home Assistant is restarting.")
    except requests.exceptions.RequestException as e:
        print(f"\nError restarting Home Assistant: {e}")
        if e.response is not None:
            print(f"Status Code: {e.response.status_code}")
            print(f"Response: {e.response.text}")

def main():
    parser = argparse.ArgumentParser(description="Deploy Broadlink Plus component and optionally restart Home Assistant.")
    parser.add_argument("--restart", action="store_true", help="Restart Home Assistant after deployment.")
    parser.add_argument("--ha-url", default="http://homeassistant.local:8123", help="Home Assistant URL.")
    parser.add_argument("--ha-token", help="Home Assistant Long-Lived Access Token.")
    args = parser.parse_args()

    # Base directories
    script_dir = Path(__file__).parent
    broadlink_src = script_dir / 'broadlink_plus'
    html_src = script_dir / 'www' / 'index.html'
    
    # Target directories
    target_components = Path('H:') / 'custom_components' / 'broadlink_plus'
    target_www = Path('H:') / 'www' / 'broadlink'
    
    try:
        # Copy Python files to custom_components
        print("Deploying Broadlink Plus component...")
        copy_files(broadlink_src, target_components, {'.py', '.json', '.yaml', '.md'})
        
        # Create www directory if it doesn't exist
        target_www.mkdir(parents=True, exist_ok=True)
        
        # Copy HTML file
        print(f"\nDeploying web interface to {target_www}")
        shutil.copy2(html_src, target_www / 'index.html')
        
        print("\nDeployment completed successfully!")

        if args.restart:
            if not args.ha_token:
                print("Restart requires --ha-token to be provided.")
            else:
                restart_home_assistant(args.ha_url, args.ha_token)
        
    except Exception as e:
        print(f"\nError during deployment: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
