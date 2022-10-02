SELECT array_to_json(array_agg(row_to_json(dropped_data_alias))) 
   FROM (SELECT * FROM dropped_data) dropped_data_alias