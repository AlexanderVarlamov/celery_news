import asyncio
from typing import Dict

from controllers.actions import get_news_list
from database.db_actions import get_sources, insert_news
from models.models import RssSource


# def get_sources(lst: list[str]):
#     if lst == ['all']:
#         news_to_get = sources.keys()
#     else:
#         news_to_get = [item for item in lst if item in sources.keys()]
#     return news_to_get


async def process_raw_news_request(sources_list: list[RssSource]) -> Dict:
    news_to_return = {}
    for one_source in sources_list:
        source_name = one_source.name
        news = await get_news_list(one_source.rss)
        news_to_return.update({source_name: news})

    return news_to_return


async def get_json() -> Dict:
    sources = await get_sources()
    news = await process_raw_news_request(sources)
    return news

