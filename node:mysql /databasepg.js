const {Client} = require('pg')

const client = new Client
({
    host: "localhost"
    user: "postgres"
    port: 5432,
    password: "1234"
    database: "selling_birmingham_data"
})

client.connect () ;

client.query('SELECT * FROM Public.selling_birmingham_data')

client.end;
