CREATE OR REPLACE FUNCTION maxPriceInRegion(region_name varchar(50)) RETURNS int AS
$$
    DECLARE
        price integer;
    BEGIN
        SELECT max(wine_price) INTO price
        FROM wines
        WHERE region = region_name;
        RETURN price;
    END;
$$ LANGUAGE 'plpgsql';

SELECT maxPriceInRegion('Toro');