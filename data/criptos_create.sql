CREATE TABLE "criptos" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"hora"	TEXT NOT NULL,
	"Moneda_from"	TEXT NOT NULL,
	"Cantidad_from"	REAL NOT NULL,
	"Moneda_to"	TEXT NOT NULL,
	"cantidad_to"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

