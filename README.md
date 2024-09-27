# [HaLL] Troop Exchange - !switchme ingame command
Using this script, it is possible to allow players in "Hell Let Loose" to switch sides without having to ask the administrator. 
Administrators also do not need to leave the game. Anyone can enter the command `!switchme` into the game's chat, and they will
automatically switch between Axis or Allied forces. Additionally, the tool has a restriction that can be utilized.
This allows specifying the maximum allowed number of players, after which executing the command is no longer possible. 
For example, this could allow switching during seeding, but not afterwards.

ToDo:
Execute the following commands after downloading:
1. Copy the `.env.dist` file to `.env` and enter your values.
1. Run the command `pip install python-dotenv`.
1. Copy `troop-exchange.service.dist` to `/etc/systemd/system/troop-exchange.service`
1. Activate and start the service with `sudo systemctl enable troop-exchange.service` and `sudo systemctl start troop-exchange.service`.
