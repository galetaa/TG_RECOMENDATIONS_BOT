from data.containers.sources import channels
from telethon.sync import TelegramClient, Message
from telethon.tl.functions.messages import GetHistoryRequest
from data.functions.Distributor import add_news
from datetime import datetime, timedelta
from data.containers.config import parse_api_id, parse_api_hash
from data.containers.config import max_message_len, min_message_len
from data.containers.key_words import wrn_wrd
from pytz import UTC

db_path = '/Users/Acer/Documents/Programming/TG_RECOMENDATIONS_BOT/data/db' \
          '/databases/database.db'


def parse_channel(client: TelegramClient, ch,
                  messages_to_parse: int = 10):
    utc = UTC

    parse_time = datetime.now()
    parse_time -= timedelta(hours=1, minutes=parse_time.minute,
                            seconds=parse_time.second,
                            microseconds=parse_time.microsecond)
    parse_time = utc.localize(parse_time)
    last_messages_history = client(GetHistoryRequest(
        peer=ch,
        limit=messages_to_parse,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    for msg in last_messages_history.messages:
        msg_date = msg.date + timedelta(hours=3)
        if msg_date > parse_time and message_is_correct(msg):
            add_news(msg, db_path)


def message_is_correct(msg: Message):
    if msg.forward is not None:
        return False
    msg_text = msg.message
    if len(msg_text) > max_message_len or len(msg_text) < min_message_len:
        return False
    for wrong_word in wrn_wrd:
        if wrong_word in msg_text:
            return False
    return True


def parse_all_channels():
    api_id = parse_api_id
    api_hash = parse_api_hash

    client = TelegramClient('session', api_id, api_hash)
    client.start()

    for chn in channels:
        channel_entity = client.get_entity(chn)
        parse_channel(client, channel_entity)


if __name__ == '__main__':
    parse_all_channels()
