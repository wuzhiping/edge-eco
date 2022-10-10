module.exports = ({ env }) => ({
    connection: {
        client: 'postgres',
        connection: {
            host: env('DATABASE_HOST', '10.17.1.145'),
            port: env.int('DATABASE_PORT', 6666),
            database: env('DATABASE_NAME', 'strapi'),
            user: env('DATABASE_USERNAME', 'strapi'),
            password: env('DATABASE_PASSWORD', 'strapi'),
            schema: env('DATABASE_SCHEMA', 'public'), // Not required
            ssl: false,
        },
        debug: false,
    },
});