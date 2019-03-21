# app
from .egginfo import EggInfoConverter
from .pip import PIPConverter
from .pipfile import PIPFileConverter
from .pipfilelock import PIPFileLockConverter
from .poetry import PoetryConverter
from .poetrylock import PoetryLockConverter
from .pyproject import PyProjectConverter
from .sdist import SDistConverter
from .setuppy import SetupPyConverter
from .wheel import WheelConverter


CONVERTERS = dict(
    egginfo=EggInfoConverter(),
    sdist=SDistConverter(),

    pip=PIPConverter(lock=False),
    piplock=PIPConverter(lock=True),

    pipfile=PIPFileConverter(),
    pipfilelock=PIPFileLockConverter(),

    poetry=PoetryConverter(),
    poetrylock=PoetryLockConverter(),

    pyproject=PyProjectConverter(),

    setuppy=SetupPyConverter(),

    wheel=WheelConverter(),
)
