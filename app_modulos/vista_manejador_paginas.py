from app_modulos.vista_pagina_inicio import pagina_inicio
from app_modulos.vista_pagina_estadisticas import pagina_estadisticas
from app_modulos.vista_pagina_predicciones import pagina_predicciones
from app_modulos.vista_pagina_blog import pagina_blog
from app_modulos.vista_pagina_carga_datos import pagina_carga_datos


def establecer_pagina(pagina='Inicio'):
    if pagina == "Inicio":
        pagina_inicio()

    elif pagina == "Estadisticas":
        pagina_estadisticas()

    elif pagina == "Predicciones":
        pagina_predicciones()

    elif pagina == "Blog":
        pagina_blog()

    elif pagina == "Carga Datos":
        pagina_carga_datos()
    
    else:
        pagina_inicio()
    

