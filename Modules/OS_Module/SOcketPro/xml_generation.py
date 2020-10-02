import xml.dom.minidom


doc = xml.dom.minidom.Document()

cities = doc.createElement("cities")
cities.setAttribute("total","1")

city = doc.createElement("city")
text = doc.createTextNode("Kurnool")

city.appendChild(text)
cities.appendChild(city)
doc.appendChild(cities)


print(doc.toxml())
print()
print(doc.toprettyxml())
