# Ficha de propuestas de proyecto · Hito H1

**Entrega: domingo 20 de septiembre, 23:59, en la Tarea «H1 · Propuestas de proyecto».**
**Decisión: domingo 27 de septiembre (hito H2).** Sin visto bueno no se sigue adelante.

Hasta **tres propuestas, en orden de preferencia**. La primera tiene que estar completa; la segunda y
la tercera son vuestras alternativas si la primera no pasa la puerta. Las tres tienen las mismas cuatro
comprobaciones.

---

## Cómo se entrega

1. Copiad esta página entera a un fichero `docs/propuestas.md` de vuestro repositorio y rellenadla ahí.
   Es Markdown: las tablas se editan en cualquier editor, y así queda en la historia de _commits_.
2. Marcad las casillas cambiando `[ ]` por `[x]` **solo cuando sea verdad**. Una casilla marcada sin
   evidencia en la tabla de debajo cuenta como no marcada.
3. Haced _commit_ y _push_, y en la Tarea de ALUD pegad **la URL del fichero en GitHub**. Entrega uno,
   cuenta por los dos.
4. El 27 de septiembre tendréis la decisión de cada propuesta en la retroalimentación de la Tarea. La
   aprobada se convierte en vuestro `docs/viabilidad.md`, que es el que se corrige con E1.

---

## Las dos vías

**Vía A · lista curada.** Uno de los doce papers ya comprobados, que están en el capítulo _Lista de
papers_ de este Libro: ResNet, U-Net, YOLO (v1), Vision Transformer, CycleGAN, Grad-CAM, SimCLR,
ejemplos adversarios (FGSM), Word2Vec, Transformer, BERT (solo preentrenamiento) y Neural
Collaborative Filtering. Sabemos que caben en la regla 5/20 y que tienen un aplicativo natural encima.
La ficha se rellena igual, pero es rápido. **Máximo dos parejas por paper**, por orden de entrega.

**Vía B · propuesta propia.** Cualquier paper o caso industrial que os interese, si la ficha pasa las
cuatro comprobaciones. Da más trabajo al principio, y ese trabajo de acotar es justo lo que venís a
aprender aquí.

---

## Pareja

|                                     |                                                                       |
| ----------------------------------- | --------------------------------------------------------------------- |
| **Nombres**                         |  Josu Viteri y Gotzon Viteri                                                                      |
| **Repositorio**                     | https://github.com/josuviteri/CLEAR                           |
| **Rol profesional al que apuntáis** | _Machine Learning Engineering, Data Science y MLOps en Research o Producción_ |

---

## Propuesta 1

### Identificación

|                            |                                                                     |
| -------------------------- | ------------------------------------------------------------------- |
| **Paper o referencia**     | _Denoising Diffusion Probabilistic Models (baseline) + High-Resolution Image Synthesis with Latent Diffusion Models y los papers Classifier-Free Guidance (CFG) y GLIDE (extensión)_                                                   |
| **Autores y año**          |  Jonathan Ho, Ajay Jain y Pieter Abbeel   (DDPM) + Robin Rombach, Andreas Blattmann, Dominik Lorenz y Bjorn Ommer (LDM)                                                                |
| **Enlace**                 | https://arxiv.org/abs/2006.11239 (DDPMs) + https://arxiv.org/pdf/2112.10752 (LDM), https://arxiv.org/pdf/2207.12598 (CFG), https://arxiv.org/pdf/2112.10741 (GLIDE)                                        |
| **Vía**                    | B                             |
| **Por qué este y no otro** | _Nos interesa aprender sobre modelos de visión-lenguaje (VLMs) e IA generativa aplicada a la visión por computador, especialmente sobre modelos de difusión, como los Denoising Diffusion Probabilistic Models (DDPM), y su evolución hacia los Latent Diffusion Models (LDM). También nos interesa estudiar cómo la incorporación de embeddings textuales permite condicionar la generación de imágenes. Queremos darle un enfoque investigador y hacer trabajo interesante._ |

### Comprobación 1 · Datos

- [x] Son **públicos y descargables hoy**. Enlace que funciona, no una promesa.
- [x] La licencia permite el uso académico.

|                                       |                                                                |
| ------------------------------------- | -------------------------------------------------------------- |
| **Dataset**                           |        CIFAR-10 y MNIST                                                        |
| **Enlace de descarga**                |      https://www.kaggle.com/competitions/cifar-10/data + https://www.kaggle.com/datasets/hojjatk/mnist-dataset                                                          |
| **Tamaño**                            | 60k imágenes - 752.88 MB (Cifar-10) y/o  60k imágenes 54.95MB (MNIST)                             |
| **Licencia**                          |                                              CC BY 4.0 (Cifar-10), CC BY-SA 3.0 (MNIST)                  |
| **¿Hace falta registro o solicitud?** | _Si, Kaggle_ |

