SELECT( SELECT idap 
		FROM vuelos 
		GROUP BY idap
		ORDER BY COUNT(*)) AS most_freq_airport,
		( SELECT ida 
		FROM vuelos 
		GROUP BY ida
		ORDER BY COUNT(*)) AS most_freq_airlines