document.getElementById("genipv6").addEventListener("click", function() {
    const hexVals = ['0', '1','2', '3', '4', '5', '6', '7','8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    var interfaceID = "::"
    for(var i = 0; i < hexVals.length; i++) {
        let rand = getRandomInt(hexVals.length)
        let ch = hexVals[rand]
        interfaceID += ch

        if (i > 0 && i < 15  && (i + 1) % 4 == 0) {
            interfaceID += ':'
        }
    }

    document.getElementById("id_genipv6").value = interfaceID;

    function getRandomInt(max) {
        return Math.floor(Math.random() * max);
    }
  });

//Office Popup
document.getElementById("office-divider").style.display ="none";

function openOffice() {
    document.getElementById("office-divider").style.display = "block";
    document.getElementById("addIPs-divider").style.display = "none";
    document.getElementById("hostname-divider").style.display = "none";
}

function closeOffice() {
    
	document.getElementById("office-divider").style.display ="none";
}

document.getElementById('officeButton').addEventListener('click', openOffice);
document.getElementById('cancelOffice').addEventListener('click', closeOffice);


//Hostname Popup
document.getElementById("hostname-divider").style.display ="none";

function openHostname() {
    document.getElementById("hostname-divider").style.display = "block";

    document.getElementById("addIPs-divider").style.display = "none";
    document.getElementById("office-divider").style.display = "none";
}

function closeHostname() {
    
	document.getElementById("hostname-divider").style.display ="none";
}

document.getElementById('hostnameButton').addEventListener('click', openHostname);
document.getElementById('cancelHost').addEventListener('click', closeHostname);


//Add IPs Popup
document.getElementById("addIPs-divider").style.display ="none";

function openIPs() {
    document.getElementById("addIPs-divider").style.display = "block";
    document.getElementById("hostname-divider").style.display = "none";
    document.getElementById("office-divider").style.display = "none";
}

function closeIPs() {
		document.getElementById("addIPs-divider").style.display ="none";
}

document.getElementById('addIPsButton').addEventListener('click', openIPs);
document.getElementById('cancelIPs').addEventListener('click', closeIPs);