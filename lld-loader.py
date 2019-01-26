
from google.protobuf.internal.decoder import _DecodeVarint
import gzip
import shutil
import appnexus.standard_feed_pb2
import sys
import os
import fire
from appnexus.convert.converter import *


class Loader(object):
    """ Downloads delimited protobuf files, decompresses, and parse fields"""

    def load(self, in_bucket, out_bucket):

        if not os.path.exists(out_bucket):
            os.makedirs(out_bucket)

        for root, directories, file_names in os.walk(in_bucket):
            for filename in file_names:

                full_gz_path = os.path.join(root, filename)
                full_proto_path = os.path.join(out_bucket, filename.replace('.gz',''))

                with gzip.open(filename=full_gz_path, mode='r') as fin, open(full_proto_path, 'wb') as fout:
                    shutil.copyfileobj(fin, fout)



    def read_adnxs_proto(self, proto_path):

        converters = Converter()

        for root, directories, file_names in os.walk(proto_path):
            for filename in file_names:
                full_proto_path = os.path.join(root, filename)

                protos = []
                with open(full_proto_path, 'rb') as f:
                    data = f.read()

                    pos = 0
                    while (pos < len(data)):
                        (size, pos) = _DecodeVarint(data, pos)
                        proto = appnexus.standard_feed_pb2.standard_feed()
                        proto.ParseFromString(data[pos:(pos+size)])
                        pos += size
                        protos.append(proto)

                for proto in protos:
                    print(proto.device_unique_id)


if __name__ == '__main__':
    fire.Fire(Loader)
