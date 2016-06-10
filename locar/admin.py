from django.contrib import admin

# Register your models here.
from .models import Categoria
admin.site.register(Categoria)
from .models import Cliente
admin.site.register(Cliente)
from .models import Filme
admin.site.register(Filme)
from .models import Locacao
admin.site.register(Locacao)