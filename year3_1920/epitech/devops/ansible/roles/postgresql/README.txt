How to debug this role:
- Check that connection can be made between postgres client and postgres server
    - cat /var/log/postgresql/postgresql-12-main.log
    - postgres.conf and pg_hba.conf files
- Restart client and server daemons to ensure they don't time out after not connecting
- Connect via a client
    - psql --host=HOST --username=USER --password
- Insert into the votes table (ensure that you have permissions on: db, table, schema)
    - INSERT INTO votes(id, vote) VALUES (y, x);
        where y is a unique voter id, and x is one of 'a', 'b', 'c', or 'd' (the option you are voting for).
- Check current table
    - SELECT * FROM votes;
- Check how result queries the table
    - SELECT vote, COUNT(id) AS count FROM votes GROUP BY vote;