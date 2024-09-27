import time
import subprocess
import requests
from dotenv import dotenv_values

# Laden der Umgebungsvariablen aus der .env-Datei
env_vars = dotenv_values(".env")
RCON_API_URL = env_vars.get("RCON_API_URL")
API_TOKEN = env_vars.get("API_TOKEN")
log_file_path = env_vars.get("LOG_FILE_PATH")
max_players = int(env_vars.get("MAX_PLAYERS", 40))  # Standardwert 40, falls nicht angegeben

# Funktion zur Überprüfung der Anzahl der Spieler auf dem Server
def check_player_count():
    try:
        response = requests.get(f"{RCON_API_URL}/api/get_gamestate", headers={"Authorization": f"Bearer {API_TOKEN}"})
        if response.status_code == 200:
            gamestate = response.json()["result"]
            num_allied_players = gamestate["num_allied_players"]
            num_axis_players = gamestate["num_axis_players"]
            total_players = num_allied_players + num_axis_players
            return total_players
        else:
            print("Fehler beim Abrufen des Spielzustands.")
            return None
    except requests.exceptions.RequestException as e:
        print("Fehler beim Kommunizieren mit der RCON-API:", e)
        return None

# Funktion, um einen Spieler in das gegnerische Team zu verschieben
def switch_player_team(player_name):
    player_count = check_player_count()
    if player_count is not None and player_count < max_players:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        payload = {"player": player_name}
        try:
            response = requests.post(f"{RCON_API_URL}/api/do_switch_player_now", json=payload, headers=headers)
            if response.status_code == 200:
                print(f"Spieler {player_name} wurde in das gegnerische Team verschoben.")
            else:
                print("Fehler beim Verschieben des Spielers.")
        except requests.exceptions.RequestException as e:
            print("Fehler beim Kommunizieren mit der RCON-API:", e)
    else:
        print(f"Es sind bereits {max_players} oder mehr Spieler auf dem Server. Der Spieler kann nicht verschoben werden.")

# Funktion, um den Spielchat zu überwachen
def monitor_game_log(log_file_path):
    try:
        with open(log_file_path, "r") as log_file:
            log_file.seek(0, 2)  # An das Ende der Datei springen
            while True:
                line = log_file.readline()
                if "!switchme" in line and "Triggered rcon.discord_chat.handle_on_chat" in line:
                    parts = line.split("[")[-1].split("]")  # Teile die Zeile an "[" und "]"
                    player_name = parts[-2].split("(")[0].strip()  # Annahme: Spielername ist vor dem "("
                    switch_player_team(player_name)
                time.sleep(0.1)  # Kurze Pause, um die CPU-Last zu reduzieren
    except FileNotFoundError:
        print("Die angegebene Logdatei wurde nicht gefunden.")
    except Exception as e:
        print("Fehler beim Überwachen des Spiellogs:", e)

# Hauptfunktion
def main():
    # Überprüfen, ob alle erforderlichen Umgebungsvariablen vorhanden sind
    if not all([RCON_API_URL, API_TOKEN, log_file_path]):
        print("Fehler: Nicht alle erforderlichen Umgebungsvariablen wurden festgelegt.")
        return

    subprocess.Popen(["tail", "-f", log_file_path], stdout=subprocess.PIPE)  # Logdatei im Hintergrund überwachen
    monitor_game_log(log_file_path)

if __name__ == "__main__":
    main()
