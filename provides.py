#!/usr/bin/python

from charms.reactive import Endpoint
from charms.reactive import set_flag, clear_flag
from charms.reactive import when, when_not

class GenericDatabase(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def _handle_joined(self):
        technology = self.all_joined_units.received['technology']
        if technology:
            flag = 'endpoint.{endpoint_name}.' + technology + '.requested'
            set_flag(self.expand_name(flag))

    #@when('endpoint.{endpoint_name}.postgresql.available')
    #def _handle_postgresql_availabl(self):
    #    pgsql_details = endpoint_from_flag('endpoint.{endpoint_name}.postgresql.available')
        
    def technology(self):
        return self.all_joined_units.received['technology']

    def share_details(self, technology, host, dbname, user, password, port):
        details = {}
        details['technology'] = technology
        details['host'] = host
        details['dbname'] = dbname
        details['user'] = user
        details['password'] = password
        details['port'] = port

        for relation in self.relations:
            relation.to_publish['details'] = details
            relation.to_publish['technology'] = technology
            relation.to_publish['host'] = host
            relation.to_publish['dbname'] = dbname
            relation.to_publish['user'] = user
            relation.to_publish['password'] = password
            relation.to_publish['port'] = port
