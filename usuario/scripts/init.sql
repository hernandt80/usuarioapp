-- Table: public."USER"

-- DROP TABLE public."USER";

CREATE TABLE public."USER"
(
    username text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    id bigint NOT NULL DEFAULT nextval('"USER_id_seq"'::regclass)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public."USER"
    OWNER to postgres;
COMMENT ON TABLE public."USER"
    IS 'Tabla para almacenar usuarios';