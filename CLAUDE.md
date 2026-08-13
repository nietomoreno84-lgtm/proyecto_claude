# Proyecto Claude

## ¿Qué es este proyecto?
-Un asistente de IA intregado con claude para optimizar los flujos de trabajo de desarrollo.

## Cómo trabajar aquí
- Usa Python como lenguaje principal.
- Explica el código con comentarios simples cuando sea algo nuevo para mí.
- Si hay varias formas de hacer algo, elige la más fácil de entender, no la más avanzada.
- Antes de instalar librerías nuevas, pregúntame primero.
- crea variables en español y sencillas.

## Estructura del proyecto
- `main.py` → archivo principal donde corre el programa.
- `requirements.txt` → lista de librerías que necesita el proyecto.
- `/config` → archivos de configuración del proyecto.

## Cómo ejecutar el proyecto
1. Activar el entorno virtual: `source .venv/Scripts/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python main.py`

## Convenciones
- [CODIGO] Usar camelCase para variables y funciones.
- [GIT] Mensajes de commit claros y concisos.
- [DOCS] Toda nueva funcion debe tenr documentacion Markdown.

## Restricciones
- No instalar dependencias nuevas sin confirmación
- Las credenciales van siempre en .env, nunca en el código.
- Limite de tokens de Claude: 150k.