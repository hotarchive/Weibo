import os

import util
from util import logger
from weibo import Weibo


def generate_archive_md(searches, topics):
    """生成归档readme
    """
    def search(item):
        return '1. [{}]({})'.format(item['desc'], item['scheme'])

    def topic(item):
        detail = ''
        if 'card_expand' in item:
            if 'content' in item['card_expand']:
                detail = item['card_expand']['content']
        return '1. [{}]({})\n    - {}\n'.format(item['title_sub'], item['scheme'], detail)

    searchMd = '暂无数据'
    if searches:
        searchMd = '\n'.join([search(item) for item in searches])

    topicMd = '暂无数据'
    if topics:
        topicMd = '\n'.join([topic(item) for item in topics])

    readme = ''
    file = os.path.join('template', 'archive.md')
    with open(file) as f:
        readme = f.read()

    readme = readme.replace("{updateTime}", util.current_time())
    readme = readme.replace("{searches}", searchMd)
    readme = readme.replace("{topics}", topicMd)

    return readme


def generate_readme(searches, topics):
    """生成今日readme
    """
    def search(item):
        return '1. [{}]({})'.format(item['desc'], item['scheme'])

    def topic(item):
        detail = ''
        if 'card_expand' in item:
            if 'content' in item['card_expand']:
                detail = item['card_expand']['content']
        return '1. [{}]({})\n    - {}\n'.format(item['title_sub'], item['scheme'], detail)

    searchMd = '暂无数据'
    if searches:
        searchMd = '\n'.join([search(item) for item in searches])

    topicMd = '暂无数据'
    if topics:
        topicMd = '\n'.join([topic(item) for item in topics])

    readme = ''
    file = os.path.join('template', 'README.md')
    with open(file) as f:
        readme = f.read()

    readme = readme.replace("{updateTime}", util.current_time())
    readme = readme.replace("{searches}", searchMd)
    readme = readme.replace("{topics}", topicMd)

    return readme


def save_readme(md):
    logger.debug('readme:%s', md)
    util.write_text('README.md', md)


def save_archive_md(md):
    logger.debug('archive md:%s', md)
    name = '{}.md'.format(util.current_date())
    file = os.path.join('archives', util.current_date_year(), util.current_date_month(), name)
    util.write_text(file, md)


def save_raw_content(content: str, filePrefix: str):
    filename = '{}-{}.json'.format(filePrefix, util.current_date())
    file = os.path.join('raw', util.current_date_year(), util.current_date_month(), filename)
    util.write_text(file, content)


def run():
    weibo = Weibo()
    # 热搜
    searches, resp = weibo.get_hot_search()
    if resp:
        save_raw_content(resp.text, 'hot-search')
    # 话题榜
    topics, resp = weibo.get_hot_topic()
    if resp:
        save_raw_content(resp.text, 'hot-topic')

    # 最新数据
    readme = generate_readme(searches, topics)
    save_readme(readme)
    # 归档
    archiveMd = generate_archive_md(searches, topics)
    save_archive_md(archiveMd)


if __name__ == "__main__":
    run()
