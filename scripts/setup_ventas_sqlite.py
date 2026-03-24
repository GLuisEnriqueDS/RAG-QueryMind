import sqlite3

# Crear base de datos
conn = sqlite3.connect("ventas.db")
cur = conn.cursor()

# Tabla Agencia
cur.execute("""
CREATE TABLE Agencia (
    agenciaID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT,
    telefono TEXT,
    email TEXT
)
""")

# Tabla RepresentanteComercial
cur.execute("""
CREATE TABLE RepresentanteComercial (
    representanteID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT,
    fecha_contratacion TEXT
)
""")

# Tabla Agente (Vendedor)
cur.execute("""
CREATE TABLE Agente (
    agenteID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT,
    fecha_contratacion TEXT,
    agenciaID INTEGER,
    representanteID INTEGER,
    FOREIGN KEY (agenciaID) REFERENCES Agencia(agenciaID),
    FOREIGN KEY (representanteID) REFERENCES RepresentanteComercial(representanteID)
)
""")

# Tabla Cliente
cur.execute("""
CREATE TABLE Cliente (
    clienteID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT,
    direccion TEXT,
    fecha_registro TEXT
)
""")

# Tabla Producto
cur.execute("""
CREATE TABLE Producto (
    productoID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL NOT NULL,
    categoria TEXT,
    stock INTEGER DEFAULT 0
)
""")

# Tabla Venta
cur.execute("""
CREATE TABLE Venta (
    ventaID INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    monto_total REAL NOT NULL,
    agenteID INTEGER NOT NULL,
    clienteID INTEGER NOT NULL,
    FOREIGN KEY (agenteID) REFERENCES Agente(agenteID),
    FOREIGN KEY (clienteID) REFERENCES Cliente(clienteID)
)
""")

# Tabla DetalleVenta (para productos en cada venta)
cur.execute("""
CREATE TABLE DetalleVenta (
    detalleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ventaID INTEGER NOT NULL,
    productoID INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (ventaID) REFERENCES Venta(ventaID),
    FOREIGN KEY (productoID) REFERENCES Producto(productoID)
)
""")

# Insertar datos de ejemplo - Agencias
cur.executemany("INSERT INTO Agencia (nombre, direccion, telefono, email) VALUES (?, ?, ?, ?)", [
    ("Agencia Central", "Av. Principal 123", "555-0101", "central@ventas.com"),
    ("Agencia Norte", "Calle Norte 456", "555-0202", "norte@ventas.com"),
    ("Agencia Sur", "Av. del Sur 789", "555-0303", "sur@ventas.com"),
    ("Agencia Este", "Boulevard Este 234", "555-0404", "este@ventas.com"),
    ("Agencia Oeste", "Plaza Oeste 567", "555-0505", "oeste@ventas.com")
])

# Insertar Representantes Comerciales
cur.executemany("INSERT INTO RepresentanteComercial (nombre, email, telefono, fecha_contratacion) VALUES (?, ?, ?, ?)", [
    ("Carlos Rodríguez", "carlos.rodriguez@empresa.com", "555-1001", "2020-01-15"),
    ("María González", "maria.gonzalez@empresa.com", "555-1002", "2019-03-20"),
    ("Juan Martínez", "juan.martinez@empresa.com", "555-1003", "2021-06-10"),
    ("Ana López", "ana.lopez@empresa.com", "555-1004", "2018-11-05"),
    ("Pedro Sánchez", "pedro.sanchez@empresa.com", "555-1005", "2022-02-28")
])

# Insertar Agentes (Vendedores)
cur.executemany("INSERT INTO Agente (nombre, email, telefono, fecha_contratacion, agenciaID, representanteID) VALUES (?, ?, ?, ?, ?, ?)", [
    ("Luis Pérez", "luis.perez@agencia.com", "555-2001", "2021-05-10", 1, 1),
    ("Laura Torres", "laura.torres@agencia.com", "555-2002", "2020-08-15", 1, 1),
    ("Roberto Díaz", "roberto.diaz@agencia.com", "555-2003", "2019-11-20", 2, 2),
    ("Sofia Castro", "sofia.castro@agencia.com", "555-2004", "2022-01-05", 2, 2),
    ("Diego Ramos", "diego.ramos@agencia.com", "555-2005", "2021-03-12", 3, 3),
    ("Carmen Flores", "carmen.flores@agencia.com", "555-2006", "2020-07-18", 3, 3),
    ("Javier Soto", "javier.soto@agencia.com", "555-2007", "2019-09-25", 4, 4),
    ("Patricia Vega", "patricia.vega@agencia.com", "555-2008", "2022-04-30", 4, 4),
    ("Fernando Ruiz", "fernando.ruiz@agencia.com", "555-2009", "2021-10-08", 5, 5),
    ("Gabriela Mora", "gabriela.mora@agencia.com", "555-2010", "2020-12-14", 5, 5)
])

