//Office Popup
document.getElementById("office-divider").style.display ="none";

function openOffice() {
    document.getElementById("office-divider").style.display = "block";
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
}

function closeIPs() {
		document.getElementById("addIPs-divider").style.display ="none";
}

document.getElementById('addIPsButton').addEventListener('click', openIPs);
document.getElementById('cancelIPs').addEventListener('click', closeIPs);