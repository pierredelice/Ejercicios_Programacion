# 📚 Guía de Git y GitHub para Proyectos Grupales

## 🎯 Objetivos

Esta guía te ayudará a:
1. Crear un repositorio en GitHub
2. Trabajar en equipo con Git
3. Hacer commits significativos
4. Mantener tu proyecto organizado

---

## 🚀 Paso 1: Configuración Inicial

### 1.1 Configurar Git (solo primera vez)

```bash
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email
git config --global user.email "tu.email@example.com"

# Verificar configuración
git config --list
```

### 1.2 Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com) y inicia sesión
2. Click en el botón verde "New" o "+" → "New repository"
3. Nombre: `[proyecto]-[apellidos]` (ej: `calculadora-digital-garcia-lopez-martinez`)
4. Descripción: "Proyecto de [nombre] - Curso de Python UdeG"
5. ✅ Marcar "Public"
6. ✅ Marcar "Add a README file"
7. ✅ Agregar .gitignore → seleccionar "Python"
8. ✅ Agregar licencia → seleccionar "MIT License"
9. Click en "Create repository"

---

## 📁 Paso 2: Estructura Inicial del Proyecto

### 2.1 Clonar el Repositorio

```bash
# Clonar tu repositorio
git clone https://github.com/[usuario]/[nombre-repo].git

# Entrar al directorio
cd [nombre-repo]
```

### 2.2 Crear Estructura de Carpetas

```bash
# Crear carpeta para datos
mkdir datos

# Crear archivo .gitkeep para mantener carpeta vacía en Git
touch datos/.gitkeep

# Crear carpeta para ejemplos (opcional)
mkdir ejemplos
```

### 2.3 Crear Archivo .gitignore

Edita el archivo `.gitignore` y asegúrate de incluir:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# Archivos de respaldo
*.bak
*.txt.bak
*~

# Sistema operativo
.DS_Store
Thumbs.db
.idea/
.vscode/

