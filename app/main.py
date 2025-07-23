from flask import Flask, jsonify, redirect, request
from werkzeug.exceptions import BadRequest, NotFound

from .models import InMemoryDB
from .services import UrlShortenerService

db = InMemoryDB()
svc = UrlShortenerService(db)

app = Flask(__name__)

# ---- Health check ----
@app.get("/healthz")
def health():
    return {"status": "ok"}

# ---- API: shorten ----
@app.post("/api/shorten")
def create_short_url():
    if not request.is_json:
        raise BadRequest("request content-type must be application/json")

    url = request.json.get("url")
    if not url:
        raise BadRequest("missing 'url' field")

    try:
        code, _ = svc.shorten(url)
    except ValueError as e:
        raise BadRequest(str(e))

    host = request.host_url.rstrip("/")
    return jsonify({"short_code": code, "short_url": f"{host}/{code}"}), 201

# ---- Redirect ----
@app.get("/<string:code>")
def redirect_short_url(code: str):
    try:
        dest = svc.resolve(code)
    except KeyError:
        raise NotFound("short code not found")
    return redirect(dest, code=302)

# ---- Analytics ----
@app.get("/api/stats/<string:code>")
def stats(code: str):
    try:
        return jsonify(svc.stats(code))
    except KeyError:
        raise NotFound("short code not found")

# ---- Error handlers ----
@app.errorhandler(BadRequest)
def handle_400(err):
    return jsonify(error=str(err)), 400

@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify(error=str(err)), 404
