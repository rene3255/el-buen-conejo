
# Project annotations

## Friday 10 Feb
After daily meet the development team observed that the username field must be unique.
In that case Rene does the corresponded user model fixes.
It is important to note that I didn't do anything becuase I was waiting some frontend changes done by Harley.

## Mon 13 feb 2023
### daily meet
Se puso a consideración el modelado y maquetado del perfil de los usuarios. 
Se acordó que el el usuario se registra con el username, email y password. Si el usuario quiere ser productor se ciñe a la política de registrarse como productor. 
Para esta semana del 13 al 18 de febrero se estará trabajando en el maquetado del perfil de los productores, el CRUD del perfil de los productores, el CRUD de las jaulas, y el CRUD de los conejos.

### Harley
Reporte de avances realizados la semana del 06 al 10 de febrero:
  6 7 desarrollo de página maker.
  8   desarrollo de pagina detalle rabbit.
  9   sin avances.
  10  terminado primer paso de merge sobre formularios de login, register y rutas privadas.
  11 12 pulido de navbar y primer paso de maquetación de perfil user.
### rene


## Scripts
python3 manage.py runscript load_states
TRUNCATE TABLE resources_state RESTART IDENTITY CASCADE;
\COPY farms_producerprofile to 'produces.csv' csv header;
