if __package__ is None:
    from lib import test
else:
    from . lib import test

print(test.get_square(4))