import argparse

from xethhung12_minio_download_file import download
import urllib3
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Upload file to minio',
        description='The command download file from minio',
    )
    parser.add_argument('--url', help='the host url')
    parser.add_argument('--access-key', help='the access-key')
    parser.add_argument('--secret-key', help='the secret-key')
    parser.add_argument('--bucket', help='the bucket name')
    parser.add_argument('--remote-file', help='the remote file')
    parser.add_argument('--local-file', help='the local file')
    args = parser.parse_args()

    url = args.url
    access_key = args.access_key
    secret_key = args.secret_key
    bucket = args.bucket
    local_file = args.local_file
    remote_file = args.remote_file

    try:
        download(
            url,
            access_key,
            secret_key,
            bucket,
            remote_file,
            local_file
        )
    except Exception as ex:
        print("Error", ex)
