import cache, asyncio, sys
from quart import Quart, render_template, redirect, request, make_response

app = Quart(__name__)
app.url_map.strict_slashes = False

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

if sys.platform != 'linux':# Add no cache headers if running locally
    async def cache_headers(r):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        return r
    app.after_request(cache_headers)

@app.before_serving
async def schedule_cache():
    asyncio.ensure_future(cache.recache(cache))

@app.route('/')
async def homepage():
    return await render_template("index.html", projects=cache.projects, socials=cache.socials)

@app.route('/legal')
async def legal():
    return await render_template("legal.html")

@app.route('/safety')
async def safety():
    return await render_template("safety.html")

@app.route('/discord')
async def discord():
    return redirect(cache.social_keys['discord'])

@app.route('/twitter')
async def twitter():
    return redirect(cache.social_keys['twitter'])

@app.route('/license')
@app.route('/license.txt')
async def license():
    return await app.send_static_file("license.txt")

@app.route('/robots')
@app.route('/robots.txt')
async def robots():
    return await app.send_static_file("robots.txt")

@app.route('/sitemap')
@app.route('/sitemap.xml')
async def sitemap():
    return await app.send_static_file("sitemap.xml")

@app.route('/files/<string:file_name>')
async def old_file_route(file_name):
    return await app.send_static_file(file_name)

@app.errorhandler(404)
async def page_not_found(e):
    return await make_response(await render_template("404.html"), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
