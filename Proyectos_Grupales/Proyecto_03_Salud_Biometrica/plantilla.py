"""
Sistema de Evaluación de Salud Biomédica
Proyecto de Tecnología Biomédica

⚠️ AVISO IMPORTANTE:
Este programa es solo para fines educativos.
NO reemplaza el consejo médico profesional.
Para diagnósticos y tratamientos, consulte siempre
a un profesional de la salud calificado.

Equipo:
- Estudiante 1: [Nombre] - Estructura y Métricas Básicas
- Estudiante 2: [Nombre] - Calculadoras Cardíacas
- Estudiante 3: [Nombre] - Cálculos de Medicación

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal del sistema de salud"""
    print("\n" + "="*70)
    print("       💊 SISTEMA DE EVALUACIÓN DE SALUD BIOMÉDICA 💊")
    print("          Universidad de Guadalajara - Campus GDL")
    print("="*70)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora de IMC (Índice de Masa Corporal)")
    print("2. Zonas de Frecuencia Cardíaca")
    print("3. Calculadora de Dosis de Medicamento")
    print("4. Necesidades de Hidratación")
    print("5. Evaluador de Presión Arterial")
    print("6. Salir")
    print("-"*70)


def mostrar_disclaimer():
    """Muestra el aviso legal del sistema"""
    print("\n" + "="*70)
    print("⚠️  AVISO IMPORTANTE")
    print("="*70)
    print("Este programa es solo para fines EDUCATIVOS.")
    print("NO reemplaza el consejo médico profesional.")
    print("Para diagnósticos y tratamientos, consulte siempre")
    print("a un profesional de la salud calificado.")
    print("="*70)


# ============================================
# SECCIÓN 2: CALCULADORA DE IMC (Estudiante 1)
# ============================================

def calcular_imc():
    """
    Calcula el IMC y proporciona clasificación según OMS.
    IMC = peso (kg) / altura² (m)
    """
    print("\n" + "━"*70)
    print("  CALCULADORA DE IMC")
    print("━"*70)

    # TODO: Implementar
    # 1. Solicitar peso en kg (validar: 20-300 kg)
    # 2. Solicitar altura en m (validar: 0.50-2.50 m)
    # 3. Calcular IMC = peso / (altura ** 2)
    # 4. Clasificar según:
    #    < 18.5       → Bajo peso
    #    18.5 - 24.9  → Normal
    #    25.0 - 29.9  → Sobrepeso
    #    30.0 - 34.9  → Obesidad I
    #    35.0 - 39.9  → Obesidad II
    #    >= 40.0      → Obesidad III
    # 5. Mostrar resultado y recomendación

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 3: HIDRATACIÓN (Estudiante 1)
# ============================================

def calcular_hidratacion():
    """
    Calcula necesidades de hidratación diaria.
    Fórmula: 35 ml/kg (ajustable según actividad)
    """
    print("\n" + "━"*70)
    print("  CALCULADORA DE NECESIDADES DE HIDRATACIÓN")
    print("━"*70)

    # TODO: Implementar
    # 1. Solicitar peso en kg
    # 2. Solicitar nivel de actividad:
    #    1 = Sedentario (35 ml/kg)
    #    2 = Moderado (40 ml/kg)
    #    3 = Muy activo (45 ml/kg)
    # 3. Calcular agua_ml = peso * factor
    # 4. Convertir a litros (/ 1000)
    # 5. Calcular vasos de 250ml = agua_ml / 250
    # 6. Mostrar resultados en ml, litros y vasos

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 4: FRECUENCIA CARDÍACA (Estudiante 2)
# ============================================

def calcular_zonas_fc():
    """
    Calcula zonas de frecuencia cardíaca para entrenamiento.
    FC Máxima = 220 - edad
    """
    print("\n" + "━"*70)
    print("  CALCULADORA DE ZONAS DE FRECUENCIA CARDÍACA")
    print("━"*70)

    # TODO: Implementar
    # 1. Solicitar edad (validar: 1-120 años)
    # 2. Calcular FC máxima = 220 - edad
    # 3. Calcular zonas:
    #    Zona 1: 50-60% FCM (Recuperación)
    #    Zona 2: 60-70% FCM (Quema de grasa)
    #    Zona 3: 70-80% FCM (Aeróbica)
    #    Zona 4: 80-90% FCM (Anaeróbica)
    #    Zona 5: 90-100% FCM (Máxima)
    # 4. Mostrar tabla con cada zona y sus rangos
    # 5. Incluir descripción de cada zona

    # Ejemplo de cálculo:
    # fc_maxima = 220 - edad
    # zona1_min = fc_maxima * 0.50
    # zona1_max = fc_maxima * 0.60

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 5: PRESIÓN ARTERIAL (Estudiante 2)
# ============================================

