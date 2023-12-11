import json

class User:
    def __init__(self, name, age): #instance variables
        self.name = name
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User) : # if object is of class user checks if is instance of a class
        #if so return dict with all instance variables as key value pairs
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True} #object.name, key age: object.age, class name as key o.__class__.__name__: value doesn't matter so True
    else:
        raise TypeError('Object of type User is not JSON serializable')

#Implement custom JSON encoder
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    #override default method encode_user
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        #otherwise let base json encoder handle it
        return JSONEncoder.default(self, o)
userJSON = UserEncoder().encode(user) #class argument as class with UserEncoder
print(userJSON) #{"name": "Max", "age": 27, "User": true}

#decode into user object by writing custom decoding method
def decode_user(dct):
    if User.__name__ in dct: #checks if dictionary contains a user key, in encod_user func added class as key
        #then create and return user object
        return User(name=dct['name'], age=dct['age']) #gets name from dict, dict with key name, age of dict
    #otherwise returns dict
    return dict


#Decode object back, user json format converted back to normal python object
user = json.loads(userJSON, object_hook=decode_user) #method object_hook set to decoding message
print(type(user))
print(user) #print(type(user)) <class 'dict'>
# {"name": "Max", "age": 27, "User": true}
# {'name': 'Max', 'age': 27, 'User': True}
