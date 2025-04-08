# PostalCodeClassification-ML_CNN

## 📒 Ejecución del `notebook` desde cero con `GPU` ([CUDA](https://developer.nvidia.com/cuda-toolkit) y [cuDNN](https://developer.nvidia.com/cudnn))

En una terminal de WSL, ejecuta el _script_ de inicio:

```batch
./setup.sh
```

El **entorno vistual** debería activarse automáticamente \[aparece '(.venvWSL)' al principio de la ruta en la terminal]. Si no lo hace, o para activarlo en futuras ocasiones, ejecuta el siguiente comando:

```batch
source .venvWSL/bin/activate
```

Instala en el entorno virtual los requisitos del proyecto:

```batch
pip install -r requirements.txt
```

Ejecuta las celdas del [notebook](DataProcessing-ModelBuilding.ipynb), observando el código y los resultados.

## 🔌 Conexión con la `API` y _`API testing`_

Ejecuta el siguiente comando para iniciar el servidor de `FastAPI`:

```batch
uvicorn app.main:app --reload
```

Espera a que aparezca en la terminal el siguiente mensaje de confirmación:

```batch
INFO:     Application startup complete.
```

Accede al puerto local [8000](http://127.0.0.1:8000/).

Debería aparecer el siguiente mensaje:

```JSON
{"message":"API de reconocimiento de dígitos funcionando 🚀"}
```

Accede al puerto [/docs](http://127.0.0.1:8000/docs).

Haz _click_ en el desplegable "POST /predict".

Haz _click_ en el botón "Try it out".

Selecciona un archivo de imagen. Puedes utilizar las imágenes de prueba en la carpeta de este proyecto [/images](./images) o utilizar imágenes propias en formato `.png` o `.jpg`. Idealmente imagen cuadrada, blanco y negro, con el número centrado. No importa si es grande (el código la redimensiona a 28x28).

Haz _click_ en el botón "Execute" y observa la respuesta de la `API`.
