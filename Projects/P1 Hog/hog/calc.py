import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

