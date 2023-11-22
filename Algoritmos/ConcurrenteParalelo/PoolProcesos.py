import multiprocessing

def procesar_dato(dato):
    print(f"Procesando {dato}")

    # Ejemplo de procesamiento de dato
    return dato * dato

if __name__ == '__main__':
    datos = [1, 2, 3, 4, 5]  # Lista de datos a procesar

    # Hago la pool de procesos
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # map va asignando tareas con un dato distinto a cada proceso y va recopilando los datos
        resultados = pool.map(procesar_dato, datos)
        pool.close()  # No se aceptan más tareas
        pool.join()   # Espero a que todos los procesos terminen

    print(f"Resultados: {resultados}")