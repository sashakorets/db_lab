--1
--select country, count(country) 
--	from wines 
--		join province on wines.region = province.region 
--		join country on province.province = country.province 
--			group by country;

--2
--select wine_id, wine_price 
--	from wines 
--		join province on wines.region = province.region 
--		join country on province.province = country.province 
--			order by 1;

--3
--select wine_points, count(wine_points) 
--	from wines 
--		join province on wines.region = province.region 
--		join country on province.province = country.province 
--			group by wine_points;
