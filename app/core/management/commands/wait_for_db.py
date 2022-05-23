from lib2to3.pytree import Base
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database"""
    
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database to load....')
        db = False
        while db is False:
            try:
                self.check(databases=['default'])
                db = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database is unavailable. Please wait one second....')
        
        self.stdout.write(self.style.SUCCESS('Database is now ready!'))