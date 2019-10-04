VERSION = (0, 9, 4)
__version__ = '.'.join(map(str, VERSION))
try:
    from .punc import Punctuator
except ImportError as exc:
    import traceback
    traceback.print_exc()
