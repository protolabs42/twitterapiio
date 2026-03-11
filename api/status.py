"""Status endpoint for TwitterAPI.io plugin."""

from helpers.api import ApiHandler, Request, Response


class Status(ApiHandler):
    async def handle(self, req: Request, res: Response):
        try:
            from helpers import plugins

            config = plugins.get_plugin_config("twitterapiio")
            has_key = bool(config and config.get("api_key"))

            return res.ok(
                data={
                    "status": "configured" if has_key else "unconfigured",
                    "has_api_key": has_key,
                }
            )
        except Exception as e:
            return res.error(str(e), status=500)
