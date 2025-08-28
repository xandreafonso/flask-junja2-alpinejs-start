CREATE TABLE  sm_posts
(
    code text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    copy text COLLATE pg_catalog."default",
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status text COLLATE pg_catalog."default" NOT NULL DEFAULT 'draft'::text,
    scheduled_at timestamp with time zone,
    briefing text COLLATE pg_catalog."default",
    CONSTRAINT posts_pkey PRIMARY KEY (code)
);


CREATE TABLE sm_posts_media
(
    code text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    key text COLLATE pg_catalog."default" NOT NULL,
    posts_code text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    details text COLLATE pg_catalog."default",
    CONSTRAINT sm_posts_media_pkey PRIMARY KEY (code),
    CONSTRAINT fk_sm_posts_key FOREIGN KEY (posts_code)
        REFERENCES public.sm_posts (code) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE users (
    code VARCHAR(36) PRIMARY KEY DEFAULT gen_random_uuid()::text,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN NOT NULL DEFAULT true,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);