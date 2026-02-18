# 📊 Resumen de Proyectos Grupales - Versión Avanzada

## 🎯 Cambios Principales

Los proyectos han sido **actualizados y mejorados** para incluir conceptos avanzados:

### ✅ Conceptos Añadidos
- **Listas** - Almacenar historiales, galerías, y registros
- **Funciones** - Todas las operaciones principales como funciones con docstrings
- **Archivos** - Persistencia de datos en TXT y CSV
- **Git/GitHub** - Repositorio obligatorio con estructura profesional
- **Datasets** - Cada proyecto trabaja con archivos de datos

### 📚 Módulos del Curso Cubiertos
**Módulos 1-11:** Variables, Números, Strings, Operadores, Condicionales, Iteración, Listas, Tuplas/Sets, Funciones, Funciones Avanzadas, Archivos

---

## 📁 Estructura Completa de Archivos

```
Proyectos_Grupales/
│
├── README.md                           # Descripción general
├── README_GITHUB_TEMPLATE.md           # Plantilla para README de GitHub
├── GIT_GITHUB_GUIDE.md                 # Guía completa de Git/GitHub
├── INSTRUCCIONES_PROFESOR.md           # Guía para el instructor
├── RESUMEN_PROYECTOS_AVANZADOS.md      # Este archivo
│
├── Proyecto_01_Calculadora_Digital/
│   ├── README.md                       # Especificaciones completas
│   ├── plantilla.py                    # Plantilla básica (original)
│   ├── plantilla_avanzada.py          # Plantilla con funciones y archivos
│   ├── ejemplos.md                     # Ejemplos básicos
│   ├── ejemplos_extendidos.md         # 100+ casos de prueba
│   ├── .gitignore_template            # Plantilla de .gitignore
│   └── datos/
│       ├── .gitkeep                   # Para mantener carpeta en Git
│       └── historial_ejemplo.txt      # Ejemplo de formato de datos
│
├── Proyecto_02_Arte_ASCII/
│   ├── README.md                       # Especificaciones actualizadas
│   ├── plantilla.py                    # Plantilla con funciones
│   ├── ejemplos.md                     # Galería de ejemplos
│   └── datos/                          # Carpeta para guardar arte
│       └── .gitkeep
│
└── Proyecto_03_Salud_Biometrica/
    ├── README.md                       # Especificaciones actualizadas
    ├── plantilla.py                    # Plantilla con funciones
    ├── ejemplos.md                     # Ejemplos de cálculos médicos
    └── datos/
        ├── .gitkeep
        └── pacientes_ejemplo.csv       # Ejemplo de formato CSV
```

---

## 🎯 Proyecto 1: Calculadora Digital - Versión Avanzada

### Características Principales
- **15+ funciones** matemáticas y de conversión
- **Sistema de historial** con listas (últimas 10 operaciones)
- **Persistencia** en `datos/historial.txt`
- **Algoritmos manuales** para conversiones (binario, hexadecimal)
- **Validación robusta** con funciones dedicadas

### Funciones Requeridas
```python
# Operaciones matemáticas (6)
sumar(a, b)
restar(a, b)
multiplicar(a, b)
dividir(a, b)
modulo(a, b)
potencia(a, b)

# Conversiones numéricas (4)
decimal_a_binario(numero)
decimal_a_hexadecimal(numero)
binario_a_decimal(binario)
hexadecimal_a_decimal(hexadecimal)

# Conversiones de unidades (6+)
bytes_a_kilobytes(bytes)
kilobytes_a_megabytes(kb)
megabytes_a_gigabytes(mb)
# ... y sus inversas

# Gestión de historial (3)
agregar_al_historial(operacion, num1, num2, resultado)
mostrar_historial()
limpiar_historial()

# Gestión de archivos (2)
guardar_historial_archivo()
cargar_historial_archivo()

# Validación (2)
validar_numero(mensaje)
validar_numero_entero(mensaje)
```

### Archivos de Datos
- `datos/historial.txt` - Formato: `fecha | operacion: num1 op num2 = resultado`

### Casos de Prueba
- **100+ test cases** en `ejemplos_extendidos.md`
- Matriz completa de pruebas
- Edge cases documentados

---

## 🎨 Proyecto 2: Arte ASCII - Versión Avanzada

### Características Principales
- **10+ funciones** de generación de arte
- **Galería persistente** con listas
- **Exportar arte** a archivos `.txt`
- **Importar arte** desde archivos
- **Sistema de categorías** (geométrico, artístico, animaciones)

### Funciones Requeridas
```python
# Patrones geométricos (3)
generar_triangulo(altura) → str
generar_cuadrado(lado) → str
generar_piramide(altura) → str

# Texto artístico (2)
generar_banner(texto) → str
generar_marco(texto, estilo) → str

# Animaciones (2)
animar_barra_progreso()
animar_texto_movil(texto)

# Utilidades (1)
generar_tabla(numero) → str

# Gestión de galería (4)
agregar_a_galeria(titulo, arte)
mostrar_galeria()
guardar_arte_archivo(arte, nombre_archivo)
cargar_arte_archivo(nombre_archivo)
```

