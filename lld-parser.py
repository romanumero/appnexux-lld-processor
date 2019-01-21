
from google.protobuf.internal.decoder import _DecodeVarint
import gzip
import shutil
import appnexus.standard_feed_pb2
import datetime
import time
import sys


def main():
    bucket = sys.argv[1]
    filename = sys.argv[2]

    with gzip.open(filename=bucket + filename + '.gz', mode='r') as pbIn, open('/tmp/'+filename, 'wb') as pbOut:
        shutil.copyfileobj(pbIn, pbOut)

    protos = readAppNexusDataProtoFile('/tmp/' + filename)

    for proto in protos:
        print(datetimeParser(proto.date_time).tm_year)


def readAppNexusDataProtoFile(protoFile):
    protos = []
    with open(protoFile, 'rb') as f:
        data = f.read()

        pos = 0
        while (pos < len(data)):
            (size, pos) = _DecodeVarint(data, pos)
            proto = appnexus.standard_feed_pb2.standard_feed()
            proto.ParseFromString(data[pos:(pos+size)])
            pos += size
            protos.append(proto)
    return protos


def datetimeParser(millis):
    return time.localtime(millis)


if __name__ == '__main__':
    main()
