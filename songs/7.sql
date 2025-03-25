SELECT AVG(energy) AS Avg_Energy_Drake_Songs FROM songs JOIN artists ON songs.artist_id = (SELECT id FROM artists WHERE name = 'Drake');
