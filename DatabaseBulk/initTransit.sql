DROP TABLE IF EXISTS transit CASCADE;
DROP FOREIGN TABLE IF EXISTS transit_remote_1 CASCADE;
DROP FOREIGN TABLE IF EXISTS transit_remote_2 CASCADE;

CREATE EXTENSION IF NOT EXISTS dblink;
CREATE EXTENSION IF NOT EXISTS postgres_fdw;

SELECT dblink_exec('host=citus_DBMS1 user=postgres password=postgres dbname=postgres'
$cmd$
    CREATE TABLE IF NOT EXISTS transit (
        id SERIAL PRIMARY KEY,
        id_from SERIAL,
        id_to SERIAL,
        origin VARCHAR(255),
        destination VARCHAR(255),
        transit_time FLOAT,
        capacity_at_risk FLOAT,
        relative_capacity_at_risk FLOAT
    );
$cmd$);