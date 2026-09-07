# Cómo ejecutar el proyecto Polinomio MVC en una nueva computadora

Estos son los pasos para descargar el proyecto desde GitHub (como ZIP) y ejecutarlo en cualquier computadora con Windows.

## 1. Descargar el proyecto desde GitHub

1. Ve al repositorio en el navegador.
2. Haz clic en el botón verde **"Code"**.
3. Selecciona **"Download ZIP"**.
4. Extrae el ZIP (clic derecho → "Extraer todo") en la carpeta donde quieras guardarlo.

## 2. Abrir la carpeta en VS Code

`File` → `Open Folder` → selecciona la carpeta extraída.

## 3. Abrir una terminal nueva

`Ctrl + ñ` (o `Ctrl + \``)

## 4. Verificar que Python esté instalado

```
python --version
```

Si no aparece ninguna versión, instala Python desde:
https://www.python.org/downloads/

⚠️ Al instalar, marca la casilla **"Add python.exe to PATH"** antes de darle a instalar.

## 5. Dar permisos de ejecución a PowerShell

Solo es necesario hacerlo una vez por computadora:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Si pregunta confirmación, escribe `S` y presiona Enter.

## 6. Crear el entorno virtual

```
python -m venv envWin
```

## 7. Activar el entorno virtual

```
envWin\Scripts\Activate.ps1
```

Debe aparecer `(envWin)` al inicio de la línea de la terminal, por ejemplo:

```
(envWin) PS C:\Users\Usuario\Polinomio>
```

## 8. Entrar a la carpeta del programa

```
cd polinomio
```

## 9. Ejecutar el programa

```
python main.py
```

Esto abrirá la ventana del programa con el campo para ingresar el polinomio.

---

## Notas adicionales

- El proyecto solo usa `tkinter`, que viene incluido con Python — no es necesario instalar ninguna librería extra con `pip`.
- Para desactivar el entorno virtual cuando termines:
  ```
  deactivate
  ```
- Para volver a ejecutar el programa en otra sesión (sin tener que repetir todos los pasos), solo necesitas:
  1. Abrir la terminal en la carpeta del proyecto.
  2. Activar el entorno: `envWin\Scripts\Activate.ps1`
  3. Entrar a la carpeta: `cd polinomio`
  4. Ejecutar: `python main.py`
