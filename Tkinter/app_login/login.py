class Login:

    def __init__(self):
        self.__user = "Admin"
        self.__password = "Admin123_"


    @property
    def user(self):
        return self.__user


    @property
    def password(self):
        return self.__password


    def validacion(self, user, password):
        return self.user == user and self.password == password

