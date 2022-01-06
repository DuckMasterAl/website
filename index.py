import cache, asyncio, sys
from quart import Quart, render_template, redirect, request, make_response

app = Quart(__name__)
app.url_map.strict_slashes = False

def misc_info(request, path="..", safety=False):
    return {
                "path": path,
                "theme-color": request.headers["User-Agent"] == "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)",
                "og-image": request.headers["User-Agent"] == "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
                "safety-copyright": safety
        }

@app.before_request
async def path_redirects():
    path = request.path.lower()# case insensitive for requests
    if path != '/' and path.endswith('/'):# trailing slash
        path = path[:-1]
    if path.endswith('.html'):# removes .html from requests
        path = path[:-5]
    if path == '/index':# /index -> /
        path = '/'
    if path != request.path:# redirect if something has changed
        return redirect(path)

if sys.platform != 'linux':
    @app.after_request
    async def cache_headers(r):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        return r

@app.before_serving
async def schedule_cache():
    asyncio.ensure_future(cache.recache(cache))

@app.route('/')
async def homepage():
    return await render_template("index.html", projects=cache.projects, socials=cache.socials, misc_info=misc_info(request))

@app.route('/legal')
async def legal():
    return await render_template("legal.html", characters=cache.characters, misc_info=misc_info(request))

@app.route('/safety')
async def safety():
    return await render_template("safety.html", misc_info=misc_info(request, safety=True))

@app.route('/hotlines')
async def hotlines():
    return await render_template("hotlines.html", misc_info=misc_info(request, safety=True))

@app.route('/bongo')
async def bongo():
    return await render_template("bongo.html", bongo_images=cache.bongo_images, misc_info=misc_info(request))

@app.route('/discord')
async def discord():
    return redirect(cache.socials['discord'])

@app.route('/license')
@app.route('/license.txt')
async def license():
    return await app.send_static_file("license.txt")

@app.route('/robots.txt')
async def robots():
    return await app.send_static_file("robots.txt")

@app.route('/sitemap.xml')
async def sitemap():
    return await app.send_static_file("sitemap.xml")

@app.route('/files/<string:file_name>')
async def old_file_route(file_name):
    return await app.send_static_file(file_name)

@app.errorhandler(404)
async def page_not_found(e):
    if request.path in ["/favicon.ico", "/apple-touch-icon.png", "/browserconfig.xml"]:# Favicons!
        return await app.send_static_file(f"favicon{request.path}")
    return await render_template("404.html", misc_info=misc_info(request, "")), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
