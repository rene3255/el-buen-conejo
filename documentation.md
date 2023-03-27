El buen conejo

Preliminary table list

Producers
Rabbits
Farms
Interest Sites
Videos
Clients


Epic story

Desde hace dos años me convertí en granjero urbano de conejos. Veamos, cuando me refiero a la frase “granjero urbano” es porque la granja se ecuentra dentro de la mancha urbana por lo que esa actividad representa un micro-negocio, mejor  nano-negocio. Sin embargo después de dos años es un hobbie que sólo produce carne de conejo para el sustento familiar, sin representar esa producción un indicador sobresaliente, quiero decir, económicamente no es un indicador representativo.

Por otra parte, en el estado de Colima, la producción de conejo sólo se conoce mediante las redes sociales, principalmente Facebook, y no se tiene conocimiento de una fuente de datos que informe sobre el inventario estatal o municipal del sector cunicola.

Aunado a lo anterior, es cierto que no se cuenta con una asociación o consejo de la crianza de conejo o gallinas en el estado cuantimás a nivel municipal.


Keyword
Mating.- Empadre o monta programada entre la hembra reproductora y el semental.
Granja urbana
Cunicola
Nano-negocio


Concepts

Mating
When does become receptive to mating, they will usually show signs of being in heat. 


User Stories

Producer
Como productor quiero llevar el control de la crianza de conejos para saber con precisión con que stock de animales cuento.

Como productor quiero un expediente por coneja reproductora para determinar la prolificidad y productividad de la coneja.

Como productor quiero publicar videos (máximo de 2 minutos) para dar a conocer la crianza. Así, posicionarme en el mercado.

Como productor quiero conocer el padrón de criadores de conejos para conocer el tamaño del
 gremio en la entidad.

Como productor  quiero comentar las publicaciones de los granjeros para retroalimentar las mejores prácticas de cada uno de los granjeros y porsupuesto felicitarlos.

Como productor quiero contar con un reporte dentro de un periodo de la productividad de la granja.


Administrator
Como Administrador soy el único que autorizo el registro de productores para controlar quienes son aptos para ser miembros del buen conejo.

Como administrador quiero registrarse sólo con mi correo electrónico y mi nombre para poder ver algunas funcionalidades de la app  ccpcc. 

Como usuario decido si quiero convertirme en productor por lo que quiero contar con una funcionalidad para solicitar mi inscripción como productor. 

 








Client

Como cliente deseo ver las granjas que venden conejos para tener la posibilidad de comprar la mejor opción.

Como cliente quiero conocer los mejores precios por kilogramo de carne de conejo para facilitarme la decisión de compra.

Como cliente deseo ver  los próximos eventos  e información de lo que se trata.

Como cliente quiero enviarle un mensaje al productor y poder llegar a un acuerdo de compra-venta.

Como cliente quiero poder convertirme en un momento dado en productor de conejos.


https://www.cdrf.co/

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
I belive that we can add a column into the producer profile model. This column must be a boolean field to check where the producer confirm he or she wants to be a producer. At the end of the day, the booelan field gonna run as a indicator in case the producer can add cage or any information.

## 20 Monday  Feb
Last week was really nutritive I learned about Model Managers and Validators. Also I finished the cage model and since now to forward I'm going to build the rabbits model. The CRUD is the main goal for this week.

## 28 Tue Feb
Into the period 21 to 28 feb the project advances consisted databases model rabbit.Some doubts arises from recursive fields between rabbits and mothers rabbits, same for bucks and rabbits.

## 03 Fri Mar
Was a frustrated day because my partner get off from the ship team. He said  
that his scholar agenda was shrinked. What a shame!

Well, the last two days were full of learning. Let me explain, I hadn´t find how to resolve an error in the class AddRabbitForm. particularly the Cage field, its ModelChoiceField and each time I filter the cage by a producer or user authenticated it depicted all table content.
At the end of the last two days the bug was fixed and the knowledgement was super.
## 05 Sun Mar
Yesterday I solved through signals the issue of saving the rabbit entered into the cage field called "rabbits_number".
So far, I'll be working in the feature to pass automatically the rabbit with status "Buck" or "Does".
# 07 Tue Mar
Running the Rabbit template I notice that the observations field is not required when it is created. So I decided to get of from de model.

# 08 Wed Mar
Was cumbersome day because I couldn't find the solution bad at end o the day I got the solution. I added two boolean fields to Rabbit model. Its function is to switch the status of the rabbit when is assigned as Doe.

# 23 Thu Mar

I got and error when I tried to run out a unnitest Mating module. Now, I'm going to clear all migrations and drop an create database.
Eureka! I find the solution, the error was in the model rabbit concretly field Sex. It is an obligatory field, so I setting in the query sentences. 
## Scripts
python3 manage.py runscript load_states
TRUNCATE TABLE resources_state RESTART IDENTITY CASCADE;
\COPY farms_producerprofile to 'produces.csv' csv header

SELECT cage_title, count(*) FROM cage_cage INNER JOIN rabbit_rabbit ON cage_cage.id = rabbit_rabbit.cage_id group by cage_title;

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

{% for item in items %}
    {% ifchanged %}
        {% if forloop.first %}
            <p>This is the first item in the list!</p>
        {% else %}
            <p>This is a new item in the list!</p>
        {% endif %}
    {% endifchanged %}
    <p>{{ item.name }}</p>
{% endfor %}