#!/usr/bin/env python3

import jupyterhub.handlers.pages as pages
import jupyterhub.handlers.base as base
from jupyterhub import app
from cernhandlers import SpawnHandler, HomeHandler
import sys

handlers_map = {
    pages.SpawnHandler: SpawnHandler,
    pages.HomeHandler: HomeHandler
}


class SWAN(app.JupyterHub):
    name = 'swan'

    def init_handlers(self):
        super().init_handlers()
        for i, cur_handler in enumerate(self.handlers):
            new_handler = handlers_map.get(cur_handler[1])
            if new_handler:
                cur_handler = list(cur_handler)
                cur_handler[1] = new_handler
                self.handlers[i] = tuple(cur_handler)

if __name__ == "__main__":
    SWAN.launch_instance(sys.argv)
