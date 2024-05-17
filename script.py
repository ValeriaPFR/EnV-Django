# Desafio 1. Creando un entorno virtual para nuestro proyecto Django

#Requerimientos
#Crear entornos virtuales (env) y configura sus condiciones operativas de acuerdo a lo solicitado.
#Respaldar los requerimientos de cada env en un archivo .txt
#

###
mkvirtualenv ferreteria
cd ferreteria
\Users\valer\Envs\ferreteria\Scripts\Activate.ps1  #* Activación alternativa a 'workon ferreteria' 
pip install django ==3.2.4pip 
pip list=> pip-list-env\ferreteria.png
pip freeze > requirements-ferreteria.txt
deactivate

####
mkvirtualenv laesquina
cd laesquina
\Users\valer\Envs\laesquina\Scripts\Activate.ps1 #* Activación alternativa a 'workon laesquina' 
pip install django<3
pip list=> pip-list-env\laesquina.png
pip freeze > requirements-laesquina.txt
deactivate

###
mkvirtualenv onlyflans
cd onlyflans
\Users\valer\Envs\onlyflans\Scripts\Activate.ps1 #* Activación alternativa a 'workon onlyflans' 
pip install django==3.2
pip list=> pip-list-env\onlyflans.png
pip freeze > requirements-onlyflans.txt
deactivate

###
mkvirtualenv prestobar
cd prestobar
\Users\valer\Envs\prestobar\Scripts\Activate.ps1 #* Activación alternativa a 'workon prestobar' 
pip install django==3.2
pip install astral
pip list=> pip-list-env\prestobar.png
pip freeze > requirements-prestobar.txt
deactivate

###
mkvirtualenv taller
cd taller
\Users\valer\Envs\taller\Scripts\Activate.ps1 #* Activación alternativa a 'workon taller' 
pip install django==3.2
pip install pytz==2019.3
pip list=> pip-list-env\taller.png
pip freeze > requirements-taller.txt
deactivate


###################################
mkvirtualenv calendariolunar
cd calendariolunar
\Users\valer\Envs\calendariolunar\Scripts\Activate.ps1 
pip install -r requirements-calendariolunar.txt
pip freeze > requirements-calendariolunar.txt
pip list=> pip-list-env\calendariolunar.png