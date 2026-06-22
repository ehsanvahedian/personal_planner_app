from Domain.repository.document_repository import document_repository
from ..ORM.document_ORM import document_ORM


class document_repo_impl(document_repository):

    def __init__(self, session):
        self.session = session

    def add_document(self, document_data):
        try:
            doc = document_ORM(**document_data.__dict__)

            self.session.add(doc)
            self.session.commit()

            return {
                "status": "success",
                "message": "document created",
                "data": doc
            }

        except Exception as e:
            self.session.rollback()

            return {
                "status": "failure",
                "message": str(e)
            }

    def update_document(self, document_data):
        try:
            res = (
                self.session.query(document_ORM)
                .filter(document_ORM.id == document_data.id)
                .update(document_data.__dict__)
            )

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

    def delete_document(self, id):
        try:
            res = (
                self.session.query(document_ORM)
                .filter(document_ORM.id == id)
                .delete()
            )

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

    def get_document(self, id):
        try:
            return (
                self.session.query(document_ORM)
                .filter(document_ORM.id == id)
                .first()
            )

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_documents(self):
        try:
            docs = self.session.query(document_ORM).all()

            return {
                "status": "success",
                "data": docs
            }

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }