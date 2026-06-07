### Paises Visitados ###

paises_visitados = set()
visitas = []
notas = []

while True:
    print("\n=== GESTOR DE PAÍSES VISITADOS ===")
    print("1. Añadir país visitado")
    print("2. Ver paises vistados")
    print("3. Ver notas de un país")
    print("4. Editar nota de un país")
    print("5. Salir")
    
    opcion = input("\nElige una opción: ")
    
    if opcion == "1": # Añadir país visitado
        while True:
            agregar_pais = input("\n¿Qué país visitaste? (escribe cancelar para cancelar agregar un nuevo país): ")
            agregar_pais = agregar_pais.capitalize()
            
            if agregar_pais.lower() == "cancelar":
                break
            elif not agregar_pais:
                print("❌ El nombre del país no puede estar vacío.")
                continue
            elif not agregar_pais.replace(" ", "").isalpha():
                print("❌ El nombre del país solo puede contener letras.")
                continue
            elif agregar_pais in paises_visitados:
                print(f"❌ Ya tienes {agregar_pais} en tu lista.")
                continue
            else:
                paises_visitados.add(agregar_pais)
                print(f"✅ {agregar_pais} añadido correctamente.")
            
            while True:
                año_pais = input("¿En que año?: ")
                if not año_pais:
                    print("❌ El año del país no puede estar vacío.")
                    continue
                elif not año_pais.isnumeric():
                    print("❌ El año tiene que ser un número. Inténtalo de nuevo.")
                    continue
                elif año_pais.isnumeric():
                    visitas.append((agregar_pais, año_pais))
                    print("✅ Año añadido correctamente.")
                    break
                
            añadir_nota = input("¿Quieres añadir una nota? (Enter para saltar): ")
            añadir_nota = añadir_nota.capitalize()
            
            if not añadir_nota:
                notas.append("Sin nota")
                print(f"\n✅ {agregar_pais} añadido sin nota.")
            else:
                notas.append((añadir_nota))
                print("✅ Nota añadida correctamente.")
            
            otro = input("\n¿Quieres añadir otro? (si/no): ")
            if otro.lower() == "si":
                continue
            if otro.lower() == "no":
                break
    
    elif opcion == "2": # Ver paises visitados
        if not paises_visitados:
            print("\n📍 No has visitado ningún país todavía.")
        else:
            print("\n📍 Países visitados")
            for i in range(len(visitas)):
                pais = visitas[i][0]    
                año = visitas[i][1]     
                nota = notas[i]         
                
                if not nota:
                    print(f"- {pais} ({año}) — {nota}.")
                else:
                    print(f"- {pais} ({año}) — {nota}.")
    
    elif opcion == "3": # Ver notas de un país
        if not paises_visitados:
            print("\n📍 No has visitado ningún país todavía.")
        else:
            print("\nDe que país quieres ver las notas")
            for i in range(len(visitas)):
                pais = visitas[i][0]    
                print(f"- {pais}")

            escoger_pais = input("\nEscoge un país: ")
            escoger_pais = escoger_pais.capitalize()
            
            if escoger_pais not in paises_visitados:
                print(f"❌ No has visitado {escoger_pais}.")
            else:
                for i in range(len(visitas)):
                    if visitas[i][0] == escoger_pais:
                        print(f"📝 {visitas[i][0]} ({visitas[i][1]}): {notas[i]}")
            
    elif opcion == "4":  # Editar nota de un país
        if not paises_visitados:
            print("\n📍 No has visitado ningún país todavía.")
        else:
            print("\nPaíses visitados:")
            for pais, año in visitas:
                print(f"- {pais}")
            
            editar_pais = input("\n¿De qué país quieres editar la nota?: ")
            editar_pais = editar_pais.capitalize()
            
            if editar_pais not in paises_visitados:
                print(f"❌ No has visitado {editar_pais}.")
            else:
                # Buscar índice del país
                indice = None
                for i in range(len(visitas)):
                    if visitas[i][0] == editar_pais:
                        indice = i
                        break
                
                # Ver nota actual
                nota_actual = notas[indice]
                print(f"Nota actual: {nota_actual}")
                
                if nota_actual == "Sin nota":
                    print("\n⚠️  Este país no tiene nota.")
                    print("1. Añadir nota")
                    print("2. Cancelar")
                    sub_opcion = input("Elige una opción: ")
                    
                    if sub_opcion == "1":
                        nueva_nota = input("Nueva nota: ")
                        notas[indice] = nueva_nota
                        print("✅ Nota añadida correctamente.")
                else:
                    print("\n1. Reescribir nota")
                    print("2. Eliminar nota")
                    print("3. Cancelar")
                    sub_opcion = input("Elige una opción: ")
                    
                    if sub_opcion == "1":
                        nueva_nota = input("Nueva nota: ")
                        notas[indice] = nueva_nota
                        print("✅ Nota actualizada correctamente.")
                    elif sub_opcion == "2":
                        notas[indice] = "Sin nota"
                        print("✅ Nota eliminada. Este país ahora no tiene nota.")
    
    elif opcion.lower() == "5" or opcion.lower() == "salir":
        print("\n👋 ¡Hasta luego!")
        break
    
    else:
        print("❌ Opción no válida.")