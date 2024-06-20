from pymongo import MongoClient

try:
    URL = "mongodb://localhost:27017/LiveChatRoom"
    client = MongoClient(URL)
    db = client.get_database()

    usersCollection = db['users']
    
    def signUp(userName,email):
        user = usersCollection.find({"username":userName})
        a = []

        for i in user:
            a.append[i]

        userInfo = {"username":userName,"email":email}
        insert_user = usersCollection.insert_one(userInfo)
        
        if len(a) > 0:
            if insert_user:
                return True
            else:
                return False
        else:
            return False

except Exception as e:
    print(f"There was an error {e}")