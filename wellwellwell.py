import time
import pyautogui
import requests

# api key steam
steam_api_key = "YOUR_STEAM_API_KEY"

steam_profile_id = "STEAM_PROFILE_ID"

friend_profile_id = "FRIEND_PROFILE_ID"

destiny_2_appid = 1085660

def send_message():
    # tab
    pyautogui.hotkey('shift', 'tab')
    time.sleep(1)  
    
    pyautogui.click(x=100, y=200)  # set to screen size/resolution or rest wont work maybe
    time.sleep(1) 
    
    pyautogui.typewrite("Well well well")
    pyautogui.press('enter')

def check_friend_playing_destiny2():
    url = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={steam_profile_id}&relationship=friend"
    response = requests.get(url)
    friend_data = response.json()
    friends = friend_data["friendslist"]["friends"]

    for friend in friends:
        if friend["steamid"] == friend_profile_id:
            game_url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={friend_profile_id}"
            game_response = requests.get(game_url)
            game_data = game_response.json()
            game_info = game_data["response"]["players"][0]["gameextrainfo"]
            if game_info and destiny_2_appid in game_info:
                return True
    return False

# loop at this
while True:
    if check_friend_playing_destiny2():
        send_message()
        time.sleep(10) 
    else:
        time.sleep(10) 
