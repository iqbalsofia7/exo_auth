import django
django.setup()

from authapp.seed import run_authapp

if __name__== '__main__':
    run_authapp()
