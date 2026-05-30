import subprocess

def run_install(choice):
    try:
        if choice.lower() == "gnome":
            cmd = ["sudo", "apt", "install", "task-gnome-desktop", "-y"]
        elif choice.lower() == "lxde":
            cmd = ["sudo", "apt", "install", "lxde", "-y"]
        else:
            print("Invalid choice. Please select 'gnome' or 'lxde'.")
            return

        result = subprocess.run(cmd, capture_output=True, text=True)
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)

    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    user_choice = input("Choose desktop environment (gnome/lxde): ")
    run_install(user_choice)
