CREATE OR REPLACE FUNCTION replace_wine_name()
RETURNS trigger AS
$$
	BEGIN
	    IF NEW.wine_name is null THEN
            NEW.wine_name = CONCAT('name_№',NEW.wine_id);
        END IF;
	        RETURN NEW;
	    END;
$$ LANGUAGE 'plpgsql';
DROP TRIGGER IF EXISTS validate_wine_name on wines;

CREATE TRIGGER validate_wine_name
BEFORE UPDATE OR INSERT ON wines
FOR EACH ROW
EXECUTE FUNCTION replace_wine_name();

SELECT * FROM wines where wine_name = 'name_№11';
INSERT INTO wines(wine_id, wine_name, wine_points, wine_price, region)
	VALUES(11,null,1,2, 'Napa Valley');
SELECT * FROM wines where wine_name = 'name_№11';
