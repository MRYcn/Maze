import os.path
import uuid, json, platform

class Data_Manager:
    def __init__(self):
        self.DEF_DATA={
            'version':'1.0.0',
            'user':{
                'id':str(uuid.uuid4()),
                'name':'Guest',
                'password':None,
                'last_login':None,
                'is_online':False
            },
            'device':{
                'id':str(uuid.uuid4()),
                'os':f'{platform.system()} {platform.release()}'
            }
        }
        USER_HOME=os.path.expanduser('~')
        DATA_DIR=os.path.join(USER_HOME,'.MazeChallenge')
        self.FILE_PATH=os.path.join(DATA_DIR,'user_info.json')
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    def load_data(self):
        try:
            with open(self.FILE_PATH,'r') as f:
                data=json.load(f)
                #版本迁移...
                return data
        except Exception as e:
            print(e)
            self.save_data(self.DEF_DATA)
            return self.DEF_DATA

    def save_data(self,data):
        try:
            with open(self.FILE_PATH,'w') as f:
                json.dump(data,f,indent=2)
        except Exception as e:
            print(e)