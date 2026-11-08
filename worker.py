
from flask import Response, request
from pyodide.ffi import run_sync
from workers import wsgi
from app import app


@app.route("/<path:path>")
def serve_static(path):
    assets = request.environ["workers.env"].ASSETS

    response = run_sync(
        assets.fetch(f"https://assets.local/{path}")
    )

    body = run_sync(response.bytes())

    return Response(
        body,
        status=response.status,
        headers=response.headers
    )


Default = wsgi.entrypoint(app)
