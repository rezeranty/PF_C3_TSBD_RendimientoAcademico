from app_modulos.vista_conf_pagina import configuracion_inicial
from app_modulos.vista_menu_principal import get_opcion_menu_principal
from app_modulos.vista_manejador_paginas import establecer_pagina


def main():
    
    configuracion_inicial()

    pagina = get_opcion_menu_principal()
    establecer_pagina(pagina)


if __name__ == "__main__":
    main()