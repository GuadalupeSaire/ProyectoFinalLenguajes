-- Base de datos: Smart Fit
-- Motor: PostgreSQL
-- Primero crea la base (ejecútalo por separado) y conéctate a ella:
-- CREATE DATABASE smartfit;

CREATE TABLE cliente (
    id          BIGSERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    genero      VARCHAR(20)  NOT NULL,
    dni         VARCHAR(8)   NOT NULL UNIQUE,
    email       VARCHAR(254) NOT NULL,
    telefono    VARCHAR(15)  NOT NULL
);

CREATE TABLE entrenador (
    id                  BIGSERIAL PRIMARY KEY,
    nombre              VARCHAR(100) NOT NULL,
    apellido            VARCHAR(100) NOT NULL,
    genero              VARCHAR(20)  NOT NULL,
    dni                 VARCHAR(8)   NOT NULL UNIQUE,
    especializacion     VARCHAR(100) NOT NULL,
    anios_experiencia   INTEGER      NOT NULL CHECK (anios_experiencia >= 0)
);

CREATE TABLE administrador (
    id          BIGSERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    genero      VARCHAR(20)  NOT NULL,
    dni         VARCHAR(8)   NOT NULL UNIQUE,
    area        VARCHAR(100) NOT NULL,
    salario     NUMERIC(10,2) NOT NULL
);

CREATE TABLE recepcionista (
    id          BIGSERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    apellido    VARCHAR(100) NOT NULL,
    genero      VARCHAR(20)  NOT NULL,
    dni         VARCHAR(8)   NOT NULL UNIQUE,
    horario     VARCHAR(100) NOT NULL,
    tareas      TEXT         NOT NULL
);

CREATE TABLE membresia (
    id              BIGSERIAL PRIMARY KEY,
    cliente_id      BIGINT       NOT NULL REFERENCES cliente (id) ON DELETE CASCADE,
    tipo            VARCHAR(50)  NOT NULL,
    fecha_inicio    DATE         NOT NULL,
    fecha_final     DATE         NOT NULL,
    precio          NUMERIC(8,2) NOT NULL,
    descripcion     TEXT,
    CHECK (fecha_final >= fecha_inicio)
);

CREATE TABLE entrenamiento (
    id          BIGSERIAL PRIMARY KEY,
    cliente_id  BIGINT       NOT NULL REFERENCES cliente (id) ON DELETE CASCADE,
    tipo        VARCHAR(50)  NOT NULL,
    duracion    VARCHAR(50)  NOT NULL,
    frecuencia  INTEGER      NOT NULL CHECK (frecuencia >= 0),
    objetivo    VARCHAR(100) NOT NULL,
    rutina      TEXT         NOT NULL
);

CREATE INDEX idx_membresia_cliente ON membresia (cliente_id);
CREATE INDEX idx_entrenamiento_cliente ON entrenamiento (cliente_id);