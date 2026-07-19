from Infrastructure.DB.repo_implement.user_repo_impl import user_repo_impl


class userUseCases:
    def __init__(self, session):
        self.implement = user_repo_impl(session)    

    def addUserUseCase(self, data):
        user = self.implement.build_user(data)
        return self.implement.add_user(user)


    def updateUserUseCase(self, data):
        current_user = self.implement.get_user(email=data.email,user_name=data.user_name)
        updated_user = {k: v for k, v in data.__dict__.items() if v is not None}
        updated_user = current_user.replace_items(current_user)

        return self.implement.update_user(updated_user)

    def authenticate_user_password(self, data):
        user = self.implement.get_user(email=data.email,user_name=data.user_name)
        return user.auth_password(data.password)

    def deleteUserUseCase(self, email = None, user_name = None):
        return self.implement.delete_user(email, user_name)

    def getUserUseCase(self, email = None, user_name = None):
        return self.implement.get_user(email, user_name)
    
    def listUsersUseCase(self):
        return self.implement.list_users()
    