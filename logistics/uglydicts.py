# -*- coding: utf-8 -*-

# Diccionarios feos para realizar migración de tablas


# Para homogeneizar spreadsheets O/D con Big Query:
gsheets_bquery = {'Alimentos Existentes (por favor, separa tu respuesta por comas)': 'AlimentosExistentes',
    'Alimentos Faltantes (por favor, separa tu respuesta por comas)': 'AlimentosFaltantes',
    'Artículos Urgentes (por favor, separa tu respuesta por comas)': 'ArtculosUrgentes',
    'Calle': 'Calle',
    'Colonia': 'Colonia',
    'Delegación o municipio': 'Delegacinomunicipio',
    'En operación': 'operando',
    'Estado': 'Estado',
    'Herramientas Existentes (por favor, separa tu respuesta por comas)': 'HerramientasExistentes',
    'Herramientas Faltantes (por favor, separa tu respuesta por comas)': 'HerramientasFaltantes',
    'Horario de atención': 'Horariodeatencin',
    'Timestamp': 'Marcatemporal',
    'Medicamentos Existentes(por favor, separa tu respuesta por comas)': 'MedicamentosExistentes',
    'Medicamentos Faltantes (por favor, separa tu respuesta por comas)': 'MedicamentosFaltantes',
    'Nombre del centro': 'Nombredelcentro',
    'Nombre del contacto (esta información no se ha pública)': 'Nombredelcontacto',
    'Número (aproximado al menos)': 'Nmero',
    'Otros Artículos que Necesitan (por favor, separa tu respuesta por comas)': 'OtrosArtculosqueNecesitan',
    'Se requiere voluntarios': 'Serequierevoluntarios',
    'Teléfono (esta información no se hará pública)': 'Telfono',
    'Verificado': 'Verificado'
    }


# Para crear nombres de columnas más utilizables:
bquery_clean = {'int64_field_0': 'id_pet',
    'AlimentosExistentes': 'alimentos',
    'AlimentosFaltantes': 'alimentos_f',
    'ArtculosUrgentes': 'articulos_f',
    'Calle': 'dir_calle',
    'Colonia': 'dir_col',
    'Delegacinomunicipio': 'dir_del',
    'EspecialistasExistentesseparaporcomas': 'especialistas',
    'EspecialistasFaltantesseparaporcomas': 'especialistas_f',
    'Estado': 'estado',
    'HerramientasExistentes': 'herramientas',
    'HerramientasFaltantes': 'herramientas_f',
    'Horariodeatencin': 'horario',
    'Marcatemporal': 'timestamp',
    'MedicamentosExistentes': 'medicamentos',
    'MedicamentosFaltantes': 'medicamentos_f',
    'Nombredelcentro': 'centro_nom',
    'Nombredelcontacto': 'contacto_nom',
    'Nmero': 'dir_num',
    'OtrosArtculosqueNecesitan': 'articulos',
    'Serequierevoluntarios': 'voluntarios',
    'Telfono': 'dir_tel',
    'TelfonoAcopio': 'centro_tel',
    'Verificado': 'verificado',
    'latitud': 'lat_long'
    }


# Índice de las columnas a checar para aplicar clean_list
check_list = ['alimentos', 
             'alimentos_f', 
             'articulos',
             'especialistas',
             'especialistas_f',
             'herramientas',
             'herramientas_f',
             'medicamentos',
             'medicamentos_f',
             'voluntarios'
             ]


# Traduce valores. Ahorita sólo tiene a None. Fase 2: corregir typos?
clean_list = {' ': None,
              '0': None, 
              '.': None,
              '-': None,
              'agua y comida':'agua y comida',
              'alimentos y bebidas':'agua y comida',
              'atendido': None,
              'atendidos':None,
              'alimentos enlatados':'enlatados',
              'alimento para bebe':'comida para bebe',
              'alimentos preparados':'comida preparada',
              'alimentos preparados listos para consumo':'comida preparada',
              'alimentos perecederos':'comida preparada',
              'alimentos no perecederos':'enlatados',
              'articulos de limpieza':'articulos de limpieza',
              'ayuda humana':'voluntarios',
              'casi se terminan':None,
              'cero': None,
              'cepillo de dientes':'cepillos de dientes',
              'cepillos de dientes':'cepillos de dientes',
              'comida para bebe':'comida para bebe',
              'comida enlatada':'comida preparada',
              'comida bebe':'comida para bebe',
              'comida perro':'comida para perro',
              'comida de perro':'comida para perro',
              'comida para perro':'comida para perro',
              'comida para perros':'comida para perros',
              'comida preparada':'comida preparada',
              'comida caliente preparada':'comida preparada',
              'comida perecedera':'comida preparada',
              'comida perecedara':'comida perecedara',
              'comida/cena preparada':'comida preparada',
              'coca cola':'bebidas azucaradas',
              'coca-cola':'bebidas azucaradas',
              'coca-colas':'bebidas azucaradas',
              'cubre bocas':'cubrebocas',
              'de todos': 'todo',
              'de todas': 'todo',
              'de todo un poco': None,
              'desabasto': None,
              'esenciales': None,
              'gerber':'comida para bebe',
              'hace falta de todo':'todo',
              'latas':'enlatados',
              'lineas de vida': None,
              'los necesarios': None,
              'muy pocas': None,
              'na': None,
              'n/a': None,
              'np': None,
              'nan': None, 
              'nada': None,
              'ninguno': None,
              'ninguna por el momento':None,
              'ninguna':None,
              'no': None,
              'no.':None,
              'no aplica': None,
              'no aplica por el momento': None,
              'no ahorita': None,
              'no faltan': None,
              'no hay informacion': None,
              'no hay respuesta': None,
              'no estan recibido': None,
              'no estan recibiendo': None,
              'no estan solicitando donaciones': None,
              'no perecederos':'enlatados',
              'no perecederos.':'enlatados',
              'no se estan solicitando donaciones': None,
              'no se': None,
              'no se.':None,
              'no se necesitan': None,
              'no se necesita':None,
              'no tenemos viveres': None,
              'nonguno':None,
              'nunguno':None,
              'pasta dental':'pasta de dientes',
              'pasta de dientes':'pasta de dientes',
              'papel sanitario':'papel higienico',
              'papel de baño':'papel higienico',
              'papel higienico':'papel higienico',
              'papel igienico':'papel higienico',
              'productos de limpieza':'articulos de limpieza',
              'recoleccion de viveres':'voluntarios',
              'recopilando informacion': None,
              'ropa usada':'ropa',
              'si':None,
              'sin respuesta': None,
              'sin info':None,
              'tiendas de campaña':'tiendas de campaña',
              'tienda de campaña':'tiendas de campaña',
              'todo':'todo',
              'toallas femeninas':'toallas femeninas',
              'toallas sanitarias':'toallas femeninas',
              'toallas húmedas':'toallas húmedas',
              'toallas de bebé':'toallas húmedas',
              'toallitas de bebé':'toallas húmedas',
              'toallitas para bebé':'toallas húmedas',
              'todos': 'todo',
              'todas':'todo',
              'tienen': None,
              'varios': None,
              'x': None,
              'ya fue utilizada': None
              }