def evaluar_presion_arterial():
    """
    Evalúa presión arterial según clasificación AHA.
    """
    print("\n" + "━"*70)
    print("  EVALUADOR DE PRESIÓN ARTERIAL")
    print("━"*70)

    # TODO: Implementar
    # 1. Solicitar presión sistólica (70-250 mmHg)
    # 2. Solicitar presión diastólica (40-150 mmHg)
    # 3. Clasificar según AHA:
    #    Normal:         sistólica < 120 Y diastólica < 80
    #    Elevada:        sistólica 120-129 Y diastólica < 80
    #    Hipertensión I: sistólica 130-139 O diastólica 80-89
    #    Hipertensión II: sistólica >= 140 O diastólica >= 90
    #    Crisis:         sistólica > 180 O diastólica > 120
    # 4. Mostrar clasificación y recomendación
    # 5. Si es crisis, advertir de emergencia médica

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 6: DOSIS DE MEDICAMENTO (Estudiante 3)
# ============================================

def calcular_dosis_medicamento():
    """
    Calcula dosis de medicamento basada en peso corporal.
    """
    print("\n" + "━"*70)
    print("  CALCULADORA DE DOSIS DE MEDICAMENTO")
    print("━"*70)
    print("⚠️  ADVERTENCIA: Esta calculadora es solo educativa.")
    print("    Siempre siga las instrucciones de un médico profesional.")
    print("━"*70)

    # TODO: Implementar
    # 1. Solicitar peso del paciente (kg)
    # 2. Solicitar dosis prescrita por kg (mg/kg)
    # 3. Calcular dosis total = peso * dosis_por_kg
    # 4. Mostrar resultado en mg
    # 5. Convertir a gramos si es >= 1000 mg
    # 6. Añadir advertencias:
    #    - Si peso < 18 kg: "Paciente pediátrico - Consultar pediatra"
    #    - Si dosis > 500 mg: "Dosis alta - Verificar con médico"

    # Ejemplo:
    # peso = 70 kg
    # dosis_por_kg = 10 mg/kg
    # dosis_total = 70 * 10 = 700 mg = 0.7 g

    pass  # Reemplazar con su código


# ============================================
# FUNCIONES DE VALIDACIÓN (Todos)
# ============================================

def validar_numero_en_rango(mensaje, minimo, maximo):
    """
    Valida que un número esté dentro de un rango.

    Args:
        mensaje (str): Mensaje para el usuario
        minimo (float): Valor mínimo aceptable
        maximo (float): Valor máximo aceptable

    Returns:
        float: Número validado
    """
    # TODO: Implementar validación
    # - Usar loop while True
    # - Intentar convertir entrada a float
    # - Verificar si está en el rango
    # - Si es válido, return valor
    # - Si no, mostrar error y repetir

    pass  # Reemplazar con su código


def validar_opcion(mensaje, opciones_validas):
    """
    Valida que la entrada sea una de las opciones válidas.

    Args:
        mensaje (str): Mensaje para el usuario
        opciones_validas (str): String con opciones válidas (ej: "123")

    Returns:
        str: Opción validada
    """
    # TODO: Implementar validación de opciones

    pass  # Reemplazar con su código


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def mostrar_separador():
    """Muestra un separador visual"""
    print("\n" + "━"*70 + "\n")


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


def preguntar_continuar():
    """
    Pregunta si el usuario desea realizar otro cálculo.

    Returns:
        bool: True si desea continuar, False si no
    """
    respuesta = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
    return respuesta == "s" or respuesta == "si"


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del sistema"""

    # Mostrar banner de bienvenida
    print("\n" + "╔" + "═"*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  💊 SISTEMA DE EVALUACIÓN DE SALUD BIOMÉDICA 💊".center(68) + "║")
    print("║" + " "*68 + "║")
    print("║" + "  Universidad de Guadalajara - Campus Chapala".center(68) + "║")
    print("║" + "  Equipo: [Nombres de los integrantes]".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "═"*68 + "╝")

    # Mostrar disclaimer
    mostrar_disclaimer()
    pausar()

    # Loop principal
    continuar_programa = True

    while continuar_programa:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            calcular_imc()
            if not preguntar_continuar():
                continuar_programa = False

        elif opcion == "2":
            calcular_zonas_fc()
            if not preguntar_continuar():
                continuar_programa = False

        elif opcion == "3":
            calcular_dosis_medicamento()
            if not preguntar_continuar():
                continuar_programa = False

        elif opcion == "4":
            calcular_hidratacion()
            if not preguntar_continuar():
                continuar_programa = False

        elif opcion == "5":
            evaluar_presion_arterial()
            if not preguntar_continuar():
                continuar_programa = False

        elif opcion == "6":
            print("\n" + "="*70)
            print("  Gracias por usar el Sistema de Evaluación de Salud")
            print("  Recuerde: Siempre consulte con profesionales de la salud")
            print("  ¡Cuide su salud! 💊⚕️")
            print("="*70)
            continuar_programa = False

        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")
            pausar()

    print("\nSistema terminado. ¡Hasta pronto!")
    print("\nDesarrollado por: [Nombres del equipo]")
    print("Curso de Programación en Python - Dr. Pierre Delice")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
