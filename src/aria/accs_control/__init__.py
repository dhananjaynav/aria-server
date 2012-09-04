# user credentials. Run independ to set one.

import md5
import pickle
import os

HOME = os.getenv("HOME")
datapath=os.path.join(HOME,'.aria_key')

def auth(user,password):
        key = read_key()
        try:
                hash = md5.new(password)
                if (user == key[0]) and (hash.hexdigest() == key[1]):
                        return True
        except TypeError:
                return False
        return False

def read_key():
        file = open(datapath)
        list = pickle.load(file)
        file.close()
        return list

def create_key():
        file = open(datapath,"w")
        pashash = md5.new()
        list = []
        username = str(raw_input("Enter Username:"))
        password = str(raw_input("Password:"))

        pashash.update(password)
        password = pashash.hexdigest()
        list.append(username)
        list.append(password)
        pickle.dump(list,file)
        file.close()

if __name__ == "__main__":
        create_key()