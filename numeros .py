import pandas as pd

# Diccionario actualizado de LADAS por estado
ladas_por_estado = {
    "Aguascalientes": [449], "Baja California": [664, 686, 653], "Baja California Sur": [612, 624],
    "Campeche": [981, 938], "Chiapas": [961, 962, 963, 964, 967], "Chihuahua": [614, 656, 625, 627, 639],
    "CDMX": [55, 56], "Coahuila": [844, 871, 878, 866], "Colima": [312, 313, 314],
    "Durango": [618, 671, 672], "Estado de México": [722, 729, 721, 715, 563, 712, 720],
    "Guanajuato": [477, 462, 464, 445, 415, 461], "Guerrero": [747, 755, 744, 762, 757],
    "Hidalgo": [771, 774, 775], "Jalisco": [33, 341, 342, 343, 375, 322],
    "Michoacán": [443, 351, 353, 354, 434], "Morelos": [777, 735], "Nayarit": [311, 323],
    "Nuevo León": [81, 826, 821], "Oaxaca": [951, 953, 954, 958], "Puebla": [222, 231, 232, 221, 223, 225, 749],
    "Querétaro": [442, 441, 427], "Quintana Roo": [998, 987, 983, 984],
    "San Luis Potosí": [444, 487], "Sinaloa": [667, 669, 687], "Sonora": [662, 631, 647, 644],
    "Tabasco": [993, 917], "Tamaulipas": [834, 868, 899, 833], "Tlaxcala": [246, 241],
    "Veracruz": [229, 271, 272, 228, 285, 296, 921], "Yucatán": [999, 997, 988], "Zacatecas": [492, 493]
}

def clasificar_numeros(ruta_ods):
    """
    Clasifica los números de teléfono por LADA y los guarda en la misma hoja del archivo ODS.

    Parámetros:
        ruta_ods (str): Ruta del archivo ODS que contiene los números en una columna llamada 'Numero'.
    """
    try:
        # Cargar el archivo ODS
        df = pd.read_excel(ruta_ods, engine="odf")

        # Asegurar que la columna de números es de tipo texto y eliminar espacios
        df['Numero'] = df['Numero'].astype(str).str.strip()

        # Agregar una columna para el estado con valor por defecto "No identificado"
        df['Estado'] = "No identificado"

        # Asignar el estado según la LADA
        for estado, ladas in ladas_por_estado.items():
            df.loc[df['Numero'].str.startswith(tuple(map(str, ladas))), 'Estado'] = estado

        # Agregar prefijo +521 a todos los números
        df['Numero'] = "+521" + df['Numero']

        # Guardar los resultados en la misma hoja del archivo ODS
        resultado_ods = "numeros_clasificados.ods"
        df.to_excel(resultado_ods, sheet_name="Clasificados", engine="odf", index=False)

        print(f"Archivo '{resultado_ods}' generado correctamente en la misma hoja.")
        return resultado_ods

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None

# Uso: Ejecutar con la ruta correcta del archivo ODS
resultado = clasificar_numeros("/home/jonatan/Documentos/prueba1.ods")
if resultado:
    print(f"Archivo generado: {resultado}")
