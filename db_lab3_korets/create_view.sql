CREATE VIEW COUNTRY_COUNT AS
select (country), count(country) from wines join province on wines.region = province.region join country on province.province = country.province group by country;

CREATE VIEW WINE_PRICE AS
select wine_id, wine_price
    from wines
    	join province on wines.region = province.region
    	join country on province.province = country.province
    		order by 1;

CREATE VIEW POINTS_COUNT AS
select wine_points, count(wine_points)
    from wines
    	join province on wines.region = province.region
    	join country on province.province = country.province
    		group by wine_points;
