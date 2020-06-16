# Lista de ventas globales

## Instalación 
1. Ejecutar
```
pip install -r requirements.txt
```
2. Crear _config.py

Renombrar '_config_template.py' a '_config.py' e infoprmar correctamente de sus claves

3. informar correctamente .env (solo para desarrollo)

Renombrar '.env_template' a '.env' 


- FLASK_APP = run.py
- FLASK_ENV= development o production

4. Crear BD

Ejecutar migrations.sql con s1lite3 en el fichero elegido como base de datos.