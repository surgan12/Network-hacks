from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

auth=DummyAuthorizer()
auth.add_user('test','1234','/home/surgan/',perm="elradfmw")

handler=FTPHandler
handler.authorizer=auth

servers=FTPServer(("127.0.0.1",1026),handler)
servers.serve_forever()

