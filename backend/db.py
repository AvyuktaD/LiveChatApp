from pymongo import MongoClient

try:
    URL = "mongodb://localhost:27017/LiveChatRoom"
    client = MongoClient(URL)
    db = client.get_database()

    usersCollection = db['users']
    
    def signUp(userName,email):
        userInfo = {"username":userName,"email":email}
        insert_user = usersCollection.insert_one(userInfo)
        if insert_user:
            return True

except Exception as e:
    print(f"There was an error {e}")