# Insertar Clientes
cur.executemany("INSERT INTO Cliente (nombre, email, telefono, direccion, fecha_registro) VALUES (?, ?, ?, ?, ?)", [
    ("Empresa ABC", "contacto@abc.com", "555-3001", "Av. Comercial 100", "2022-01-10"),
    ("Distribuidora XYZ", "ventas@xyz.com", "555-3002", "Calle Industria 200", "2022-02-15"),
    ("Tech Solutions", "info@techsol.com", "555-3003", "Parque Tecnológico 300", "2022-03-20"),
    ("Comercial del Sur", "pedidos@comercialsur.com", "555-3004", "Ruta 5 km 400", "2022-04-25"),
    ("Importaciones Global", "import@global.com", "555-3005", "Zona Franca 500", "2022-05-30"),
    ("Minoristas Unidos", "compras@minoristas.com", "555-3006", "Galerías 600", "2022-06-05"),
    ("Corporación Norte", "corporacion@norte.com", "555-3007", "Av. del Norte 700", "2022-07-10"),
    ("Servicios Integrales", "info@servintegrales.com", "555-3008", "Edificio Central 800", "2022-08-15"),
    ("Distribuciones Este", "ventas@diste.com", "555-3009", "Polígono Industrial 900", "2022-09-20"),
    ("Comercial Oeste", "contacto@coeste.com", "555-3010", "Plaza Mayor 1000", "2022-10-25")
])

# Insertar Productos
cur.executemany("INSERT INTO Producto (nombre, descripcion, precio, categoria, stock) VALUES (?, ?, ?, ?, ?)", [
    ("Laptop Pro", "Laptop de alta gama para profesionales", 1200.00, "Electrónica", 50),
    ("Smartphone X", "Teléfono inteligente última generación", 800.00, "Electrónica", 100),
    ("Tablet Plus", "Tablet con pantalla de alta resolución", 450.00, "Electrónica", 75),
    ("Monitor 4K", "Monitor Ultra HD 27 pulgadas", 350.00, "Electrónica", 40),
    ("Teclado Mecánico", "Teclado gaming RGB", 80.00, "Accesorios", 150),
    ("Mouse Inalámbrico", "Mouse ergonómico Bluetooth", 45.00, "Accesorios", 200),
    ("Impresora Laser", "Impresora multifunción", 250.00, "Oficina", 30),
    ("Escritorio Ejecutivo", "Escritorio de madera premium", 400.00, "Muebles", 15),
    ("Silla Ergonómica", "Silla de oficina ajustable", 300.00, "Muebles", 25),
    ("Proyector HD", "Proyector para presentaciones", 500.00, "Electrónica", 20)
])

# Insertar Ventas
cur.executemany("INSERT INTO Venta (fecha, monto_total, agenteID, clienteID) VALUES (?, ?, ?, ?)", [
    ("2023-01-15", 2000.00, 1, 1),
    ("2023-01-20", 1250.00, 2, 2),
    ("2023-02-05", 3600.00, 3, 3),
    ("2023-02-18", 800.00, 4, 4),
    ("2023-03-10", 1750.00, 5, 5),
    ("2023-03-22", 2150.00, 6, 6),
    ("2023-04-05", 950.00, 7, 7),
    ("2023-04-19", 3050.00, 8, 8),
    ("2023-05-03", 1400.00, 9, 9),
    ("2023-05-17", 2800.00, 10, 10),
    ("2023-06-01", 1650.00, 1, 2),
    ("2023-06-15", 3200.00, 2, 3),
    ("2023-07-05", 1100.00, 3, 4),
    ("2023-07-20", 2400.00, 4, 5),
    ("2023-08-10", 1850.00, 5, 6)
])

# Insertar Detalles de Venta
cur.executemany("INSERT INTO DetalleVenta (ventaID, productoID, cantidad, precio_unitario, subtotal) VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 1, 1200.00, 1200.00),
    (1, 2, 1, 800.00, 800.00),
    (2, 3, 2, 450.00, 900.00),
    (2, 5, 1, 80.00, 80.00),
    (2, 6, 1, 45.00, 45.00),
    (3, 4, 3, 350.00, 1050.00),
    (3, 10, 2, 500.00, 1000.00),
    (4, 2, 1, 800.00, 800.00),
    (5, 7, 2, 250.00, 500.00),
    (5, 8, 1, 400.00, 400.00),
    (6, 9, 3, 300.00, 900.00),
    (6, 5, 2, 80.00, 160.00),
    (7, 6, 5, 45.00, 225.00),
    (8, 1, 2, 1200.00, 2400.00),
    (9, 3, 1, 450.00, 450.00),
    (10, 4, 2, 350.00, 700.00),
    (11, 2, 1, 800.00, 800.00),
    (12, 10, 1, 500.00, 500.00)
])

# Guardar y cerrar
conn.commit()
conn.close()

print("Base de datos 'ventas.db' creada exitosamente con todas las tablas y datos de ejemplo.")