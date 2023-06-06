import kontur.pie as pie
from kontur.pie.tools.ib import FileConnector

import os

if pie.os.name == "posix":
    pie.v83_bin = "/opt/1cv8/current"
else:
    pie.v83_bin = "C:\\Program Files\\1cv8\\8.3.22.1750\\bin"

src_dir = "src/lib"


def dump():
    ib = __current_base()
    ib.close_designer()

    ib.dump_cfg(cfg_src=src_dir)

    ib.open_designer()


def build():
    ib = __current_base()
    ib.close_designer()

    ib.load_cfg(cfg_src=src_dir, update=False)
    
    ib.open_designer()


def __current_base():
    username = pie.os.environ.get("IB_USERNAME", "")
    password = pie.os.environ.get("IB_PASSWORD", "")
    name = pie.os.environ.get("IB_NAME")

    assert name, "Не указана база для подключения"

    auth = pie.ib.Auth(username=username, password=password)
    connector = pie.ib.ListConnector(auth=auth, name=name)
    ib = pie.ib.InfoBase(connector)

    return ib
