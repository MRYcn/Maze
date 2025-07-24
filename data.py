import os.path
import uuid, json, platform
from json import JSONDecodeError
from packaging import version


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
            },
            'data':{
                'map':[0]
            }
        }
        USER_HOME=os.path.expanduser('~')
        self.DATA_DIR=os.path.join(USER_HOME,'.MazeChallenge')
        self.FILE_PATH=os.path.join(self.DATA_DIR,'user_info.json')
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)

    def load_data(self):
        try:
            with open(self.FILE_PATH,'r') as f:
                data=json.load(f)
                user_v=version.parse(data['version'])
                new_v=version.parse(self.DEF_DATA['version'])
                if new_v>user_v:
                    data['version']=self.DEF_DATA['version']
                    for key1 in self.DEF_DATA.keys():
                        if key1 not in data:
                            data[key1]=self.DEF_DATA[key1]
                        if isinstance(self.DEF_DATA[key1],dict):
                            for key2 in self.DEF_DATA[key1].keys():
                                if key2 not in data[key1]:
                                    data[key1][key2]=self.DEF_DATA[key1][key2]
                    print('用户数据更新完成。')
                return data
        except FileNotFoundError:
            self.save_data(self.DEF_DATA)
            return self.DEF_DATA
        except JSONDecodeError:
            dst_file=os.path.join(self.DATA_DIR,'user_info.json.bak')
            os.rename(self.FILE_PATH,dst_file)
            self.save_data(self.DEF_DATA)
            print('用户数据损坏，已自动备份原文件为 user_info.json.bak，并重建用户数据于 user_info.json。')
            return self.DEF_DATA
        except Exception as e:
            self.save_data(self.DEF_DATA)
            print('未知错误：',e,'已重建用户数据。',sep='\n')
            return self.DEF_DATA

    def save_data(self,data):
        try:
            with open(self.FILE_PATH,'w') as f:
                json.dump(data,f,indent=2)
        except Exception as e:
            print(e)