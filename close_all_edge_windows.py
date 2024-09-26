import subprocess

try:
    # Use taskkill to close all instances of Microsoft Edge
    subprocess.call(["taskkill", "/F", "/IM", "msedge.exe"])
    print("All Microsoft Edge windows have been closed.")
except Exception as e:
    print(f"An error occurred: {e}")