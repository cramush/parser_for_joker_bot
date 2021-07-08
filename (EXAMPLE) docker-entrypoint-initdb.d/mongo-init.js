db = db.getSiblingDB('jokes_db');
db.createUser(
    {
        user: 'username',
        pwd:  'password',
        roles: [{role: 'dbOwner', db: 'jokes_db'}],
    }
);