## Postgres local setup
`sudo apt-get install postgresql-client -y`
`sudo apt-get install postgresql-contrib -y`

Follow instructions from the link to create postgres artifacts in ubuntu
`https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04`
* `sudo adduser smartodds`


NOTE: ensure postgres is running after following instructions from above link and create 'smartodds' - role, user and db
    
Start Postgres locally:
`sudo service postgresql start`

* Ensure postgres is running on port 5432
   `sudo netstat -plunt |grep postgres`
* Command `alembic revision -m "create_tennis_data_table" --autogenerate` generated the alembic revision and check alembic/versions creates the new revision.  
  `86eab194ec1f_create_tennis_data_table.py` is created
 * Command 'alembic upgrade head' have created 'tennis_data_id_seq' in the smartodds postgres db that was created above
 
  