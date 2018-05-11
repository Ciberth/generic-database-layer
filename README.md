# generic-database-layer

This is the repository for the 'generic-database' interface. 


## Overview of interesting/used links & documentation

(TODO updating LINKS)

- [Consumer-app](https://github.com/Ciberth/consumer-app)
- [Generic-database charm](https://github.com/Ciberth/generic-database) 
- [Generic-database interface](https://github.com/Ciberth/generic-database-layer) (this repository)

## Usage

### Requires 

Example usage to request a specific databasetechnology:

```python
@when('endpoint.generic-database.joined')
def request_db():
    endpoint = endpoint_from_flag('endpoint.generic-database.joined')
    endpoint.request('postgresql')
    status_set('maintenance', 'Requesting postgresql')
```

When the generic database is done requesting and obtaining the connection details a flag will be set according to the requested technology (in this case 'postgresql')

```python
@when('endpoint.generic-database.postgresql.available')
def pgsql_render_config():
    pgsql = endpoint_from_flag('endpoint.generic-database.postgresql.available')
    
    render('pgsql-config.j2', '/var/www/consumer-app/pgsql-config.php', {
        'gdb_host' : pgsql.host(),
        'gdb_port' : pgsql.port(),
        'gdb_dbname' : pgsql.databasename(),
        'gdb_user' : pgsql.user(),
        'gdb_password' : pgsql.password(),
    })
    
    status_set('maintenance', 'Rendering config file')
    set_flag('endpoint.generic-database.connected')
    set_flag('restart-app')
```

Currently supported technologies:
- Postgresql

Todo:
- Mysql
- Mongodb