### Comprobación 2 · Especificación

- [x] Hay implementación de referencia, **o bien** el paper especifica la arquitectura lo bastante como
      para implementarla sin adivinar.

|                                                          |                                                                                                               |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **¿Hay código de referencia?**                           | _Sí (https://github.com/hojonathanho/diffusion) DDPM + (https://github.com/compvis/latent-diffusion) LDM_                                                                                            |
| **Si no lo hay, ¿el paper da la arquitectura completa?** | _NA_                                                         |
| **Qué NO especifica el paper (DDPM)**                           | 
- Manejo exacto de los bordes/índices temporales
- Tratamiento del EMA (Exponential Moving Average)
- Padding y resolución de autoatención
- Discretización de log-verosimilitud vs. Muestreo continuo

 **Qué NO especifica el paper (LDM)**                           | 
 - Factor de escala del espacio latente
 - Estrategia exacta de token conditioning nulo para CFG
 - Detalles de entrenamiento en dos etapas

### Comprobación 3 · Cómputo · la regla 5/20

- [en principio si, sería interesante contar con una segunda opinión] Cabe en el presupuesto, **con el plan de recorte escrito**.

|                                                |                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Escala del paper original (DDPM)**                  | _CIFAR-10 completo (50.000 imágenes), 800.000 pasos de optimizador (batch size 128, ~2.048 épocas) en TPU v3-8 durante varios días; U-Net con ~35.7M parámetros._                                                          |
| **Escala del paper original (LDM)**                  | _LAION-400M / OpenImages, cientos de miles de steps en clusters de NVIDIA A100/V100 (semanas de cómputo)._                                                          |
| **Escala que vais a hacer vosotros**           | _Tenemos pensado usar ambos datasets MNIST y CIFAR-10, con el objetivo de comprobar que todo va bien con un dataset más simple (MNIST) antes de ir con CIFAR-10, tanto para el modelo de difusión sin guiado, como para el de extensión con CFG. Por lo que tenemos varios milestones en los que tendríamos un modelo listo para entregar por si nos estancamos en algún punto del desarrollo o no da más tiempo y es necesario desarrollar la GUI o el documento tex. 1. Fase de validación (MNIST): 60.000 imágenes $1\times 28\times 28$ (padded a $32\times 32$), U-Net reducida (~1.5M parámetros: canales base 32 en vez de 128, sin self-attention pesada), ~20 epochs. 2. Fase de extensión (CIFAR-10): 50.000 imágenes $3\times 32\times 32$, U-Net compacta (~4M a 7M parámetros: canales base 64, atención solo a resolución $16\times 16$), reduciendo a 60.000 steps (~150 épocas con batch 128) usando el encoder CLIP con weights congelados (clip-vit-base-patch32) para la extensión de guiar la generación con texto sin entrenar pesos del lenguaje._                                                                       |
| **Tiempo estimado del entrenamiento completo** | _Esperamos completar el entrenamiento de demostración en colab para MNIST en 10 minutos (~10 epochs) y el extendido de forma local en 10 minutos (~30 epochs). Respecto a CIFAR-10, el sanity check en colab en 30/45 minutos (~65 epochs), y el extendido de forma local en 3.5 a 5 hora (~380 epochs). Para ejecutar en inferencia no esperamos tener problemas (varios steps por segundo), ya que es viable tanto en colab mediante scripting en forma de demo al terminar el sanity check, como usando nuestro hardware como servidor para la GUI._                                            |
| **Qué se pierde al recortar**                  | _Se espera perder calidad y que los fondos no sean muy detallados._ |
| **Hardware que vais a usar**                   | _Usaremos Google Colab (GPU T4) para la demo en forma de sanity check, con el objetivo de demostrar que los scripts de entrenamiento funcionan y GPUs locales para desarrollo, con el objetivo de extender el tiempo de entrenamiento, sin llegar a replicar el tiempo de cómputo original de los papers (NVIDIA RTX 3060 y 5070 12GB)._                                                                                |

### Comprobación 4 · Aplicativo

- [ ] Hay una capa de servicio natural encima de la replicación.

|                                |                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **Qué construís encima**       | _Hemos elegido los papers DDPM y LDM con el objetivo de empezar replicando los modelos de difusión sin generación guiada, y ampliaremos a la generación guiada si todo va bien (primero DDPM, seguido de conditional routing con CFG y finalmente text encoding y cross-attention con LDM/GLIDE). Pensamos desplegar los modelos en una aplicación web en la que usarlos en inferencia, con o sin generación guiada por texto (Classifier-Free Guidance - CFG) e inspección visual de los cross-attention heatmaps, dependiendo de lo que consigamos abordar._                           |
| **Quién lo usaría y para qué** | _Investigadores o estudiantes que quieran experimentar visualmente con modelos de difusión, el parámetro de guidance (CFG) y qué palabras del prompt activan qué regiones espaciales durante el denoising._ |
| **Qué necesita del modelo**    | _Dependiendo de si el denoising se lleva a cabo con o sin guía (dependiendo de nuestro progreso), hacemos uso de una seed aleatoria o es necesario un prompt que encodear con CLIP. Input: Texto del prompt (ej. "a green frog on a leaf"), seed aleatoria, escala CFG ($w \in [1.0, 10.0]$) y número de pasos de muestreo ($K \in [20, 50]$). Output: Imagen sintética $32\times 32$ (escalada para visualización a $128\times 128$) y mapa de calor de atención por token_                                             |

### Riesgo principal

|                                                    |                                                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Qué es lo que más probablemente va a salir mal** |  _1. Riesgo de infraestructura: Que Colab desconecte la máquina por tiempo límite o inactividad tras 3–4 horas de entrenamiento en CIFAR-10. 2. Riesgo algorítmico: Que la U-Net aprenda a generar imágenes realistas de CIFAR-10 ignorando por completo el embedding de texto (la atención cruzada colapsa a pesos uniformes y el modelo se comporta como un generador incondicional), o que aparezca guidance blowout (imágenes sobresaturadas y con ruido de alta frecuencia al subir el peso de CFG)._                                                                                            |
| **Qué haríais si pasa**                            | _1. Frente a desconexiones: El bucle guardará checkpoints cada X steps en Google Drive (model_state, optimizer_state, step_idx), aunque tenemos pensado usar nuestro hardware en la medida de lo posible, excepto para las demostraciones necesarias. Si la sesión muere, reanudamos en una máquina nueva sin perder cómputo previo. 2. Frente al ignorado del texto (falta de alineación semántica): Si en 20.000 steps el mapa de atención cruzada sigue plano o la imagen no responde al prompt, pasaremos a usar MNIST con dígitos como texto ("the digit seven", etc.). Al tener mucha menos entropía visual que CIFAR-10, esperamos que la atención converja antes._ |

### Visto bueno del profesor (H2) · no rellenar

|                 |                                            |
| --------------- | ------------------------------------------ |
| **Decisión**    | Aprobado / Aprobado con recorte / Devuelto |
| **Condiciones** |                                            |

---

## Propuesta 2 (alternativa)

### Identificación

|                            |                                                                     |
| -------------------------- | ------------------------------------------------------------------- |
| **Paper o referencia**     | _Título completo_                                                   |
| **Autores y año**          |                                                                     |
| **Enlace**                 | _arXiv, DOI o web del paper_                                        |
| **Vía**                    | A (lista curada) / B (propuesta propia)                             |
| **Por qué este y no otro** | _Dos líneas. Idealmente conectado con el rol profesional de arriba_ |

### Comprobación 1 · Datos

- [ ] Son **públicos y descargables hoy**. Enlace que funciona, no una promesa.
- [ ] La licencia permite el uso académico.

|                                       |                                                                |
| ------------------------------------- | -------------------------------------------------------------- |
| **Dataset**                           |                                                                |
| **Enlace de descarga**                |                                                                |
| **Tamaño**                            | _En MB/GB y en número de ejemplos_                             |
| **Licencia**                          |                                                                |
| **¿Hace falta registro o solicitud?** | _Si la respuesta es «hay que pedir acceso y tardan», es un no_ |

### Comprobación 2 · Especificación

- [ ] Hay implementación de referencia, **o bien** el paper especifica la arquitectura lo bastante como
      para implementarla sin adivinar.

|                                                          |                                                                                                               |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **¿Hay código de referencia?**                           | _Sí (enlace) / No_                                                                                            |
| **Si no lo hay, ¿el paper da la arquitectura completa?** | _Capas, dimensiones, función de pérdida, optimizador_                                                         |
| **Qué NO especifica el paper**                           | _Lo importante. Si la lista está vacía, no habéis leído el paper con suficiente atención: siempre falta algo_ |

### Comprobación 3 · Cómputo · la regla 5/20

- [ ] Cabe en el presupuesto, **con el plan de recorte escrito**.

|                                                |                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Escala del paper original**                  | _Dataset completo, N épocas, qué hardware, cuánto tardó_                                                          |
| **Escala que vais a hacer vosotros**           | _Subset de N, M épocas, modelo reducido a…_                                                                       |
| **Tiempo estimado del entrenamiento completo** | _En minutos, en la máquina que vayáis a usar, y cómo lo habéis medido_                                            |
| **Qué se pierde al recortar**                  | _La respuesta honesta. «La métrica bajará de 0.72 a algo en torno a 0.6» es una buena respuesta; «nada» no lo es_ |
| **Hardware que vais a usar**                   | _Portátil / Colab gratuito / otro_                                                                                |

### Comprobación 4 · Aplicativo

- [ ] Hay una capa de servicio natural encima de la replicación.

|                                |                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **Qué construís encima**       | _Un buscador, un detector en vídeo, una API, un panel…_                           |
| **Quién lo usaría y para qué** | _Una frase. Si no se os ocurre, el proyecto no cumple el objetivo del aplicativo_ |
| **Qué necesita del modelo**    | _Entrada, salida, latencia aceptable_                                             |

### Riesgo principal

|                                                    |                                                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Qué es lo que más probablemente va a salir mal** |                                                                                              |
| **Qué haríais si pasa**                            | _Útil: «si no converge, reducimos a MNIST y lo declaramos». Inútil: «nada, está controlado»_ |

### Visto bueno del profesor (H2) · no rellenar

|                 |                                            |
| --------------- | ------------------------------------------ |
| **Decisión**    | Aprobado / Aprobado con recorte / Devuelto |
| **Condiciones** |                                            |

---

## Propuesta 3 (alternativa)

### Identificación

|                            |                                                                     |
| -------------------------- | ------------------------------------------------------------------- |
| **Paper o referencia**     | _Título completo_                                                   |
| **Autores y año**          |                                                                     |
| **Enlace**                 | _arXiv, DOI o web del paper_                                        |
| **Vía**                    | A (lista curada) / B (propuesta propia)                             |
| **Por qué este y no otro** | _Dos líneas. Idealmente conectado con el rol profesional de arriba_ |

### Comprobación 1 · Datos

- [ ] Son **públicos y descargables hoy**. Enlace que funciona, no una promesa.
- [ ] La licencia permite el uso académico.

|                                       |                                                                |
| ------------------------------------- | -------------------------------------------------------------- |
| **Dataset**                           |                                                                |
| **Enlace de descarga**                |                                                                |
| **Tamaño**                            | _En MB/GB y en número de ejemplos_                             |
| **Licencia**                          |                                                                |
| **¿Hace falta registro o solicitud?** | _Si la respuesta es «hay que pedir acceso y tardan», es un no_ |

### Comprobación 2 · Especificación

- [ ] Hay implementación de referencia, **o bien** el paper especifica la arquitectura lo bastante como
      para implementarla sin adivinar.

|                                                          |                                                                                                               |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **¿Hay código de referencia?**                           | _Sí (enlace) / No_                                                                                            |
| **Si no lo hay, ¿el paper da la arquitectura completa?** | _Capas, dimensiones, función de pérdida, optimizador_                                                         |
| **Qué NO especifica el paper**                           | _Lo importante. Si la lista está vacía, no habéis leído el paper con suficiente atención: siempre falta algo_ |

### Comprobación 3 · Cómputo · la regla 5/20

- [ ] Cabe en el presupuesto, **con el plan de recorte escrito**.

|                                                |                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Escala del paper original**                  | _Dataset completo, N épocas, qué hardware, cuánto tardó_                                                          |
| **Escala que vais a hacer vosotros**           | _Subset de N, M épocas, modelo reducido a…_                                                                       |
| **Tiempo estimado del entrenamiento completo** | _En minutos, en la máquina que vayáis a usar, y cómo lo habéis medido_                                            |
| **Qué se pierde al recortar**                  | _La respuesta honesta. «La métrica bajará de 0.72 a algo en torno a 0.6» es una buena respuesta; «nada» no lo es_ |
| **Hardware que vais a usar**                   | _Portátil / Colab gratuito / otro_                                                                                |

### Comprobación 4 · Aplicativo

- [ ] Hay una capa de servicio natural encima de la replicación.

|                                |                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **Qué construís encima**       | _Un buscador, un detector en vídeo, una API, un panel…_                           |
| **Quién lo usaría y para qué** | _Una frase. Si no se os ocurre, el proyecto no cumple el objetivo del aplicativo_ |
| **Qué necesita del modelo**    | _Entrada, salida, latencia aceptable_                                             |

### Riesgo principal

|                                                    |                                                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Qué es lo que más probablemente va a salir mal** |                                                                                              |
| **Qué haríais si pasa**                            | _Útil: «si no converge, reducimos a MNIST y lo declaramos». Inútil: «nada, está controlado»_ |

### Visto bueno del profesor (H2) · no rellenar

|                 |                                            |
| --------------- | ------------------------------------------ |
| **Decisión**    | Aprobado / Aprobado con recorte / Devuelto |
| **Condiciones** |                                            |
