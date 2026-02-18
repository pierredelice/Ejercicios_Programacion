# 💊 Proyecto 3: Sistema de Evaluación de Salud Biomédica

## 🎯 Objetivo del Proyecto

Crear un sistema interactivo que calcule y evalúe métricas de salud, proporcionando recomendaciones basadas en parámetros biomédicos. Los estudiantes aplicarán conceptos de programación a cálculos médicos reales.

**Carrera:** Tecnología Biomédica
**Duración:** 2 semanas
**Equipo:** 3 estudiantes

## 📚 Conceptos de Python Utilizados

- Variables y tipos de datos (int, float, str)
- Operadores aritméticos para cálculos médicos
- Operadores de comparación para rangos de salud
- Condicionales complejos (if/elif/else anidados)
- Loops para menús y múltiples cálculos
- **Listas** para almacenar historial de pacientes
- **Funciones** para cada cálculo médico (con parámetros y return)
- **Archivos CSV/TXT** para registros de pacientes
- Formateo de números (redondeo, decimales)
- Validación de entrada de datos

## 🎓 Competencias a Desarrollar

1. Implementar fórmulas médicas en código
2. Evaluar rangos de salud según estándares médicos
3. Proporcionar recomendaciones basadas en datos
4. Validar datos biomédicos (rangos realistas)
5. Presentar información médica de forma clara
6. Comprender la importancia de la precisión en salud

## 📋 Requisitos Funcionales

### ✅ Requisitos Mínimos (Obligatorios)

1. **Menú Principal del Sistema**
   - Mostrar opciones de calculadoras biomédicas
   - Permitir múltiples cálculos en una sesión
   - Opción para salir del sistema
   - Loop continuo y navegación clara

2. **Funciones de Cálculo Médico (Mínimo 5)**
   - `calcular_imc(peso, altura)` - Retorna IMC y clasificación
   - `calcular_fc_maxima(edad)` - Retorna zonas de frecuencia cardíaca
   - `calcular_dosis(peso, dosis_por_kg)` - Retorna dosis total
   - `calcular_hidratacion(peso, actividad)` - Retorna ml y vasos
   - `evaluar_presion_arterial(sistolica, diastolica)` - Retorna clasificación

3. **Sistema de Registro de Pacientes (Listas)**
   - Almacenar datos de pacientes en lista
   - Cada paciente: nombre, fecha, tipo de evaluación, resultado
   - Máximo 20 registros (eliminar más antiguos)
   - Función para ver historial de registros

4. **Persistencia de Datos (Archivos CSV)**
   - Guardar registros en `datos/pacientes.csv`
   - Formato: `fecha,nombre,tipo_evaluacion,valor1,valor2,resultado,clasificacion`
   - Cargar registros al iniciar
   - Exportar reporte de paciente específico

5. **Funciones de Validación**
   - `validar_peso(peso)` - Validar rango 20-300 kg
   - `validar_altura(altura)` - Validar rango 0.5-2.5 m
   - `validar_presion(valor, tipo)` - Validar rangos de presión
   - `validar_edad(edad)` - Validar rango 1-120 años

6. **Sistema de Estadísticas**
   - Calcular promedio de IMC de todos los registros
   - Calcular evaluación más realizada
   - Generar resumen estadístico
   - Guardar estadísticas en archivo separado

### 🌟 Características Opcionales (Extra)

- Sistema de búsqueda de pacientes por nombre
- Comparación de evaluaciones anteriores de un paciente
- Exportar reporte completo de paciente en TXT
- Gráfico ASCII de evolución de IMC del paciente
- Alertas automáticas para valores críticos (guardadas en archivo)
- Estadísticas mensuales/semanales
- Sistema de recordatorios (próxima evaluación)
- Calculadora de Tasa Metabólica Basal (TMB)
- Calculadora de superficie corporal
- Base de datos de múltiples pacientes con ID único

## 👥 Distribución de Trabajo Sugerida

### Estudiante 1: Estructura y Gestión de Datos
- Menú principal del sistema
- **Funciones de archivo** (cargar/guardar registros CSV)
- **Funciones de validación** (peso, altura, edad, presión)
- Sistema de búsqueda en registros
- Integración de módulos

### Estudiante 2: Funciones de Cálculo Médico
- **Función calcular_imc()** con clasificación
- **Función calcular_fc_maxima()** con zonas
- **Función evaluar_presion_arterial()** con clasificación
- **Función calcular_hidratacion()** con ajuste por actividad
- Todas con parámetros, return y docstrings

