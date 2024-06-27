
# Simple Backend Biblioteca USAC

Manual de la utilizacion del backend con el framework Flask



## Authors

- [@JonhAlva](https://github.com/JonhAlva)

#### Para iniciar el funcionamiento de la API ejecutar el archivo `Main.py` 

## Referencia de la API

#### Rutas disponibles:


1.
```http
  http://localhost:4000/cargarLibros
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `/cargarLibros` | `POST` | **Carga los libros en el sistema** |

2.
```http
  http://localhost:4000/verLibros
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `/verLibros` | `GET` | **Muestra los libros registrados** |

3.
```http
  http://localhost:4000/verLibro/<id>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `<id>` | `String` | **Muestra libro basado en ID** |

4.
```http
  http://localhost:4000/libros/<categoria>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `<categoria>` | `String` | **Muestra toda la categoria de libros** |

## Funcionamiento de la API con Postman

**Carga de Libros**
![Carga de Libros](/images/cargarLibros.png)

**Visualización de libros**
![Muestra de Libros](/images/verLibros.png)

**Buscar libro por ID**
![Buscar libro por ID](/images/verLibroPorID.png)

**Buscar libros por categoria**
![Libro por categoria](/images/verLibroPorCategoria.png)


