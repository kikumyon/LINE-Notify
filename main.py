import requests

#LINE Notifyよりアクセストークンを発行してください
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def main():
    message = input("送信内容を入力してください:") 

    api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer {}".format(ACCESS_TOKEN)}
    data = {"message": message}

    requests.post(api_url, headers=headers, data=data)


if __name__ == "__main__":
    main()