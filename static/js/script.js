 // Get the check-in date input element and the book button
const checkInDate = document.getElementById("id_checkin");
const bookButton = document.getElementById("book");
if(checkInDate && bookButton){
    checkInDate.addEventListener("change", checkDate);
    function checkDate() {
    // Add an event listener to the check-in date input that runs the checkDate function every time the input's value changes
    checkInDate.addEventListener("change", checkDate);
    // Define the checkDate function
    function checkDate() {
    // Get the current date
    const currentDate = new Date();
    // Get the check-in date from the input
    const checkIn = new Date(checkInDate.value);
    // Compare the check-in date to the current date
    if (checkIn < currentDate) {
        // If the check-in date is in the past, disable the book button
        bookButton.disabled = true;
        bookButton.value = "Check-in date is in the past, please correct";
    } else {
        // If the check-in date is in the future, enable the book button
        bookButton.disabled = false;
        bookButton.value = "Book"
    }
    }
}
}

// a go back one page function

$(document).ready(function() {
    $('.btn-back').click(function() {
        window.history.back();
    })
})

function calculateTotalPrice() {
    var checkInDate = new Date(document.getElementById("id_checkin").value);
    var checkOutDate = new Date(document.getElementById("id_checkout").value);
    var housePrice = document.getElementById("price").innerHTML;
    var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    var diffDays = Math.round(Math.abs((checkOutDate.getTime() - checkInDate.getTime())/(oneDay)));
    var totalCost = diffDays * housePrice;
    document.getElementById("total_cost").innerHTML = totalCost;
}

document.getElementById("id_checkin").addEventListener("change", calculateTotalPrice);
document.getElementById("id_checkout").addEventListener("change", calculateTotalPrice);