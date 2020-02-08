import json
import os
import uuid

DATA_FILE_PATH="users.json"
def read():
    if not os.path.exists(DATA_FILE_PATH):
        return[]
    with open(DATA_FILE_PATH) as fd:
        users=json.load(fd)
        return users

def save(users):
    with open(DATA_FILE_PATH, "w") as fd:
        json.dump(users, fd)

def main():
    users_list=read()
    print("идет запись данных")
    first_name=input("name:")
    last_name=input("sir name:")
    email=input("email:")
    user_id=str(uuid.uuid4())
    user={
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    users_list.append(user)
    save(users_list)
    print("Thanks, data is saved")

if __name__ == "__main__":
    main()