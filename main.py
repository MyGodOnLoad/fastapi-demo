import asyncio

import uvicorn

from core.lib import util
from core.lib.cfg import get_cmd_opts, load_cfg


def _set_proactor_eventloop() -> None:
    """
    set eventloop as ProactorEventLoop, maybe used in windows system
    then in uvicorn main script, add these codes:
    >>> from uvicorn.config import LOOP_SETUPS
    >>> LOOP_SETUPS['asyncio'] = 'core.lib.aio:set_proactor_eventloop'
    if proactor loop is set, do not enable reload in development
    :return: None
    """
    asyncio.set_event_loop(asyncio.ProactorEventLoop())


def main() -> None:
    """
    main function, steps are:
    1. Get cmd opts with the current environment (dev/prod)
    2. Read configs by env (uvicorn.json, logger.json)
    3. Run uvicorn application, launch APP in app/__init__.py
    for more uvicorn args, refer to uvicorn/config.py
    :return: None
    """
    opts = get_cmd_opts()
    print('launch uvicorn with cmd opts: %s' % util.pfmt(opts))
    cfg = load_cfg(opts['env'])
    print('launch uvicorn with cfg: %s' % util.pfmt(cfg, width=120))
    uvicorn.run('app:APP', **cfg)


if __name__ == '__main__':
    main()
