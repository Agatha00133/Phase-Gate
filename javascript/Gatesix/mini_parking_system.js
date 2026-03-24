let parking = new Array(20).fill(0);

function showMenu() {
    return prompt(
`--- Parking System ---
1. Park automatically
2. Park in a specific slot
3. Remove car
4. Show parking status
5. Exit
Choose an option:`
    );
}

function showStatus() {
    let status = parking.map((slot, index) => `Slot ${index + 1}: ${slot === 0 ? "Empty" : "Occupied"}`).join("\n");
    let available = parking.filter(slot => slot === 0).length;
    alert(`Parking Status:\n${status}\n\nAvailable spaces: ${available}`);
}

function parkAuto() {
    let index = parking.indexOf(0);
    if (index !== -1) {
        parking[index] = 1;
        alert(`Car parked in slot ${index + 1}`);
    } else {
        alert("Parking lot is full!");
    }
    showStatus(); 
}

function parkSpecific() {
    let slot = parseInt(prompt("Enter slot number (1-20):"));
    if (slot >= 1 && slot <= 20) {
        if (parking[slot - 1] === 0) {
            parking[slot - 1] = 1;
            alert(`Car parked in slot ${slot}`);
        } else {
            alert("Slot already occupied!");
        }
    } else {
        alert("Invalid slot number!");
    }
    showStatus(); 
}

function removeCar() {
    let slot = parseInt(prompt("Enter slot number to remove car (1-20):"));
    if (slot >= 1 && slot <= 20) {
        if (parking[slot - 1] === 1) {
            parking[slot - 1] = 0;
            alert("Car removed from slot ${slot}");
        } else {
            alert("Slot is already empty!");
        }
    } else {
        alert("Invalid slot number!");
    }
    showStatus(); 
}


while (true) {
    let choice = showMenu();
    if (choice === "1") {
        parkAuto();
    } else if (choice === "2") {
        parkSpecific();
    } else if (choice === "3") {
        removeCar();
    } else if (choice === "4") {
        showStatus();
    } else if (choice === "5") {
        alert("Exiting system...");
        break;
    } else {
        alert("Invalid choice! Try again.");
    }
}
