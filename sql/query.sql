SELECT 	r.region_id,
		r.number_of_station,
		h.station_name,
		h.region,
        h.price,
        h.tel
FROM h2_station_info h LEFT OUTER JOIN h2_stations_by_region r ON h.region_id = r.region_id
ORDER BY 1 ;