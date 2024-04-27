DO $$
BEGIN
CREATE USER paul_admin WITH SUPERUSER PASSWORD '12345';
EXCEPTION WHEN duplicate_object THEN RAISE NOTICE '%, skipping', SQLERRM USING ERRCODE = SQLSTATE;
END
$$;
SELECT 'CREATE DATABASE candelae_main_docker'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'candelae_main_docker')\gexec