### Estudiante 3: Sistema de Registros y Estadísticas
- **Sistema de lista de pacientes** (agregar, ver, buscar)
- **Función calcular_dosis()** medicamentos
- **Funciones estadísticas** (promedios, más común)
- Exportar reportes individuales
- Características opcionales adicionales

## 📊 Ejemplo de Ejecución

```
╔═════════════════════════════════════════════════════╗
║  💊 SISTEMA DE EVALUACIÓN DE SALUD BIOMÉDICA 💊    ║
║     Universidad de Guadalajara - Campus Chapala    ║
║     Equipo: [Nombres de los estudiantes]           ║
╚═════════════════════════════════════════════════════╝

MENÚ PRINCIPAL:
1. Calculadora de IMC
2. Zonas de Frecuencia Cardíaca
3. Calculadora de Dosis de Medicamento
4. Necesidades de Hidratación
5. Evaluador de Presión Arterial
6. Salir

Seleccione una opción: 1

--- CALCULADORA DE IMC ---
Ingrese su peso en kilogramos: 70
Ingrese su altura en metros: 1.75

Calculando...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RESULTADOS DE IMC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Peso:     70.0 kg
Altura:   1.75 m
IMC:      22.9

Clasificación: ✅ PESO NORMAL (18.5 - 24.9)

RECOMENDACIÓN:
Su IMC está dentro del rango saludable.
Continúe con hábitos de alimentación balanceada
y actividad física regular.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿Desea realizar otro cálculo? (s/n): n

[Volver al menú principal...]
```

## 📝 Rúbrica de Evaluación (100 puntos)

### Funcionalidad (40 puntos)
- [ ] Menú principal funciona correctamente (5 pts)
- [ ] Calculadora de IMC con clasificación completa (8 pts)
- [ ] Zonas de frecuencia cardíaca correctas (7 pts)
- [ ] Calculadora de dosis de medicamento (7 pts)
- [ ] Calculadora de hidratación (6 pts)
- [ ] Evaluador de presión arterial (7 pts)

### Precisión Médica (25 puntos)
- [ ] Fórmulas implementadas correctamente (10 pts)
- [ ] Clasificaciones según estándares médicos (8 pts)
- [ ] Recomendaciones apropiadas y seguras (7 pts)

### Código (20 puntos)
- [ ] Uso correcto de operadores y variables (5 pts)
- [ ] Condicionales bien estructurados (6 pts)
- [ ] Validación de entrada adecuada (5 pts)
- [ ] Código legible y organizado (4 pts)

### Documentación y Presentación (15 puntos)
- [ ] Comentarios claros en el código (5 pts)
- [ ] README del equipo con fuentes médicas (5 pts)
- [ ] Presentación clara de resultados (3 pts)
- [ ] Advertencias de seguridad incluidas (2 pts)

## 🚀 Entregables

1. **Archivo:** `sistema_salud_equipo_[nombres].py`
2. **README del equipo:** `README_EQUIPO.md` con:
   - Nombres de los integrantes y roles
   - Fuentes médicas consultadas (estándares OMS, AHA, etc.)
   - Instrucciones de uso
   - Limitaciones y advertencias del sistema
3. **Documento de Fórmulas:** Incluir las fórmulas médicas utilizadas
4. **Advertencia Legal:** Incluir disclaimer de uso educativo

## ⚕️ Fórmulas y Estándares Médicos

### 1. IMC (Índice de Masa Corporal)
```
IMC = peso (kg) / altura² (m)

Clasificación OMS:
< 18.5       Bajo peso
18.5 - 24.9  Normal
25.0 - 29.9  Sobrepeso
30.0 - 34.9  Obesidad Clase I
35.0 - 39.9  Obesidad Clase II
≥ 40.0       Obesidad Clase III
```

### 2. Frecuencia Cardíaca Máxima
```
FCM = 220 - edad

Zonas de Entrenamiento:
Zona 1: 50-60% FCM (Recuperación)
Zona 2: 60-70% FCM (Quema de grasa)
Zona 3: 70-80% FCM (Aeróbica)
Zona 4: 80-90% FCM (Anaeróbica)
Zona 5: 90-100% FCM (Esfuerzo máximo)
```

