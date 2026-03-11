"""Inject TwitterAPI.io API key into agent environment for code_execution_tool."""

import os

from helpers.extension import Extension
from helpers import plugins
from agent import LoopData


class TwitterApiIoConfig(Extension):

    async def execute(self, loop_data: LoopData = LoopData(), **kwargs):
        config = plugins.get_plugin_config("twitterapiio", self.agent)
        if not config:
            return

        api_key = config.get("api_key", "")
        if api_key:
            os.environ["TWITTERAPIIO_API_KEY"] = api_key
