CREATE OR REPLACE PROCEDURE filter_wines_by_region(region_name varchar(150))
LANGUAGE 'plpgsql'
AS $$
BEGIN
	DROP TABLE IF EXISTS filtered_wines;
	CREATE TABLE filtered_wines
	AS
	(
	    select wine_id, wine_name from wines
	    where  region = region_name
	);
END;
$$;

CALL filter_wines_by_region('Toro');

select * from filtered_wines