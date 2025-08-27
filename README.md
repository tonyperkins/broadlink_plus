# Broadlink Plus

Broadlink Plus is a custom integration for Home Assistant that enhances the functionality of Broadlink devices. It provides a user-friendly web interface to streamline the process of learning IR/RF commands and generating Home Assistant configurations.

## Features

### Home Assistant Integration

- **Device Support**: Supports a wide range of Broadlink devices, including remotes, switches, and sensors.
- **Configuration Flow**: Easy setup and configuration directly from the Home Assistant UI.
- **Dynamic Services**: Provides services to interact with your Broadlink devices, such as listing all learned commands.
- **Auto-Discovery**: Automatically discovers Broadlink devices on your network using DHCP.

### Command Learning Web UI

- **Intuitive Interface**: A web-based UI to easily learn and manage IR/RF commands.
- **Device Templates**: Pre-configured templates for common devices like TVs, ceiling fans, and air conditioners to speed up the setup process.
- **Real-time Feedback**: Live progress updates and activity logs during the command learning process.
- **YAML Generation**: Automatically generates the required YAML configuration for your Home Assistant setup.

## Installation

1.  Copy the `broadlink_plus` directory into your Home Assistant `custom_components` folder.
2.  Restart Home Assistant.
3.  Go to **Configuration** -> **Integrations** and click the `+` button.
4.  Search for "Broadlink Plus" and follow the on-screen instructions.

## Device and Command Naming Convention

To keep your commands organized and easy to manage, we recommend following a consistent naming convention. The web UI is designed around this convention.

### Recommended Convention

-   **Device**: `tonys_office_ceiling_fan`
-   **Command**: `light_on`

This structure helps in creating clear and descriptive command names that are easy to use in your automations and scripts.

## Usage

1.  **Access the Web UI**: Open the `www/index.html` file in your browser.
2.  **Connect to Home Assistant**: Enter your Home Assistant URL and a Long-Lived Access Token.
3.  **Select Your Device**: Choose your Broadlink device from the dropdown menu.
4.  **Configure Device and Commands**: Use the device templates or add custom commands.
5.  **Learn Commands**: Follow the on-screen instructions to learn the commands from your remote.
6.  **Generate YAML**: Once all commands are learned, generate and download the YAML configuration.

## Services

### `broadlink_plus.list_commands`

This service fetches all the stored IR/RF commands for a specified remote device and populates them into an `input_text` helper entity. This allows you to easily view all available commands directly within Home Assistant.

## Dependencies

-   [requests](https://pypi.org/project/requests/)
-   [broadlink](https://pypi.org/project/broadlink/)
