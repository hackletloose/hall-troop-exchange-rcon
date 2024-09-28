# [HaLL] Troop Exchange - !switchme ingame command
Using this script, it is possible to allow players in "Hell Let Loose" to switch sides without having to ask the administrator. 
Administrators also do not need to leave the game. Anyone can enter the command `!switchme` into the game's chat, and they will
automatically switch between Axis or Allied forces. Additionally, the tool has a restriction that can be utilized.
This allows specifying the maximum allowed number of players, after which executing the command is no longer possible. 
For example, this could allow switching during seeding, but not afterwards.

ToDo:
Execute the following commands after downloading:
1. Copy the `.env.dist` file to `.env` and enter your values.
2. Run the command `pip install python-dotenv`.
3. Copy `troop-exchange.service.dist` to `/etc/systemd/system/troop-exchange.service`
4. Activate and start the service with `sudo systemctl enable troop-exchange.service` and `sudo systemctl start troop-exchange.service`.

## Features

- **Log Monitoring**: Continuously monitors the game server log for a specific chat command (`!switchme`).
- **Player Count Check**: Ensures the number of players on the server is below a set maximum before switching a player to the opposing team.
- **RCON API Integration**: Uses an RCON API to manage team switching on the server.
- **Configurable Limits**: The maximum number of players on the server before switching is restricted is configurable via environment variables.

## Prerequisites

- Python 3.8+
- A game server with an RCON API
- `.env` file with the following environment variables:
  - `RCON_API_URL`: The URL for the RCON API
  - `API_TOKEN`: The API token for authenticating with the RCON API
  - `LOG_FILE_PATH`: Path to the game log file to be monitored
  - `MAX_PLAYERS`: Maximum number of players allowed before the bot stops switching players (optional, default is 40)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hackletloose/hall-troop-exchange.git
    cd hall-trop-exchange
    ```

2. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory with the following content:
    ```bash
    RCON_API_URL=https://your-rcon-api-url
    API_TOKEN=your-api-token
    LOG_FILE_PATH=/path/to/your/logfile.log
    MAX_PLAYERS=40  # Optional, default is 40
    ```

4. Run the script:
    ```bash
    python troop-exchange.py
    ```

## Usage

1. **Monitor Server Logs**: The script continuously monitors the log file specified in the `.env` file for the `!switchme` command.
   
2. **Automatic Team Switching**: When a player uses the `!switchme` command in the game chat, the bot checks the total number of players on the server. If the number of players is below the configured maximum, it switches the player to the opposing team.

3. **Logs and Debugging**: The script also prints out messages for actions such as successful player switches or errors during communication with the RCON API.

## Environment Variables

The following environment variables must be set in the `.env` file:

- `RCON_API_URL`: The base URL for the RCON API that the bot will use to interact with the game server.
- `API_TOKEN`: A token for authenticating requests to the RCON API.
- `LOG_FILE_PATH`: The path to the log file that the bot will monitor.
- `MAX_PLAYERS`: The maximum number of players allowed on the server before the bot stops switching players (default is 40).

## Dependencies

- `requests`: For sending HTTP requests to the RCON API
- `python-dotenv`: For loading environment variables from the `.env` file
- `subprocess`: For monitoring the log file in real time

## Contributing

Feel free to fork this repository and create a pull request if you want to contribute to the project. You can also open issues if you encounter any problems or have suggestions for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
