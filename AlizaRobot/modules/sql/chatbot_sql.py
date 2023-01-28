import threading

from sqlalchemy import Column, String

from AlizaRobot.modules.sql import BASE, SESSION


class AlizaChats(BASE):
    __tablename__ = "aliza_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


AlizaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_aliza(chat_id):
    try:
        chat = SESSION.query(AlizaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_aliza(chat_id):
    with INSERTION_LOCK:
        alizachat = SESSION.query(AlizaChats).get(str(chat_id))
        if not alizachat:
            alizachat = AlizaChats(str(chat_id))
        SESSION.add(fallenchat)
        SESSION.commit()


def rem_aliza(chat_id):
    with INSERTION_LOCK:
        alizachat = SESSION.query(AlizaChats).get(str(chat_id))
        if alizachat:
            SESSION.delete(alizachat)
        SESSION.commit()
