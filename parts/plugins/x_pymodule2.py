import logging

import snapcraft
from snapcraft.common import get_python2_path
from snapcraft.plugins import python2

from os.path import basename, dirname

logger = logging.getLogger(__name__)


class XPymodule2Plugin(snapcraft.plugins.python2.Python2Plugin):

    def __init__(self, name, options):
        snapcraft.BasePlugin.__init__(self, name, options)

    def env(self, root):
        logger.info('env request for %s' % root)
        path = root
        if basename(root) == "install":
            path = dirname(dirname(root)) + '/python2/install'
        try:
            path2 = get_python2_path(path)
        except EnvironmentError as e:
            print(e)
        logger.info('trying %s' % path)
        return ['PYTHONPATH={0}'.format(get_python2_path(path))]

    def pull(self):
        logger.info('pre-pull')
        super().pull()
        logger.info('post-pull')

