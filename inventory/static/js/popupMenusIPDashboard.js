//Office Popup
document.getElementById("office-divider").style.display ="none";

function openOffice() {
    document.getElementById("office-divider").style.display = "block";
<<<<<<< HEAD
=======
    document.getElementById("addIPs-divider").style.display = "none";
    document.getElementById("hostname-divider").style.display = "none";
>>>>>>> f09eebe18480ab9d1bc6b48db82a67e538226920
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
<<<<<<< HEAD
=======

    document.getElementById("addIPs-divider").style.display = "none";
    document.getElementById("office-divider").style.display = "none";
>>>>>>> f09eebe18480ab9d1bc6b48db82a67e538226920
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
<<<<<<< HEAD
=======
    document.getElementById("hostname-divider").style.display = "none";
    document.getElementById("office-divider").style.display = "none";
>>>>>>> f09eebe18480ab9d1bc6b48db82a67e538226920
}

function closeIPs() {
		document.getElementById("addIPs-divider").style.display ="none";
}

document.getElementById('addIPsButton').addEventListener('click', openIPs);
document.getElementById('cancelIPs').addEventListener('click', closeIPs);