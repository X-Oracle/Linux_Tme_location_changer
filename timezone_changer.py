import subprocess
import platform

def clear_terminal():
    subprocess.run(["clear"])

current_os = platform.system()
current_os = ""

if current_os == "Windows":
    print(f"Script can't Run on {current_os}")
    exit()

clear_terminal()

current_time_zone = (
    subprocess.check_output(["timedatectl", "show", "-p", "Timezone"])
    .decode()
    .split("=")[-1]
)
# current_time_zone = "Timezone=Etc/UTC".split("=")[-1]
print(
    f"Current time location: {current_time_zone}",
)

while True:
    new_location = input(
        "Enter new time location (ex: Asia/Tehran) (type 'n' to exit): "
    )
    
    clear_terminal()
    
    if new_location.lower() == "n":
        exit()
    elif new_location == "":
        clear_terminal()
        continue


    time_zone_list = tuple(
        subprocess.check_output(["timedatectl", "list-timezones"]).decode().split("\n")
    )

    if new_location in time_zone_list:
        clear_terminal()
        break
    else:
        clear_terminal()
        print("Time location is wrong.Try Again !")


are_you_sure = input(
    f"Are you sure you want to change the time location to {new_location}? (y/n)"
)

clear_terminal()

if are_you_sure.lower() == "y":
    subprocess.check_output(["timedatectl", "set-timezone", new_location])
    print("Time location changed successfully!")
else:
    print("Exiting script.")
