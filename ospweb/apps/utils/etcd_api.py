import  etcd
from   opsweb.settings import ETCD_Server, ETCD_Port
client = etcd.Client(host=ETCD_Server, port=ETCD_Port)


def  create_dir(key):
    dir = client.write(key, None, dir=True)
    if  dir.dir:
        return True
    else:
        return False


def  delete_dir(key):
    dir = client.delete(key, None, dir=True)
    if  dir.dir:
        return True
    else:
        return False


def  create_vhost(key, value):
    dir = client.write(key,value)
    if  dir.dir:
        return False
    else:
        return True


def  delete_vhost(key):
    dir = client.delete(key)
    if  dir.dir:
        return False
    else:
        return True