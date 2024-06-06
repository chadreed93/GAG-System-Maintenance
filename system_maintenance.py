import os
import subprocess
import shutil
from datetime import datetime

def run_windows_update():
    print("Starting Windows Update...")
    subprocess.run(['powershell', 'Start-WindowsUpdate'], check=True)
    print("Windows Update completed.")

def run_windows_defender_scan():
    print("Starting Windows Defender quick scan...")
    subprocess.run(['powershell', 'Start-MpScan -ScanType QuickScan'], check=True)
    print("Windows Defender quick scan completed.")

def create_local_backup(source_dirs, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    os.makedirs(backup_path)

    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            dest_dir = os.path.join(backup_path, os.path.basename(source_dir))
            shutil.copytree(source_dir, dest_dir)
            print(f"Backup completed for {source_dir} to {dest_dir}")
        else:
            print(f"Source directory {source_dir} does not exist.")

def main():
    # Run Windows Update
    run_windows_update()

    # Run Windows Defender Scan
    run_windows_defender_scan()

    # Backup Directories
    source_dirs = [
        'C:\\Users\\YourUsername\\Documents',
        'C:\\Users\\YourUsername\\Pictures'
    ]
    backup_dir = 'D:\\Backups'
    create_local_backup(source_dirs, backup_dir)

if __name__ == "__main__":
    main()
