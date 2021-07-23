projects = []
socials = []
social_keys = {}

import asyncio, json, sys
async def recache(cache):# https://pgjones.gitlab.io/quart/how_to_guides/background_tasks.html
    while True:
        cache.projects = json.loads(open('bduck/projects.json' if sys.platform == 'linux' else 'projects.json').read())
        cache.socials = json.loads(open('bduck/socials.json' if sys.platform == 'linux' else 'socials.json').read())
        cache.social_keys = {}
        for x in cache.socials:
            cache.social_keys[x['name'].lower()] = x['link']
        await asyncio.sleep(14400)
