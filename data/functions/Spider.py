from data.containers.sources import channels
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from data.functions.Distributor import add_news
from datetime import datetime, timedelta
from data.containers.config import parse_api_id, parse_api_hash
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
        if msg_date > parse_time:
            add_news(msg, db_path)


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
