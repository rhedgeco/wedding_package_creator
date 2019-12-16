create table users
(
    id            int  not null
        constraint users_pk
            primary key,
    username      text not null,
    password_hash text not null,
    last_access   text not null
);

create unique index users_username_uindex
    on users (username);
