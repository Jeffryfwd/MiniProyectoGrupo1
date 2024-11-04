# MiniProyectoGrupo
1. sql injection
uso de consultas preparadas: la inyeccion de sql ocurre cuando las entradas de los usuarios se incorporan directamente en las consultas sql. para evitarlo, utiliza consultas preparadas (tambien llamadas consultas parametrizadas), que separan la logica sql de los datos del usuario. esto es crucial si estas construyendo consultas sql dinamicas.
orms: usar un orm (como django orm o sequelize en node.js) puede mitigar sql injection, ya que generan consultas preparadas automaticamente. evita escribir sql sin procesar siempre que sea posible.
ejemplo en django:

python
#
from django.db import connection

# no seguro
def obtener_usuario_inseguro(nombre):
    return connection.cursor().execute(f"SELECT * FROM users WHERE name = '{nombre}'")

# seguro
def obtener_usuario_seguro(nombre):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = %s", [nombre])
        return cursor.fetchall()
2. cross-site scripting (xss)
sanitizacion y validacion de entradas: asegúrate de validar y sanitizar cualquier entrada de usuario antes de mostrarla en el html. esto incluye entradas en formularios, comentarios y cualquier otro contenido generado por el usuario.
uso de plantillas seguras: utiliza motores de plantillas seguros que escapen automaticamente el html, como django templates o ejs en express. esto evita que las etiquetas de script se interpreten y se ejecuten en el navegador del usuario.
ejemplo en django:

html
#
<!-- las plantillas de django escapan automaticamente las variables -->
<p>{{ usuario.comentario }}</p>
ejemplo en express:

javascript

app.get('/comentarios', (req, res) => {
    res.render('comentarios', { comentario: req.body.comentario });
});
librerias de sanitizacion: en express, usa librerias como sanitize-html para limpiar el contenido de entrada.
javascript
#
const sanitizeHtml = require('sanitize-html');
const comentarioSeguro = sanitizeHtml(req.body.comentario);
3. cross-site request forgery (csrf)
proteccion contra csrf en formularios: los ataques csrf funcionan enganando a los usuarios para que envien solicitudes no deseadas en sitios donde estan autenticados. la proteccion csrf asegura que las solicitudes sensibles (como cambios en el perfil o compras) se originen desde el propio sitio de confianza.

django: django tiene csrf habilitado por defecto y utiliza tokens para protegerse de estos ataques. asegúrate de incluir {% csrf_token %} en todos los formularios html y verifica que los tokens se incluyan en los encabezados de las solicitudes ajax.

html
#
<!-- en django -->
<form method="post" action="/example/">
    {% csrf_token %}
    <!-- campos de formulario -->
</form>
express: en express, puedes usar el middleware csurf para agregar proteccion csrf.
javascript
#
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.use(csrfProtection);

app.get('/form', (req, res) => {
    res.render('send', { csrfToken: req.csrfToken() });
});