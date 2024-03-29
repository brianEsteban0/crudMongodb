from pymongo import MongoClient

link = "mongodb://localhost:27017/"

database = "dataset"
collection = "personas"

def coneccionBD():
    client = MongoClient(link)
    db = client[database]
    collection = db[collection]
    return collection


def crearDocumento(data):
    collection = coneccionBD()
    collection.insert_one(data)
    print("Comando ejecutado Correctamente!")


def buscarDocumentos():
    collection = coneccionBD()
    documents = collection.find({})
    for doc in documents:
        print(doc)

def actualizarDocumento(id, data):
    collection = coneccionBD()
    collection.update_one({"_id": id}, data)
    print("Comando ejecutado Correctamente!")


def eliminarDocumento(id):
    collection = coneccionBD()
    collection.delete_one({"_id": id})
    print("Comando ejecutado Correctamente!")


while True:
    print("\nCRUD mongoDB")
    print("1. Crear Documento")
    print("2. Mostrar Documentos de la Colección")
    print("3. Actualizar Documento")
    print("4. Eliminar Documento")
    print("5. Salir")
    i = input("Ingresar opción:")

    if i == '1':
        materia = input("Ingresar Materia: ")
        nota = int(input("Ingresar Nota: "))
        data = {"materia": materia, "nota": nota}
        crearDocumento(data)
    elif i == '2':
        buscarDocumentos()
    elif i == '3':
        id = input("Ingrese el Id: ")
        update_data = {"$set": {}} 
        update_data["$set"]["name"] = input("Enter new name: ")
        update_data["$set"]["nota"] = int(input("Enter new name: "))
        actualizarDocumento(id, update_data)
    elif i == '4':
        id= input("Ingrese el id del documento a eliminar")
        eliminarDocumento(id)
    elif i == '5':
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