### 3. Hidratación
```
Agua diaria = 35 ml/kg de peso corporal

Ajustes:
- Sedentario: 35 ml/kg
- Activo moderado: 40 ml/kg
- Muy activo: 45 ml/kg

1 vaso ≈ 250 ml
```

### 4. Presión Arterial (AHA)
```
Normal:         < 120 / < 80
Elevada:        120-129 / < 80
Hipertensión I: 130-139 / 80-89
Hipertensión II: ≥ 140 / ≥ 90
Crisis:         > 180 / > 120
```

## 💡 Consejos de Implementación

### 1. Validación de Rangos Médicos
```python
# Ejemplo: Validar peso realista
while True:
    peso = float(input("Peso en kg: "))
    if peso > 20 and peso < 300:
        break
    else:
        print("❌ Peso fuera de rango. Ingrese un valor entre 20 y 300 kg.")
```

### 2. Formateo de Resultados
```python
# Mostrar números con decimales apropiados
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.1f}")  # 1 decimal

# Redondear dosis
dosis = peso * dosis_por_kg
print(f"Dosis: {round(dosis, 2)} mg")
```

### 3. Clasificación con Condicionales
```python
if imc < 18.5:
    clasificacion = "Bajo peso"
    recomendacion = "Consulte con un nutricionista..."
elif imc < 25:
    clasificacion = "Normal"
    recomendacion = "Mantenga hábitos saludables..."
elif imc < 30:
    clasificacion = "Sobrepeso"
    recomendacion = "Considere aumentar actividad física..."
# ... etc
```

### 4. Cálculo de Zonas de FC
```python
fc_maxima = 220 - edad
zona1_min = fc_maxima * 0.50
zona1_max = fc_maxima * 0.60
zona2_min = fc_maxima * 0.60
zona2_max = fc_maxima * 0.70
# ... etc
```

## ⚠️ Advertencias Importantes

### Disclaimer Legal (INCLUIR en su programa)
```
AVISO IMPORTANTE:
Este programa es solo para fines educativos.
NO reemplaza el consejo médico profesional.
Para diagnósticos y tratamientos, consulte siempre
a un profesional de la salud calificado.
```

### Consideraciones Éticas
- Los cálculos son aproximaciones generales
- Las recomendaciones deben ser educativas, no prescriptivas
- Incluir siempre la sugerencia de consultar con un médico
- Ser sensible con terminología relacionada al peso

### Rangos de Validación Recomendados
- Peso: 20-300 kg
- Altura: 0.50-2.50 m
- Edad: 1-120 años
- Presión sistólica: 70-250 mmHg
- Presión diastólica: 40-150 mmHg

## 📚 Fuentes Médicas Recomendadas

- **OMS (Organización Mundial de la Salud):** Clasificación de IMC
- **AHA (American Heart Association):** Guías de presión arterial
- **ACSM (American College of Sports Medicine):** Zonas de FC
- **CDC (Centers for Disease Control):** Guías generales de salud

Documenten las fuentes que consulten en su README.

## 📅 Cronograma Sugerido

### Semana 1
- **Día 1-2:** Investigar fórmulas médicas, planificación
- **Día 3-4:** Implementar calculadoras básicas (IMC, hidratación)
- **Día 5-6:** Implementar calculadoras cardíacas
- **Día 7:** Implementar calculadora de medicamento, integración

### Semana 2
- **Día 1-2:** Añadir validaciones robustas
- **Día 3-4:** Mejorar presentación de resultados, características extras
- **Día 5:** Documentación de fórmulas y fuentes
- **Día 6-7:** Pruebas exhaustivas con casos reales, preparar entrega

## 🏆 Criterio de Excelencia

Un proyecto excepcional debe:
- ✅ Implementar todas las calculadoras correctamente
- ✅ Validar entradas exhaustivamente (rangos médicos realistas)
- ✅ Proporcionar recomendaciones apropiadas y seguras
- ✅ Presentar resultados de forma profesional y clara
- ✅ Incluir al menos 2 características opcionales
- ✅ Tener código bien comentado y documentado
- ✅ Incluir fuentes médicas consultadas
- ✅ Demostrar comprensión de la aplicación médica

---

**¡Apliquen la programación para mejorar la salud!** 💊⚕️

Recuerden: La precisión en cálculos médicos puede impactar vidas reales. Programen con responsabilidad y cuidado.
