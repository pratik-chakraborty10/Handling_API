import requests

def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    object=response.json()

    if object["success"] and "data" in object:
        user_data=object["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username,country=fetch_random_user_freeapi()
        print(f"username:{username} \n country:{country}")
    except  Exception as e:
        print(str(e))


if __name__=="__main__":
    main()
