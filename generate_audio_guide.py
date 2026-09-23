import asyncio
import os
import sys
import edge_tts

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

VOICE = "es-ES-AlvaroNeural"  # Professional, articulate, clear academic tone

AUDIO_MODULES = [
    {
        "filename": "01_Diseno_Conceptual_DER_y_Claves.mp3",
        "title": "Tema 1: Diseño Conceptual, Diagrama Entidad-Relación y Claves",
        "text": """
Bienvenidos a este repaso para el parcial de Administración y Gestión de Bases de Datos. En este primer módulo abordaremos el Diseño Conceptual, el Diagrama Entidad-Relación y el uso de Claves.

Comencemos por el principio: ¿Qué es el DER, o Diagrama Entidad-Relación?
El DER es una herramienta visual fundamental utilizada en la primera etapa de diseño de cualquier base de datos. Su propósito principal es modelar la información del mundo real, identificando con precisión qué datos se deben almacenar y cómo interactúan entre sí, mucho antes de implementar tablas físicas o escribir código SQL.

En este modelo existen dos componentes básicos: las entidades y los atributos.

Primero, las Entidades. Representan objetos, sujetos o conceptos del mundo real sobre los cuales la organización necesita almacenar información. Por ejemplo: Socios, Inscripciones o Actividades. En un DER, las entidades suelen representarse gráficamente mediante rectángulos.

Segundo, los Atributos. Son las propiedades o características específicas que describen a una entidad. Por ejemplo, para la entidad Socio, sus atributos pueden ser: nombre, apellido, teléfono, documento y dirección.

Ahora pasemos a un concepto clave que siempre es pregunta de examen: Las Claves, o Keys.

Existen dos tipos fundamentales:
Número uno: La Clave Primaria, o Primary Key, identificada como PK.
Es un atributo, o combinación de atributos, cuyo valor es absolutamente único para cada registro dentro de la tabla. Regla de oro para el parcial: la clave primaria nunca puede ser nula ni estar vacía. Su función es permitir la identificación unívoca e inequívoca de cada fila.

Número dos: La Clave Foránea o Clave Externa, identificada como FK.
Es un atributo presente en una tabla que hace referencia directa a la Clave Primaria de otra tabla. Su función fundamental es establecer el vínculo o relación lógica entre ambas tablas, garantizando la integridad referencial.

Con esto cerramos el tema de diseño conceptual y claves. Continuemos con el siguiente módulo sobre relaciones y cardinalidades.
""".strip()
    },
    {
        "filename": "02_Relaciones_y_Cardinalidades.mp3",
        "title": "Tema 2: Relaciones, Cardinalidades y Resolución de Muchos a Muchos",
        "text": """
En este segundo tema analizaremos las Relaciones y Cardinalidades, con especial atención a un problema clásico de diseño en el modelo relacional.

Las relaciones describen la forma en que las entidades interactúan entre sí. Por su parte, la cardinalidad define la cantidad de instancias de una entidad que pueden asociarse con instancias de otra.

Existen tres tipos principales de cardinalidad:

Primero: Relación Uno a Uno, o 1 a 1.
En este caso, un registro de la Entidad A se relaciona con un único registro de la Entidad B, y viceversa.

Segundo: Relación Uno a Muchos, o 1 a N.
Aquí, un registro de la Entidad A puede estar vinculado con múltiples registros de la Entidad B, pero cada registro de B solo puede relacionarse con un único registro de A.
Por ejemplo: Un socio puede realizar muchas inscripciones en el club a lo largo del tiempo, pero cada inscripción individual pertenece a un solo socio.

Tercero: Relación Muchos a Muchos, o N a M.
Muchísima atención con esto para el parcial:
En el modelo relacional, los motores de bases de datos no soportan de manera directa las relaciones de Muchos a Muchos.

¿Cómo se resuelve esto en la práctica?
Se debe romper la relación Muchos a Muchos mediante la creación de una tabla intermedia, también llamada entidad asociativa.
Esta tabla intermedia albergará como claves foráneas a las claves primarias de ambas tablas originales. De esta manera, la relación Muchos a Muchos se transforma limpiamente en dos relaciones de Uno a Muchos.

Recordá siempre este mecanismo, ya que es el patrón estándar de normalización y diseño en bases de datos relacionales.
""".strip()
    },
    {
        "filename": "03_Proceso_de_Normalizacion_1FN_2FN_3FN.mp3",
        "title": "Tema 3: Proceso de Normalización y Formas Normales 1FN, 2FN y 3FN",
        "text": """
Tema tres: El Proceso de Normalización. Este es uno de los temas teóricos y prácticos más importantes de la materia.

¿Qué es la normalización?
Es un proceso sistemático para estructurar y organizar los datos en tablas. Sus objetivos principales son:
Primero, evitar la redundancia y duplicación de información.
Segundo, proteger la integridad de los datos.
Y tercero, eliminar anomalías al momento de insertar, modificar o eliminar registros.

Veamos en detalle las tres primeras formas normales:

Primera Forma Normal, o 1FN: El principio de Atomicidad.
Exige que cada celda de la tabla contenga un valor único e indivisible, es decir, atómico.
Esto significa dos reglas prácticas:
Regla A: Una columna no se puede subdividir. Por ejemplo, está prohibido tener varios números de teléfono en una sola celda separados por comas.
Regla B: No deben existir grupos repetidos de columnas, como por ejemplo teléfono 1, teléfono 2 y teléfono 3.

Segunda Forma Normal, o 2FN: Eliminación de Dependencias Parciales.
Para aplicar la Segunda Forma Normal, la tabla debe cumplir dos condiciones:
Primero, ya debe encontrarse en Primera Forma Normal.
Segundo, se deben eliminar todas las dependencias funcionales parciales.
¿Cuándo ocurre una dependencia parcial? Ocurre cuando la tabla tiene una Clave Primaria compuesta, formada por dos o más atributos, por ejemplo: id_pedido más id_producto. Si un atributo no clave, como nombre_producto, depende únicamente de id_producto y no de toda la clave compuesta, estamos ante una dependencia parcial.
¿Cómo se soluciona? Separando ese atributo en una tabla propia con su clave correspondiente.

Tercera Forma Normal, o 3FN: Eliminación de Dependencias Transitivas.
Nuevamente, requiere dos condiciones:
Primero, que la tabla ya esté en Segunda Forma Normal.
Segundo, que no existan dependencias transitivas.
Esto significa que ningún atributo no clave puede depender de otro atributo no clave. Todos los atributos descriptivos deben depender única, directa y exclusivamente de la Clave Primaria.
Como regla mnemotécnica para el parcial: Cada dato debe depender de la clave, de toda la clave, y de nada más que de la clave.
""".strip()
    },
    {
        "filename": "04_Introduccion_a_SQL_DDL_y_DML.mp3",
        "title": "Tema 4: Introducción a SQL y Diferenciación DDL vs DML",
        "text": """
Tema cuatro: Introducción al lenguaje SQL.

SQL, cuyas siglas significan Structured Query Language o Lenguaje de Consulta Estructurado, es el estándar mundial para interactuar, administrar y consultar bases de datos relacionales.

En los exámenes se suele evaluar la distinción precisa entre las distintas familias de comandos. Las dos principales son DDL y DML.

Primero: DDL, o Data Definition Language, que traduce Lenguaje de Definición de Datos.
Los comandos DDL se utilizan para definir, crear o alterar las estructuras de almacenamiento, es decir, los esquemas, tablas, vistas e índices. No modifican las filas individuales, sino el contenedor.
Los comandos esenciales de DDL son:
CREATE: para crear nuevas bases de datos o nuevas tablas.
ALTER: para modificar la estructura existente de una tabla, como agregar o quitar una columna.
DROP: para eliminar por completo una tabla o base de datos junto con su definición.
Y TRUNCATE: para vaciar rápidamente todos los registros de una tabla, conservando intacta su estructura.

Segundo: DML, o Data Manipulation Language, que traduce Lenguaje de Manipulación de Datos.
Los comandos DML operan sobre los datos propiamente dichos, es decir, sobre el contenido dentro de las tablas existentes.
Los comandos fundamentales de DML son:
SELECT: para consultar, filtrar y recuperar datos.
INSERT: para agregar nuevos registros o filas.
UPDATE: para modificar o actualizar datos ya existentes.
Y DELETE: para eliminar una o más filas específicas que cumplan cierta condición.

Tener muy en claro esta diferencia entre estructura, que es DDL, y contenido, que es DML, es garantía de sumar puntos en el parcial.
""".strip()
    },
    {
        "filename": "05_Tipos_de_Datos_y_Sintaxis_CREATE_TABLE.mp3",
        "title": "Tema 5: Tipos de Datos en SQL, Sentencia CREATE TABLE y Tips de Examen",
        "text": """
En este quinto módulo revisaremos los Tipos de Datos más comunes en SQL, la sintaxis de creación de tablas y una estrategia práctica infalible para el parcial.

Al definir una tabla con DDL, a cada columna se le debe asignar un tipo de dato según la naturaleza de la información:

Primero: VARCHAR de n. Almacena cadenas de texto de longitud variable, donde n representa el número máximo de caracteres permitidos. Es ideal para nombres, apellidos, correos electrónicos o domicilios.
Segundo: DATE. Es el tipo de dato nativo para almacenar fechas compuestas por año, mes y día. Está optimizado para filtros temporales y comparaciones cronológicas sin horas.
Tercero: DECIMAL de p coma s. Se utiliza para valores numéricos exactos con decimales, donde p es la cantidad total de dígitos y s es la cantidad de decimales. Se justifica plenamente en valores monetarios: precios, salarios y facturación.
Cuarto: INT. Números enteros sin decimales. Ocupa poco espacio de memoria y ofrece el máximo rendimiento en cálculos y claves primarias.
Quinto: BOOLEAN o BIT. Representa estados binarios: verdadero o falso, uno o cero. Es óptimo para banderas de estado, como por ejemplo: si un socio está activo o si adeuda cuotas.

Veamos ahora la sintaxis práctica de la sentencia CREATE TABLE.
Para crear una tabla de alumnos, la sintaxis en SQL es:
CREATE TABLE alumnos, abrimos paréntesis:
Primera columna: id_alumno, tipo INT, restricción PRIMARY KEY, coma.
Segunda columna: nombre, tipo VARCHAR de cincuenta caracteres, coma.
Tercera columna: apellido, tipo VARCHAR de cincuenta caracteres, coma.
Cuarta columna: fecha_nacimiento, tipo DATE.
Cerramos el paréntesis y finalizamos con punto y coma.

Para finalizar, el Tip de Oro para el parcial:
Cuando te den el enunciado de un caso práctico, lee muy atentamente y aplica la siguiente técnica lingüística:
Uno: Identifica todos los sustantivos del texto. Esos sustantivos serán casi con certeza tus entidades y tus futuras tablas.
Dos: Identifica los adjetivos y datos específicos que los describen. Ellos se transformarán en los atributos y columnas.
Tres: Identifica las acciones y verbos conectores, tales como realiza, gestiona, pertenece o se inscribe. Esos verbos definirán las relaciones, cardinalidades y claves foráneas que debes vincular.

Muchos éxitos en el examen de Base de Datos.
""".strip()
    },
    {
        "filename": "00_Resumen_Completo_Repaso_Total_Parcial.mp3",
        "title": "Repaso Completo: Todo el Parcial en un Solo Audio",
        "text": """
Resumen integral para el primer parcial de Administración y Gestión de Bases de Datos.

Módulo 1: Diseño Conceptual, Diagrama Entidad-Relación y Claves.
El Diagrama Entidad-Relación o DER es la herramienta gráfica empleada en la etapa conceptual para modelar la realidad del negocio antes de pasar a la implementación física.
Sus componentes esenciales son:
Entidades: Representan objetos o conceptos del mundo real sobre los que se guardan datos, como Socios o Inscripciones.
Atributos: Son las propiedades que describen a la entidad, como nombre, apellido y teléfono.
En cuanto a las Claves:
La Clave Primaria o Primary Key es el identificador unívoco de cada registro. Nunca puede ser nula ni repetirse.
La Clave Foránea o Foreign Key es un campo que apunta a la Clave Primaria de otra tabla, vinculándolas y asegurando la integridad referencial.

Módulo 2: Relaciones y Cardinalidades.
La cardinalidad indica cuántas instancias de una entidad se vinculan con instancias de otra:
Uno a Uno: Un registro se relaciona únicamente con uno del otro lado.
Uno a Muchos: Un registro se relaciona con varios, pero cada uno de esos se relaciona solo con el primero. Por ejemplo: un socio tiene muchas inscripciones, pero cada inscripción pertenece a un único socio.
Y atención con Muchos a Muchos: En el modelo relacional no se soportan relaciones de Muchos a Muchos directas. La solución obligatoria es romperla creando una tabla intermedia asociativa, que contenga como claves foráneas las claves primarias de ambas tablas, transformando el problema en dos relaciones Uno a Muchos.

Módulo 3: Normalización de Bases de Datos.
La normalización organiza los datos para eliminar redundancias y prevenir anomalías:
Primera Forma Normal (1FN): Exige atomicidad. Cada celda debe tener un valor indivisible, sin listas separadas por comas ni grupos de columnas repetidas.
Segunda Forma Normal (2FN): Debe estar en 1FN y eliminar dependencias parciales. Si hay clave primaria compuesta, ningún atributo debe depender de una sola parte de la clave.
Tercera Forma Normal (3FN): Debe estar en 2FN y eliminar dependencias transitivas. Ningún atributo no clave debe depender de otro atributo no clave. Todo dato debe depender directa y únicamente de la clave primaria.

Módulo 4: Lenguaje SQL, DDL y DML.
SQL es el estándar para bases de datos relacionales.
DDL, o Lenguaje de Definición de Datos, define las estructuras. Sus comandos son: CREATE para crear, ALTER para modificar estructuras, DROP para eliminar objetos completos, y TRUNCATE para vaciar el contenido de una tabla conservando su estructura.
DML, o Lenguaje de Manipulación de Datos, gestiona los datos en sí. Sus comandos son: SELECT para consultar, INSERT para agregar filas, UPDATE para modificar datos existentes, y DELETE para borrar filas.

Módulo 5: Tipos de Datos y Consejos de Examen.
Tipos de datos comunes: VARCHAR para texto de longitud variable; DATE para fechas cronológicas; DECIMAL con precisión y escala para importes monetarios; INT para enteros y claves; y BOOLEAN para valores lógicos binarios.
En la sentencia CREATE TABLE definimos cada columna, su tipo de dato y restricciones como PRIMARY KEY.
Y el tip de oro para el examen: En los enunciados, los sustantivos son tus tablas y entidades; los adjetivos y datos son tus atributos; y los verbos y acciones determinan las relaciones, cardinalidades y claves foráneas.

¡Éxitos en tu parcial!
""".strip()
    }
]

async def generate_audios():
    out_dir = os.path.join(os.path.dirname(__file__), "audios_estudio")
    os.makedirs(out_dir, exist_ok=True)
    
    print(f"Generando {len(AUDIO_MODULES)} audios con la voz: {VOICE}...")
    for mod in AUDIO_MODULES:
        out_path = os.path.join(out_dir, mod["filename"])
        print(f"Generando: {mod['filename']} ({mod['title']})...")
        communicate = edge_tts.Communicate(mod["text"], voice=VOICE, rate="+0%", pitch="+0Hz")
        await communicate.save(out_path)
        print(f"[OK] Guardado: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    asyncio.run(generate_audios())