### Archivos de Datos
- `datos/galeria_[nombre].txt` - Múltiples archivos, uno por arte
- `datos/galeria_indice.txt` - Índice de todas las creaciones

---

## 💊 Proyecto 3: Sistema de Salud - Versión Avanzada

### Características Principales
- **10+ funciones** de cálculo médico
- **Sistema de registros** con listas (últimos 20 pacientes)
- **Base de datos CSV** para persistencia
- **Estadísticas** de todos los registros
- **Exportar reportes** individuales

### Funciones Requeridas
```python
# Cálculos médicos (5)
calcular_imc(peso, altura) → (imc, clasificacion)
calcular_fc_maxima(edad) → {zonas}
calcular_dosis(peso, dosis_por_kg) → dosis_mg
calcular_hidratacion(peso, actividad) → (ml, vasos)
evaluar_presion_arterial(sistolica, diastolica) → clasificacion

# Validación médica (4)
validar_peso(peso) → bool
validar_altura(altura) → bool
validar_presion(valor, tipo) → bool
validar_edad(edad) → bool

# Gestión de registros (5)
agregar_registro(nombre, tipo, valores, resultado)
mostrar_registros()
buscar_paciente(nombre)
calcular_estadisticas()
exportar_reporte(nombre_paciente)

# Gestión de archivos (2)
guardar_registros_csv()
cargar_registros_csv()
```

### Archivos de Datos
- `datos/pacientes.csv` - Formato: `fecha,nombre,tipo_evaluacion,valor1,valor2,resultado,clasificacion`
- `datos/estadisticas.txt` - Resumen estadístico generado

---

## 📋 Requisitos de Entrega (Todos los Proyectos)

### 1. Repositorio GitHub
- [ ] Repositorio público creado
- [ ] Nombre: `[proyecto]-[apellidos]` (ej: `calculadora-digital-garcia`)
- [ ] README.md completo y profesional
- [ ] .gitignore configurado para Python
- [ ] Licencia MIT incluida
- [ ] Mínimo **15 commits distribuidos entre 3 personas**
- [ ] Mensajes de commit descriptivos en español

### 2. Estructura de Código
- [ ] Todas las funciones tienen **docstrings** (estilo Google)
- [ ] Variables con nombres descriptivos
- [ ] Comentarios explicativos en secciones complejas
- [ ] Sin código comentado innecesario
- [ ] Sin errores de sintaxis

### 3. Funcionalidad
- [ ] Todas las funciones requeridas implementadas
- [ ] Sistema de menús funciona correctamente
- [ ] Validación de entrada robusta
- [ ] No hay crashes o errores no manejados
- [ ] Guardado/cargado de datos funciona

### 4. Archivos de Datos
- [ ] Carpeta `datos/` existe
- [ ] Archivos se crean automáticamente si no existen
- [ ] Formato de archivos es correcto
- [ ] Archivos de ejemplo incluidos
- [ ] .gitignore no sube datos personales

### 5. Documentación
- [ ] README.md en el repositorio está completo
- [ ] Instrucciones de instalación claras
- [ ] Ejemplos de uso incluidos
- [ ] Descripción de archivos de datos
- [ ] Tabla de contribuciones del equipo

---

## 🎓 Evaluación Actualizada

### Rúbrica (100 puntos)

| Categoría | Puntos | Criterios |
|-----------|--------|-----------|
| **Funcionalidad** | 35 | Funciones implementadas, menús, sin errores |
| **Código** | 25 | Funciones bien escritas, docstrings, variables descriptivas |
| **Persistencia** | 15 | Archivos funcionan correctamente, formato correcto |
| **Git/GitHub** | 15 | Commits apropiados, README completo, estructura correcta |
| **Documentación** | 10 | Comentarios, docstrings, README del equipo |

### Desglose Detallado

**Funcionalidad (35 puntos)**
- Todas las funciones obligatorias: 20 pts
- Sistema de menús: 5 pts
- Validación de entrada: 5 pts
- Sin errores/crashes: 5 pts

**Código (25 puntos)**
- Funciones con docstrings: 8 pts
- Uso correcto de listas: 5 pts
- Variables descriptivas: 4 pts
- Código organizado: 4 pts
- Sin código duplicado: 4 pts

**Persistencia (15 puntos)**
- Guardar datos funciona: 5 pts
- Cargar datos funciona: 5 pts
- Formato de archivo correcto: 3 pts
- Manejo de archivos no existentes: 2 pts

**Git/GitHub (15 puntos)**
- Mínimo 15 commits: 5 pts
- Commits de 3 personas: 3 pts
- Mensajes descriptivos: 3 pts
- README completo: 3 pts
- .gitignore correcto: 1 pt

