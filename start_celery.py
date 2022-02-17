import os

from dotenv import load_dotenv

from core.lib import util
from core.lib.cfg import get_cmd_opts, load_cfg


def main() -> None:
    opts = get_cmd_opts()
    print('launch celery with cmd opts: %s' % util.pfmt(opts))
    cfg = load_cfg(opts['env'])
    load_dotenv(dotenv_path=cfg['env_file'])
    os.system('celery -A core.celery.celery worker -l info')


if __name__ == '__main__':
    main()
