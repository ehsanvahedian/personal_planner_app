from Domain.repository.document_repository import document_repository
from ..ORM.document_ORM import document_ORM, documents_list


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
            
            document: document_ORM = self.session.query(document_ORM).filter(document_ORM.id == id).first()
            return document.to_entity()

        except Exception as e:
            return {
                "status": "failure",
                "message": str(e)
            }

    def list_documents(self) -> documents_list:
        try:
            docs: list[document_ORM] = self.session.query(document_ORM).all()
            docs = list(map(lambda doc: doc.to_entity(), docs))
            return documents_list("success", docs)

        except Exception as e:
            return documents_list("failure", str(e))