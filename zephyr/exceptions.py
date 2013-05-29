from django.core.exceptions import PermissionDenied

class RateLimited(PermissionDenied):
    def __init__(self, msg=""):
        super(RateLimited, self).__init__(msg)
