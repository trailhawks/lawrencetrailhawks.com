"""
Based on:
- https://chris-lamb.co.uk/posts/appending-request-url-sql-statements-django
- https://github.com/dobarkod/django-queryinspect/blob/master/qinspect/middleware.py

"""
import sys

from django.db.backends import BaseDatabaseWrapper
from django.db.backends.util import CursorDebugWrapper
from django.http import HttpRequest


class RequestUrlCursor(CursorDebugWrapper):

    def execute(self, sql, *args):
        f = sys._getframe()
        while f:
            request = f.f_locals.get('request')
            if isinstance(request, HttpRequest):
                sql += ' -- %s' % repr(request.path)[2:-1].replace('%', '%%')
                break
            f = f.f_back

        return self.cursor.execute(sql, *args)


class QueryRequestUrlMiddleware(object):

    @classmethod
    def patch_cursor(cls):
        fn = BaseDatabaseWrapper.cursor
        BaseDatabaseWrapper.cursor = lambda self: RequestUrlCursor(fn(self), self)

    '''
    def process_request(self, request):
        if not isinstance(CursorDebugWrapper, URLCursor):
            self.old_cursor = CursorDebugWrapper
            CursorDebugWrapper = URLCursor
        #URLCursor.logger = self.logger

    def process_response(self, request, response):
        if isinstance(CursorDebugWrapper, URLCursor):
            CursorDebugWrapper = self.old_cursor
        return response
    '''

QueryRequestUrlMiddleware.patch_cursor()
