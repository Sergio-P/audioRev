import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Baje la lista de alumnos de la tarea a evaluar en u-cursos como excel."
        print "Abra el archivo en excel y exportela como csv."
        print "El archivo csv obtenido debe ser pasado como parametro, por ejemplo:"
        print "python alum_from_ucursos.py notas.csv"
    else:
        entries = []
        with open(sys.argv[1]) as f:
            first = True
            for linea in f:
                comps = linea.replace("\"", "").split(",")
                if comps[0].isdigit():
                    rut = comps[3]
                    apellido = comps[1].split(" ")[0]
                    nombre = comps[2].split(" ")[1]
                    entries.append(rut+","+nombre+" "+apellido+"\n")

        with open("alumnos.txt","w") as f:
            for entry in entries:
                f.write(entry)
        print "Guardado."
