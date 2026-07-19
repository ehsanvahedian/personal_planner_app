from Domain.repository.user_repository import user_repository
from ..ORM.user_ORM import user_ORM, users_list


class user_repo_impl(user_repository):

    def __init__(self, session):
        self.session = session

    def add_user(self, user_data):
        try:
            user = user_ORM(**user_data.__dict__)

            self.session.add(user)
            self.session.commit()

            return {
                "status": "success",
                "message": "user created",
                "data": user.to_entity()
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def update_user(self, user_data):
        try:
            user = (
                self.session.query(user_ORM).filter(user_ORM.email == user_data.email) and
                self.session.query(user_ORM).filter(user_ORM.user_name == user_data.user_name)
                    )
            
            res = user.update(user_data.__dict__)

            self.session.commit()

            return {
                "status": "success",
                "message": f"{res} row updated"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def delete_user(self, email = None, user_name = None):
        try:

            user = (
                email if self.session.query(user_ORM).filter(user_ORM.email == email) else
                self.session.query(user_ORM).filter(user_ORM.user_name == user_name)
                )
            
            res = user.delete()

            self.session.commit()

            return {
                "status": "success",
                "message": f"{res} row deleted"
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def get_user(self, email = None, user_name = None):
        try:
            
            user: user_ORM = (
                email if self.session.query(user_ORM).filter(user_ORM.email == email) else
                self.session.query(user_ORM).filter(user_ORM.user_name == user_name)
                ).first()
            return user.to_entity()

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_users(self) -> users_list:
        try:
            users : list[user_ORM] = (
                self.session.query(user_ORM)
                .filter(user_ORM.completed == False)
                .all()
            )

            return users_list("success", "", users)

        except Exception as e:
            return users_list("failure", str(e))