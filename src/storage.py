from minio import Minio


class Storage(object):

    def __init__(self, address, port, accessKey, secretKey, secure=False):
        # This "location" is a placeholder and an artifact of Amazon's S3 syntax.
        # Check Minio's documentation for more information. It can safely be ignored.
        self._location = ("us-west-1")
        self._server = (address + ":" + port)
        self._secure = secure
        self._session = self._connect(address, port, accessKey, secretKey)

    def _connect(self, address, port, accessKey, secretKey):
        try:
            url = (address + ":" + port)
            session = Minio(url, accessKey, secretKey, secure=self._secure)
            return session
        except:
            return False

    def list_buckets(self):
        try:
            buckets = [bucket.name for bucket in self._session.list_buckets()]
            return buckets
        except:
            return ("Unable to connect to server: '{}'"
                    .format(self._session._endpoint_url))

    def create_bucket(self, name):
        try:
            self._session.make_bucket(name, self._location)
            return True
        except:
            if self._session.bucket_exists(name):
                return ("Bucket '{}' exists".format(name))
            else:
                return ("Unable to create bucket: '{}'".format(name))

    def remove_bucket(self, name):
        if not self._session.bucket_exists(name):
            return ("Bucket '{}' does not exist".format(name))
        try:
            self._session.remove_bucket(name)
            return True
        except:
            return ("Unable to remove bucket: '{}' Force with 'wipe_bucket'".format(name))

    def wipe_bucket(self, name):
        if not self._session.bucket_exists(name):
            return ("Bucket '{}' does not exist".format(name))
        try:
            objects = self.list_objects(name)
            try:
                for obj in objects:
                    self._session.remove_object(name, obj)
                try:
                    self._session.remove_bucket(name)
                    return True
                except:
                    return ("Unable to remove bucket: '{}'"
                            .format(name))
            except:
                return ("Unable to remove all objects from bucket: '{}'"
                        .format(name))
        except:
            return ("Connection error. Unable to wipe bucket: '{}'"
                    .format(name))


    def list_objects(self, name):
        if not self._session.bucket_exists(name):
            return ("Bucket '{}' does not exist".format(name))
        try:
            objects = [obj.object_name for obj in self._session.list_objects(name, recursive=True)]
            return objects
        except:
            return ("Unable to list objects in bucket: '{}'".format(name))

    def put_object(self, bucketName, obj):
        if not self._session.bucket_exists(bucketName):
            return ("Bucket '{}' does not exist".format(name))
        try:
            self._session.fput_object(bucketName, obj, obj)
            return True
        except:
            return ("Unable to push file '{}' to bucket: '{}'"
                    .format(obj, bucketName))

    def get_object(self, bucketName, obj):
        if not self._session.bucket_exists(bucketName):
            return ("Bucket '{}' does not exist".format(name))
        try:
            file_exists = self._session.stat_object(bucketName, obj)
            if file_exists:
                try:
                    self._session.fget_object(bucketName, obj, obj)
                    return True
                except:
                    return ("Unable to get object '{}' from bucket: '{}'"
                            .format(obj, bucketName))
        except:
            return ("Requested object '{}' not found in bucket: '{}'"
                    .format(obj, bucketName))

    def remove_object(self, bucketName, obj):
        if not self._session.bucket_exists(bucketName):
            return ("Bucket '{}' does not exist".format(name))
        try:
            file_exists = self._session.stat_object(bucketName, obj)
            if file_exists:
                try:
                    self._session.remove_object(bucketName, obj)
                    return True
                except:
                    return ("Unable to remove object '{}' from bucket: '{}'"
                            .format(obj, bucketName))
        except:
            return ("Requested object '{}' not found in bucket: '{}'"
                    .format(obj, bucketName))
