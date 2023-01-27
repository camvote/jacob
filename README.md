# jacob
Just A Cool Online Ballot-Box

## Requirements

- Python 3.11

## Docker for development

You can use docker and avoid any setup. Just run:

```
docker-compose -f dev.yaml build
docker-compose -f dev.yaml up
```

which will spin up the Flask application (http://localhost:5000), a Postgres instance, and an Adminer instance to poke at the database (http://localhost:5001).   
Any changes to the `app/` folder will be immediately reflected inside the Flask container.  
To wipe the database, delete the `jacob_dev_db_data` volume.  
By default, webservers are only visible to localhost.  