# Datos generados (pero mantener ejemplos)
datos/*.txt
datos/*.csv
!datos/*_ejemplo.*
!datos/.gitkeep
```

---

## 🔄 Paso 3: Workflow de Trabajo en Equipo

### 3.1 Antes de Empezar a Trabajar (Siempre)

```bash
# Actualizar tu copia local con cambios del equipo
git pull origin main
```

### 3.2 Trabajar en tu Código

1. Abre tu editor y trabaja en tu parte del código
2. Prueba que funcione correctamente
3. Guarda tus cambios

### 3.3 Hacer Commit de tus Cambios

```bash
# Ver qué archivos cambiaron
git status

# Agregar archivos específicos
git add archivo.py
git add datos/.gitkeep

# O agregar todos los archivos Python modificados
git add *.py

# Crear commit con mensaje descriptivo
git commit -m "Agregar función de suma y resta"

# Ver historial de commits
git log --oneline
```

### 3.4 Subir tus Cambios a GitHub

```bash
# Subir al repositorio en GitHub
git push origin main
```

---

## ✍️ Paso 4: Buenos Mensajes de Commit

### ❌ Mensajes MALOS:
```bash
git commit -m "cambios"
git commit -m "fix"
git commit -m "asdf"
git commit -m "aaa"
```

### ✅ Mensajes BUENOS:
```bash
git commit -m "Agregar función calcular_imc con validación"
git commit -m "Implementar sistema de historial con listas"
git commit -m "Corregir bug en división por cero"
git commit -m "Agregar persistencia de datos en archivo CSV"
git commit -m "Crear menú principal con opciones 1-6"
git commit -m "Documentar funciones con docstrings"
```

### 📝 Formato Recomendado:

**Verbo en imperativo + qué hiciste**

Ejemplos de verbos:
- `Agregar` - para nuevo código
- `Implementar` - para nueva funcionalidad completa
- `Corregir` - para bugs
- `Actualizar` - para mejoras
- `Eliminar` - para código removido
- `Refactorizar` - para reorganización de código
- `Documentar` - para comentarios/docs

---

## 👥 Paso 5: Trabajar en Equipo Sin Conflictos

### 5.1 Coordinación del Equipo

**División clara:**
- Estudiante 1: Archivos/funciones A, B, C
- Estudiante 2: Archivos/funciones D, E, F
- Estudiante 3: Archivos/funciones G, H, I

### 5.2 Workflow Diario

**Cada estudiante:**

```bash
# 1. ANTES de trabajar
git pull origin main

# 2. Trabajar en TU parte del código
# ... editar, probar, guardar ...

# 3. Hacer commit
git add tu_archivo.py
git commit -m "Descripción clara de tus cambios"

# 4. Actualizar antes de subir (por si hubo cambios)
git pull origin main

# 5. Subir tus cambios
git push origin main
```

### 5.3 Si Hay Conflictos

Si Git te dice que hay conflictos:

1. **No entres en pánico**
2. Abre el archivo con conflicto
3. Busca las secciones marcadas:
   ```python
   <<<<<<< HEAD
   Tu código
   =======
   Código de tu compañero
   >>>>>>> branch
   ```
4. Decide qué código mantener (o combinar ambos)
5. Elimina las marcas `<<<<`, `====`, `>>>>`
6. Guarda el archivo
7. Haz commit:
   ```bash
   git add archivo.py
   git commit -m "Resolver conflicto en función X"
   git push origin main
   ```

---

## 📊 Paso 6: Verificar el Trabajo del Equipo

### 6.1 Ver Estado del Repositorio

```bash
# Ver qué archivos cambiaron
git status

# Ver diferencias detalladas
git diff

# Ver historial de commits
git log --oneline --graph --all

# Ver quién hizo cada commit
git log --oneline --all --author="Nombre"
```

### 6.2 Verificar Contribuciones

En GitHub:
1. Ve a tu repositorio
2. Click en "Insights" → "Contributors"
3. Verás gráfica de commits por persona

---

## 📝 Paso 7: README del Proyecto

### 7.1 Usar la Plantilla

Usa el archivo `README_GITHUB_TEMPLATE.md` como base para tu proyecto.

### 7.2 Personalizar

Edita las secciones:
- Reemplaza `[Nombre del Proyecto]` con tu nombre
- Llena la tabla del equipo
- Describe características
- Agrega ejemplos de uso

### 7.3 Commit del README

```bash
git add README.md
git commit -m "Actualizar README con información del equipo"
git push origin main
```

---

## 🎯 Checklist de Entregas

Antes de la entrega final, verifica:

### Repositorio GitHub
- [ ] Repositorio es público
- [ ] README.md está completo y profesional
- [ ] .gitignore está configurado
- [ ] Licencia MIT está incluida
- [ ] Estructura de carpetas es correcta

### Commits
- [ ] Mínimo 15 commits en total
- [ ] Commits distribuidos entre los 3 integrantes
- [ ] Mensajes de commit son descriptivos
- [ ] No hay commits con mensajes vagos ("fix", "cambios", etc.)

### Código
- [ ] Todas las funciones tienen docstrings
- [ ] Código está comentado adecuadamente
- [ ] Variables tienen nombres descriptivos
- [ ] No hay código comentado sin uso

### Archivos
- [ ] Carpeta `datos/` existe
- [ ] Archivos de ejemplo están incluidos
- [ ] .gitignore funciona correctamente
- [ ] No hay archivos innecesarios (`__pycache__`, `.DS_Store`)

---

## 🆘 Comandos de Emergencia

### Deshacer el último commit (sin perder cambios)
```bash
git reset --soft HEAD~1
```

### Descartar cambios no guardados
```bash
git checkout -- archivo.py
```

### Ver diferencias con versión anterior
```bash
git diff HEAD~1 archivo.py
```

### Recuperar archivo borrado
```bash
git checkout HEAD -- archivo.py
```

---

## 💡 Consejos Finales

1. **Commit frecuentemente:** Mejor muchos commits pequeños que uno grande
2. **Pull antes de push:** Siempre actualiza antes de subir
3. **Mensajes claros:** Tus compañeros deben entender qué hiciste
4. **Prueba antes de commit:** Asegúrate que tu código funciona
5. **Comunícate:** Avisa al equipo cuando trabajes en algo importante
6. **No subas archivos grandes:** Imágenes, videos, o archivos de datos enormes
7. **Respeta el trabajo de otros:** No modifiques código que no es tuyo sin avisar

---

## 📚 Recursos Adicionales

- [GitHub Docs](https://docs.github.com) - Documentación oficial
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) - Hoja de trucos
- [GitHub Desktop](https://desktop.github.com/) - Interfaz gráfica (opcional)

---

## 🎓 Apoyo

Si tienes problemas con Git/GitHub:
1. Consulta esta guía
2. Pregunta a tus compañeros de equipo
3. Busca en [Stack Overflow](https://stackoverflow.com)
4. Consulta al instructor en horario de clase

---

**¡Éxito con tu proyecto!** 🚀

Recuerda: Git es una herramienta profesional usada por millones de desarrolladores. Aprenderla ahora te ayudará en tu carrera.
