import subprocess

# List of Python scripts to execute
scripts = ['t1.py', 't2.py', 't3.py']

# Loop through each script and execute them one by one
for script in scripts:
    print(f"Executing {script}...")
    try:
        # Execute the script using subprocess.run()
        subprocess.run(['python3', script], check=True)
        print(f"{script} executed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle any error that occurred during script execution
        print(f"Error executing {script}: {e}")
    print("=" * 40)  # Print separator between script executions
