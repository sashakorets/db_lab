select * from country;
create table countrycopy as select * from country;
delete from countrycopy;
select * from countrycopy;

DO $$
DECLARE
    countryName countrycopy.country%TYPE;
    provinceName countrycopy.province%TYPE;


BEGIN
    countryName := 'a';
    provinceName := 'b';
    FOR i IN 1..10
        LOOP
            INSERT INTO countrycopy(province, country)
            VALUES (CONCAT(2*i , provinceName),CONCAT(3*i , countryName));
        END LOOP;
END;
$$