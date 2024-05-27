/* JAVASCTIPT CODE OM GEGEVENS UIT BUIENRADER TE KRIJGEN */
var xmlhttp = new XMLHttpRequest();	// Een nieuw XMLHttpRequest
xmlhttp.onreadystatechange = function() {// Als het request een respons geeft
	if(this.readyState == 4 && this.status == 200) {// Respons is valide
		var data = JSON.parse(this.responseText);// Parse de JSON data

						//HIERONDER ZET JE CODE OM GEGEVENS UIT DE JSON BESTAND TE HALEN EN AAN ELEMENT TE KOPPELEN
					document.getElementById("temperatuur").innerHTML = data.actual.stationmeasurements[1].temperature;
					document.getElementById("locatie").innerHTML = data.actual.stationmeasurements[1].stationname
					document.getElementById("voorspeling").innerHTML = data.forecast.shortterm.forecast
				}
};

xmlhttp.open("GET", "https://api.buienradar.nl/data/public/2.0/jsonfeed", true);// Zet een verbinding op naar Buienradar
xmlhttp.send();// Verzend het request
