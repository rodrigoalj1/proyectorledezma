import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "gC7wGlxvqyG8XG5bWQ7xQxhrAvxFchI4"
while True:
    orig = input("Ciudad de origen: ")
    if orig == "Salir" or orig =="S" or orig =="s":
        break
    dest = input("Ciudad de destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from" :orig, "to": dest})
    print("URL: " + (url))
    json_data = requests.get (url). json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) +" = A successful route call. \n")
        print("=================================================")

        print("Direcciones viaje:" + (orig) + " a " + (dest))
        print("Distancia en Kilometros:" + str(" {:.1f}".format((json_data["route"]["distance"]) * 1.61)))
        print("Duración del viaje:" + (json_data["route"]["formattedTime"]))

        print("=================================================")
    for each in json_data["route"] ["legs"] [0] ["maneuvers"]:
        print((each["narrative"]) +"("+ str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=======================\n")
