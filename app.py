import requests
import web
import json

urls = ('/index', 'Index')

class Index(object):
	def POST(self):
		data = web.input()
		data = data["feature"]

		key = "40b7e550-a13e-11eb-bf35-a5186e22f517e4559e0a-562f-4395-b5ad-ae2b39d21c02"
		url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

		response = requests.get(url, params={ "data" : data })

		if response.ok:
			responseData = response.json()
			topMatch = responseData[0]
			label = topMatch["class_name"]

			if label == "reptil":
				titulo = "reptil"
				resultado = "La característica enviada describe a un reptil."
				status = 200
			elif label == "mamifero":
				titulo = "mamifero"
				resultado = "La característica enviada describe a un mamífero."
				status = 200
			else:
				titulo = "error"
				resultado = "No pudimos interpretar la información enviada, intenta de nuevo."
				status = 404
		else:
			response.raise_for_status()
			
		datos = {
			titulo : []
		}

		result = {}
		result["resultado"] = resultado
		result["status"] = status
		datos[titulo].append(result)
		return json.dumps(datos)

if __name__ == "__main__":
   app = web.application(urls, globals()) 
   app.run()