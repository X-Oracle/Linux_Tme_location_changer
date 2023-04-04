# Linux_Tme_location_changer
A Python script to change your server time location (time zone) to a new location .

# Scipt Details
- this script helps you change your VPS linux Server timezone to the location You want.
- in order to use this script you need to know your timezome in a correct format.
  - like (example: Asia/Tehran)
  - you can google it or use [TimeZones List](http://www.timezoneconverter.com/cgi-bin/timezones.tzc)

# Requirements
- updated and upgrade apt :
```bash
sudo apt update && apt upgrade -y
```
- Python3
```bash
sudo apt install python3 -y
```

## Auto Download :
1. Run bellow script :
```bash
python3 <(curl -Ls https://raw.githubusercontent.com/X-Oracle/Linux_Tme_location_changer/main/timezone_changer.py)
```
2. follow script .

## Manual Download:
1. Download The Python File ftrom source
2. Put it in a location you can remember like `/root/`
3. Run bellow command :
```bash
sudo python3 /root/timezone_changer.py
```
4. follow script.