**Documentación (10 puntos)**
- Comentarios en código: 4 pts
- Docstrings completos: 4 pts
- README del equipo: 2 pts

---

## ⏱️ Timeline Actualizado (2 semanas)

### Semana 1

**Días 1-2: Setup y Planificación**
- Crear repositorio en GitHub
- Clonar localmente
- Dividir tareas entre el equipo
- Crear estructura de carpetas
- Primer commit conjunto

**Días 3-5: Desarrollo de Funciones**
- Cada estudiante implementa sus funciones
- Escribir docstrings
- Probar individualmente
- Commits frecuentes

**Días 6-7: Primera Integración**
- Integrar módulos de todos
- Resolver conflictos de Git
- Probar el programa completo
- **Checkpoint con profesor** (10% de nota)

### Semana 2

**Días 1-3: Persistencia de Datos**
- Implementar carga/guardado de archivos
- Crear archivos de ejemplo
- Probar con diferentes datasets
- Validar formato de datos

**Días 4-5: Refinamiento**
- Agregar validaciones faltantes
- Mejorar mensajes de usuario
- Características opcionales
- Más commits

**Día 6: Documentación**
- Completar README.md
- Verificar docstrings
- Agregar comentarios
- Preparar ejemplos

**Día 7: Entrega Final**
- Pruebas exhaustivas
- Verificar checklist
- Último commit
- Enviar link del repo

---

## 💡 Consejos para el Éxito

### Para Estudiantes

1. **Git desde el día 1** - No esperen al final para usar Git
2. **Commits frecuentes** - Mejor muchos commits pequeños
3. **Prueben individualmente** - Antes de integrar, prueben su parte
4. **Lean los ejemplos** - Hay 100+ casos de prueba como referencia
5. **Usen las plantillas** - No empiecen de cero

### Para el Instructor

1. **Checkpoint obligatorio** - Día 7 para verificar progreso
2. **Revisar commits** - Asegurar contribución equitativa
3. **Probar persistencia** - Verificar que archivos funcionan
4. **Verificar GitHub** - Repositorio debe estar público
5. **Usar rúbrica** - Evaluación consistente y transparente

---

## 📚 Recursos Proporcionados

### Documentación
- ✅ README actualizado con nuevos requisitos
- ✅ Guía completa de Git/GitHub
- ✅ Plantilla profesional de README
- ✅ Especificaciones detalladas de cada proyecto
- ✅ 100+ casos de prueba

### Código
- ✅ Plantillas con estructura de funciones
- ✅ Ejemplos de docstrings
- ✅ Validación de entrada como referencia
- ✅ Gestión de archivos como ejemplo

### Datos
- ✅ Archivos de ejemplo en formato correcto
- ✅ .gitignore_template para Python
- ✅ Estructura de carpetas clara

---

## 🎯 Diferencias con Versión Básica

| Aspecto | Versión Básica | Versión Avanzada |
|---------|---------------|------------------|
| **Módulos** | 1-6 | 1-11 |
| **Funciones** | No requeridas | Obligatorias con docstrings |
| **Listas** | Opcional | Obligatorias para historial |
| **Archivos** | No incluidos | Obligatorios TXT/CSV |
| **Git/GitHub** | No requerido | Obligatorio con 15+ commits |
| **Duración** | 2 semanas | 2 semanas |
| **Complejidad** | Media | Media-Alta |

---

## ✅ Checklist Final del Instructor

Antes de calificar, verificar:

### Repositorio
- [ ] Es público y accesible
- [ ] Nombre sigue el formato requerido
- [ ] README está completo
- [ ] .gitignore funciona
- [ ] Licencia incluida

### Commits
- [ ] 15+ commits en total
- [ ] 3 personas han contribuido
- [ ] Mensajes son descriptivos
- [ ] Commits distribuidos en el tiempo

### Código
- [ ] Todas las funciones requeridas presentes
- [ ] Docstrings en todas las funciones
- [ ] Código funciona sin errores
- [ ] Validación de entrada robusta

### Archivos
- [ ] Carpeta datos/ existe
- [ ] Guardar funciona correctamente
- [ ] Cargar funciona correctamente
- [ ] Formato de datos es correcto

### Extras
- [ ] Al menos 1 característica opcional
- [ ] Código está bien organizado
- [ ] Experiencia de usuario es buena

---

**Preparado por:** Dr. Pierre Delice
**Versión:** 2.0 - Avanzada (con Listas, Funciones, Archivos, Git/GitHub)
**Fecha:** Febrero 2026
**Universidad de Guadalajara - Campus Chapala**

---

## 📞 Soporte

Para preguntas sobre esta versión actualizada:
- Consultar documentación en cada carpeta de proyecto
- Revisar `GIT_GITHUB_GUIDE.md` para problemas de Git
- Ver `ejemplos_extendidos.md` para casos de prueba
- Contactar al instructor en horario de clase

**¡Proyectos listos para equipos avanzados!** 🚀
