https://github.com/SamuelDauzon/intranetMDS2020

````shell
## Under unix system
# Creating virtual env
python3 -m venv venv_intranet
# Then entering into this venv
source venv_intranet/bin/activate


## OR under Windows
py -m venv venv_intranet
# Then entering into this venv
venv_intranet/bin/activate

# Une fois dans le Venv pour start le serveur 
python manage.py runserver 127.0.0.0:8080

````
