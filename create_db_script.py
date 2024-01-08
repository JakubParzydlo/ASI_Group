import argparse
import requests
import yaml

def send_api_request(api_url, payload, username, password):
    try:
        # Include auth parameter for Basic Authentication
        response = requests.post(api_url, json=payload, auth=(username, password))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending API request: {e}")
        return None
    
def update_yaml_file(yaml_file_path, api_response):
    try:
        # Extract relevant information from the API response
        new_url = f"postgresql+psycopg2://{api_response['url'].split('@')[1]}"

        # Load existing YAML data
        with open(yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Update the URL in the YAML data
        yaml_data['postgresql-credentials']['con'] = new_url

        # Write the updated YAML data back to the file
        with open(yaml_file_path, 'w') as file:
            yaml.dump(yaml_data, file, default_flow_style=False)
    except Exception as e:
        print(f"Error updating YAML file: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send API request and update YAML file.")
    parser.add_argument("password", help="Password for Basic Authentication")

    args = parser.parse_args()

    api_url = "https://customer.elephantsql.com/api/instances"
    username=""
    yaml_file_path=".\\asi-kedro\conf\local\credentials.yml"

    # API payload
    api_payload = {
        "name": "ASI_db_test",
        "plan": "turtle",
        "region": "amazon-web-services::eu-north-1"
        }

    # Send API request with Basic Authentication
    api_response = send_api_request(api_url, api_payload, username, args.password)

    if api_response:
        # Update YAML file with API response
        print(api_response)
        update_yaml_file(yaml_file_path, api_response)
    else:
        print("Failed to connect")

if __name__ == "__main__":
    main()
