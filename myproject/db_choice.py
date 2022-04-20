import random

from django.conf import settings

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """


        print('inside : db_for_read')
        print('settings.DATABASENAME : ',settings.DATABASENAME)
        return settings.DATABASENAME

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        print('inside : db_for_write ')
        return settings.DATABASENAME

    def allow_relation(self, obj1, obj2, **hints):
        print('inside : allow_relation ')
        return settings.DATABASENAME

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        print('inside : allow_migrate ')
        return settings.DATABASENAME