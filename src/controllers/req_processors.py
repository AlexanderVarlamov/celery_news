from typing import Dict

from controllers.actions import get_news_list
from database.db_actions import get_sources_from_db
from models.models import RssSource


async def process_raw_news_request(sources_list: list[RssSource]) -> Dict:
    news_to_return = {}
    for one_source in sources_list:
        source_name = one_source.name
        news = await get_news_list(one_source.rss)
        news_to_return.update({source_name: news})

    return news_to_return


async def get_json() -> Dict:
    sources = await get_sources_from_db()
    news = await process_raw_news_request(sources)
    return news
