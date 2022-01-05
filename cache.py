projects = []
socials = []
social_keys = {}

import asyncio, json, sys, os, logging
async def recache(cache):# https://pgjones.gitlab.io/quart/how_to_guides/background_tasks.html
    while True:
        cache.projects = json.loads(open('projects.json').read())
        cache.projects.sort(key=lambda x: x['note'] if 'note' in x else '')
        cache.characters = json.loads(open('legal.json').read())
        cache.socials = json.loads(open('socials.json').read())

        bongo_images = os.listdir('static/bongo')
        cache.bongo_images = []
        artist_info = json.loads(open('artists.json').read())
        for x in bongo_images:
            try:
                artist, name = x.split('-')
                name = '.'.join(name.split(".")[:-1])
                new_name = []
                for a in name.split("_"):
                    new_name.append(a.capitalize())

                cache.bongo_images.append(
                                            {
                                                "artist": artist_info[str(artist)],
                                                "name": ' '.join(new_name),
                                                "url": x
                                            }
                                        )
            except Exception as e:
                logging.warning(f"An error occured when processing {x} during bongo_images caching:\n{type(e).__name__}: {e}")
        cache.bongo_images.sort(key=lambda x: x['name'])

        await asyncio.sleep(14400)
