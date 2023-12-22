import threading

from sqlalchemy import Column, String

from AbingRobot.modules.sql import BASE, SESSION


class AbingChats(BASE):
    __tablename__ = "abing_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


AbingChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_abing(chat_id):
    try:
        chat = SESSION.query(AbingChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_abing(chat_id):
    with INSERTION_LOCK:
        abingchat = SESSION.query(AbingChats).get(str(chat_id))
        if not abingchat:
            abingchat = AbingChats(str(chat_id))
        SESSION.add(abingchat)
        SESSION.commit()


def rem_abing(chat_id):
    with INSERTION_LOCK:
        Abingchat = SESSION.query(AbingChats).get(str(chat_id))
        if abingchat:
            SESSION.delete(abingchat)
        SESSION.commit()
