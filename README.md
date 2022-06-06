<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLE-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />

<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Progamación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACIÓN:</td><td>05/06/2022</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">11:30 pm</td>
</tr>
<tr><td colspan="3">INTEGRANTE(s):
<ul>
    <li>Contreras Mamani Claudia Asunción - ccontrerasma@usa.edu.pe</li>
    <li>Cordova Silva Heidi Stephany - hcordovas@unsa.edu.pe</li>
    <li>Llaique Chullunquia Angie Carolina - allaiquec@unsa.edu.pe</li>
    <li>Mamani Cañari Gabriel Antony - gmamanican@unsa.edu.pe</li>
</ul>
</td>
<td>NOTA:</td><td colspan="2"></td>
</<tr>
<tr><td colspan="6">DOCENTE(s):
<ul>
<li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
</ul>
</td>
</<tr>
</tbody>
</table>

<table>
<theader>
<tr><th>Solución y resultados</th></tr>
</theader>
<tbody >
<tr><td>I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS
    <ul>
        <li>Los ejercicios se realizaron en un ambiente virtual. Siga los siguientes pasos para poder ejecutar los ejercicios: 
            <ol>
                <li>Clonar el repositorio</li>
                <li>Acceder al repositorio <code>cd Pweb2-lab04-grupal</code></li>
                <li>Crear un ambiente virtual en el repositorio con <code>virtualenv -p python3 .</code></li>
                <li>Active el ambiente virtual con <code>./bin/activate</code> en linux y <code>./Scripts/activate</code> en Windows</li>
                <li>Instalar las dependencias con <code>pip install -r requirements.txt</code></li>
                <li>Ya podrá ejecutar los ejercicios con python</li>
            </ol>
        </li>
        <li>
            Resultados Ejercicio 2a<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172094959-3c55622b-d1cf-4389-9637-f4d8e55d34a7.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2b<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172095028-6f9d8265-1cfe-458a-8950-9ede5db890b2.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2c<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172095690-aefc6167-6bc2-4c8f-9560-11d663d14f90.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2d<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172095131-f923240d-e867-476b-8b72-bf730a01d62c.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2e<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172095279-9b6e5e4b-e6a7-492c-a740-cb5b61e454d1.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2f<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172095246-869fed6b-d4db-4f0c-b648-e313a353e9cb.png" width=300/>
        </li>
        <li>
            Resultados Ejercicio 2g<br/>
            <image src="https://user-images.githubusercontent.com/85516522/172094305-d5f27e82-151f-42b1-8a85-0030e5dfee7a.png" width=300/>
        </li>
    </ul>
<tr><td>II. SOLUCIÓN DEL CUESTIONARIO
    <ul>
        <li>
            ¿Qué son los archivos *.pyc?
            <ul>
                <li>pyc es una versión compilada, o "ya interpretado" de un modulo. Los archivos PYC son más rápidos y mejoran el tiempo de ejecución.Los archivos PYC contienen principalmente bytecode de Python</li>
                <li>Son archivos ejecutables, que contienen un codigo de bytes compilado para un programa escrito en python</li>
                <li>Aquellos archivos que tienen una extensión “pyc”  son los que contienen la versión ya interpretada, el resultado de compilar código. Es decir que después de la primera ejecución en Python, se utilizará el .pyc compilado al importar. Con los archivos pyc y py guardados, mientras que el código fuente del módulo no cambie, no tiene que volver a compilar las instrucciones. Con ello, ayuda a acelerar y mejorar el tiempo de ejecución.</li>
            </ul>  
        </li>
        <li>
            ¿Para qué sirve el directorio pycache?
            <ul>
                <li>Python registra y almacena  las versiones compiladas en un directorio, pycache es el directorio que  sirve para ello,  para contener los archivos pyc, estos comparten el mismo nombre con los archivos .py en su carpeta de proyecto. Su mayor aporte está en brindar una ejecución más rápida, sin embargo el directorio puede ser ignorado simplemente</li>
                <li>Sirve para almacenar los numerosos archivos con la extension .pyc  que se crean al ejecutar el codigo de Python</li>
                <li>pycache sirve como un directorio que contiene archivos de caché de bytecode que son generados automáticamente por python, es decir, python compilado.</li>
            </ul>
        </li>
        <li>
            ¿Cuáles son los usos y lo que representa el subguión en Python?
            <ul>
                <li>Depende de la ubicación. Por ejemplo. Con solo un subguion( name), indicaría un uso interno y que no debería ser accedida desde fuera de la clase. Con doble(_name) indicaría un atributo privado.</li>
                <li>Uno de los usos es para codificar los constructores, 2 guiones bajos al inicio y al final</li>
                <li>El guión bajo en python se usa principalmente como modificador de acceso, también se utiliza para declarar los constructores
Usos Almacenando el ultimo valor de interprete,En la nomenclatura defunciones y variables, indicando una importancia especifica,Ignorar valores,Para internacionalizar cadenas,Facilitando la legibilidad.</li>
            </ul>
        </li>
    </ul>
    </td></tr>
<tr><td>III. CONCLUSIONES
    <ul>
        <li>En este trabajo hemos repasado las características más importantes de Python: los tipos de datos, funciones integradas, librerías etc, que nos ayudaron a complementar nuestros aprendizajes</li>
        <li>Gracias a la actividad se pudo trabajar conceptos importantes acerca del lenguaje de programación Python como listas, ciclos, condicionales, entre otras. También la información proporcionada por el docente junto con los ejercicios resueltos fueron útiles para la resolución del trabajo.</li>
        <li>En el presente laboratorio pudimos aprender a usar de manera correcta un virtual enviroment para poder gestionar dependencias locales y no globales mediante pip. Conocimos librerías como pygame que es muy útil para crear videojuegos rápidos con python y de manera breve</li>
        <li>Python demostró ser un lenguaje agradable que nos permite enforcarnos más en la lógica de programación que en ciertas reglas de sintaxis</li>
    </ul>
    </td></tr>
</tbody>
</table>


<table>
<theader>
<tr><th>RETROALIMENTACIÓN GENERAL
    </th></tr>
</theader>
<tbody>
<tr><td>
    <pre>                                                                                          </pre>
    <pre>                                                                                          </pre>
    </td></tr>
</tbody>
</table>
</div>    
<p><b>REFERENCIAS Y BIBLIOGRAFÍA</b></p>
<ul>
    <li>https://www.w3schools.com/python/python_reference.asp</li>
    <li>https://docs.python.org/3/tutorial/</li>
    <li>https://www.geeksforgeeks.org/python-map-function/</li>
    <li>https://www.freecodecamp.org/espanol/news/expresiones-lambda-en-python/#:~:text=Las%20expresiones%20lambda%20en%20Python,con%20la%20palabra%20clave%20def%20</li>
    <li>https://www.analyticslane.com/2019/09/23/listas-por-comprension-en-python/</li>
</ul>
