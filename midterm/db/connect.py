from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb+srv://weiian:1234@cluster0.llxpm.mongodb.net/databaseTest1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")