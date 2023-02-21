
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

## Friday 15 Feb
I attend to a aws live stream to know the fundamentals o ML
Comeback to the project, yesterday a got Producer profile CRUD.  Now I'm working on cage app CRUD.

## Friday 16 Feb

Surged a doubt about the producer profile. Let me put a question on the dialog table, How to know if a user gonna become in a rabbit producer? 
and if it is the case,  he or she is authorized to entry a cage information.
I belive that we can add a column into the producer profile model. This column must be a boolean field to check where the producer confirm he or she wants to
be a producer. At the end of the day, the booelan fields gonna serve as a indicator in case the producer can add cage or whatever information.

## 20 Monday  Feb
Las week was really nutritive I learned about Model Managers and Validators. Alose I finished the cage model and since now to forward I'm going to build the rabbits model. The CRUD is the main goal for this week.


## Scripts
python3 manage.py runscript load_states
TRUNCATE TABLE resources_state RESTART IDENTITY CASCADE;
\COPY farms_producerprofile to 'produces.csv' csv header;
Cuando se guarda listas en el archivo '.env' va así: MY_LIST="['my_string1','my_string2']"

def my_login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return HttpResponseRedirect('/splash/')
        else:
            return function(request, *args, **kw)
    return wrapper

