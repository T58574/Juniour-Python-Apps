from calendar import month
import requests as re
import time
from webbrowser import open_new_tab as tab
import datetime


def main():
    def formating_token(s: str):
        s = s.replace("https://oauth.vk.com/blank.html#access_token=", "")
        
        # Put your user id
        s = s.replace("&expires_in=86400&user_id=<<YOUR USER ID>>", "")
        s = s.replace(" ", "")
        return s

    def get_token(app_id: int, v):
        get_url = tab(
            f"https://oauth.vk.com/authorize?client_id={app_id}&/redirect_uri=https://oauth.vk.com/blank.hmtl&scope=friends&response_type=token&/display=page/")
        get_url = input('Put stroke in browser\n\n')
        token_and_v = f'&access_token={formating_token(get_url)}&v={v}'

        return token_and_v

    def get_info_user(access_token: str, domain: str):
        log_user = re.get(f'{domain}users.get?{access_token}')
        user_id = log_user.json()['response'][0]['id']
        user_firstname = log_user.json()["response"][0]["first_name"]
        user_lastname = log_user.json()["response"][0]["last_name"]
        print(
            f'\nUser id -> {user_id}\nName -> {user_firstname} {user_lastname}\n')

        return int(user_id)

    def get_user_friends(user_id: int, access_token: str, domain: str):
        get_user_friends = re.get(
            f'{domain}friends.getRequests?user_ids={user_id}&count=1000{access_token}')
        user_friends_count = get_user_friends.json()[
            "response"]["count"]
        array_user_friends = get_user_friends.json()[
            "response"]["items"]
        print(f'\nCount friends -> {user_friends_count}\n')

        return array_user_friends

    version_vk_api = 5.131
    
    # Put your app id
    app_id = <<YOUR APP ID>>
    access_token = get_token(app_id, version_vk_api)
    domain = 'https://api.vk.com/method/'

    while True:
        user_id = get_info_user(access_token, domain)
        arr = get_user_friends(user_id, access_token, domain)
        for id in arr:
            re.get(
                f'{domain}friends.add?user_id={id}{access_token}')
            get_info_about_friend = re.get(
                f'{domain}users.get?user_ids={id}{access_token}')
            friends_id = get_info_about_friend.json()[
                'response'][0]['id']
            print(f'{friends_id} -  added')
            dates = datetime.datetime.now()
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{friends_id} - {dates}\n')

            time.sleep(1)
        time.sleep(30)


if __name__ == "__main__":
    main()
