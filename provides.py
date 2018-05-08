#!/usr/bin/python

from charms.reactive import Endpoint
from charms.reactive import set_flag, clear_flag
from charms.reactive import when, when_not

class GenericDatabase(Endpoint):

    @when(endpoint.{endpoint_name}.changed)
    def _handle_changed(self):
        technology = self.all_joined_units.received['technology']
        if technology:
            flag = '{endpoint_name}.' + technology + '.requested'
            set_flag(self.expand_name(flag))

    def technology(self):
        return self.all_joined_units.received['technology']

    def share_details(self, technology, host, dbname, user, password, port):
        to_publish['technology'] = technology
        to_publish['host'] = host
        to_publish['dbname'] = dbname
        to_publish['user'] = user
        to_publish['password'] = password
        to_publish['port'] = port
