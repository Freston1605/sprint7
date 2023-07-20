# SPRINT 7 GRUPO 2

## Tareas por realizar

1. **Crear el modelo de Tareas:** Comienza creando el modelo para representar las tareas pendientes. Define los campos necesarios, como título, descripción, fecha de vencimiento, estado y etiqueta (categoría). No te olvides de establecer una relación con el modelo de usuarios para asociar las tareas con el usuario correspondiente.

2. **Migración y administración de entidades:** Realiza la migración del modelo de tareas para crear la tabla correspondiente en la base de datos. Luego, asegúrate de configurar la administración de entidades de Django para que los superusuarios puedan gestionar las tareas a través del panel de administración.

3. **Sistema de Autenticación y Sesiones:** Implementa el sistema de autenticación de Django para permitir que los usuarios se registren, inicien sesión y cierren sesión en la aplicación. Configura las sesiones de Django para mantener la sesión del usuario durante el tiempo necesario.

4. **Vista de la página principal:** Crea una vista para la página principal donde los usuarios puedan ver una lista de todas las tareas pendientes ordenadas por fecha de vencimiento. Implementa filtros para permitir a los usuarios filtrar las tareas por etiqueta y estado.

5. **Vista de creación de tareas:** Implementa la vista que permitirá a los usuarios autenticados agregar nuevas tareas. Asegúrate de que los usuarios puedan seleccionar una etiqueta de una lista predefinida al crear una nueva tarea.

6. **Vista de detalles de tarea:** Crea una vista para mostrar los detalles de una tarea específica, incluida la información completa de la tarea y un botón para marcarla como completada.

7. **Funcionalidad de edición y eliminación:** Implementa la funcionalidad para editar y eliminar tareas existentes desde la página principal y la página de detalles de tarea.

8. **Modelo de Prioridades:** Ahora, crea el modelo para representar las prioridades de las tareas. Define los campos necesarios y realiza la migración correspondiente.

9. **Vista de edición con prioridad:** Actualiza la vista de edición de tareas para permitir a los usuarios cambiar la prioridad y guardar el valor junto con otros datos del registro.

10. **Visualización de prioridad:** Asegúrate de que la vista de visualización de tareas muestre la prioridad de la tarea de forma destacada.

11. **Columna de prioridad en la vista de listado:** Agrega la columna de prioridad a la tabla de despliegue en la vista de listado de tareas.

12. **Estadísticas de tareas:** Implementa la funcionalidad para que los usuarios puedan ver cuántas tareas tienen pendientes, cuántas han completado, cuántas están en progreso y cuántas han vencido. Puedes agregar esto en la página principal o en una página separada, según tu preferencia de diseño.

Espero que esta lista actualizada te sea de ayuda para desarrollar la aplicación web con todas las funcionalidades requeridas, incluido el sistema de autenticación y sesiones que es esencial para la seguridad y funcionamiento de la aplicación. ¡Mucho éxito en tu desarrollo!
