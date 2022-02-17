import getopt
import json
import os
import sys
from typing import Any, Dict

from core.lib import util


def get_cmd_opts() -> Dict[str, Any]:
    """
    get commandline opts
    :return: cmd options
    """
    # get options
    try:
        opts, _ = getopt.getopt(
            sys.argv[1:],
            'e:t:',
            ['env=', 'tag=']
        )
    except getopt.GetoptError as e:
        raise e
    t = {
        'env': 'dev',
        'tag': ''
    }
    for o, a in opts:
        if o == '-e':
            t['env'] = a
        elif o == '-t':
            t['tag'] = a
    return t


def load_cfg(env: str) -> Dict[str, Any]:
    """
    load configs
    :param env: app env
    :return: uvicorn cfg dict
    """
    if not env:
        raise Exception('env not specified')
    cfg_dir = os.path.join('cfg', env)
    assert os.path.isdir(cfg_dir)

    # logger cfg
    logger_cfgpath = os.path.join(cfg_dir, 'logger.json')
    logger_cfg = json.loads(open(logger_cfgpath, encoding=util.ENCODING).read())
    assert isinstance(logger_cfg, dict)

    # uvicorn cfg
    default_uvicorn_cfg = {
        'log_config': logger_cfg,
        'env_file': os.path.join(cfg_dir, 'app.cfg'),
        'loop': 'asyncio'
    }
    uvicorn_cfgpath = os.path.join(cfg_dir, 'uvicorn.json')
    uvicorn_cfg = json.loads(open(uvicorn_cfgpath, encoding=util.ENCODING).read())
    assert isinstance(uvicorn_cfg, dict)

    return dict(default_uvicorn_cfg, **uvicorn_cfg)
