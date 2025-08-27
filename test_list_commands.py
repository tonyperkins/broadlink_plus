# This script tests the broadlink_plus.list_commands service call via the Home Assistant REST API.

import requests
import json
import argparse

def test_list_commands(token=None):
    """Connects to Home Assistant and calls the list_commands service."""

    # --- User Configuration ---
    # Replace with your Home Assistant URL and Long-Lived Access Token.
    # Use arguments if provided, otherwise prompt the user.
    ha_url = args.ha_url if args.ha_url else input(f"Enter your Home Assistant URL [default: http://homeassistant.local:8123]: ") or "http://homeassistant.local:8123"
    entity_id = args.entity_id if args.entity_id else input(f"Enter the entity_id of your Broadlink remote [default: remote.broadlink_plus]: ") or "remote.broadlink_plus"

    if not token:
        token = input("Enter your Long-Lived Access Token: ")

    if not ha_url.startswith(('http://', 'https://')):
        print("Error: Invalid URL format. Please include http:// or https://")
        return

    # --- API Call ---
    service_url = f"{ha_url}/api/services/broadlink_plus/list_commands?return_response=true"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "entity_id": entity_id
    }

    print(f"\nCalling service: {service_url}")
    print(f"With target: entity_id={entity_id}")

    try:
        response = requests.post(service_url, headers=headers, data=json.dumps(data), timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        print("\n--- Service Call Successful ---")
        try:
            response_data = response.json()
            if response_data:
                print(json.dumps(response_data, indent=2))
            else:
                print("Received an empty response from the service call.")

        except json.JSONDecodeError:
            print("Could not decode JSON response. Raw response text:")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"\n--- An error occurred ---")
        print(f"Error: {e}")
        if e.response is not None:
            print(f"Status Code: {e.response.status_code}")
            print(f"Response: {e.response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test the broadlink_plus.list_commands service.")
    parser.add_argument("--ha-token", help="Your Home Assistant Long-Lived Access Token.")
    parser.add_argument("--ha-url", help="Your Home Assistant URL (e.g., http://192.168.1.100:8123)")
    parser.add_argument("--entity-id", help="The entity_id of the Broadlink remote.")
    args = parser.parse_args()

    test_list_commands(token=args.ha_token)
