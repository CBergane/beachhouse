 // Get the check-in date input element and the book button
const checkInDate = document.getElementById("id_checkin");
const checkOutDate = document.getElementById("id_checkout");
const bookButton = document.getElementById("book");
if(checkInDate && checkOutDate && bookButton){
    checkInDate.addEventListener("change", checkDates);
    checkOutDate.addEventListener("change", checkDates);
    checkDates();
    function checkDates() {
        // Get the current date
        const currentDate = new Date();
        // Get the check-in date from the input
        const checkIn = new Date(checkInDate.value);
        // Get the check-out date from the input
        const checkOut = new Date(checkOutDate.value);
        // Compare the check-in date to the current date
        if (checkIn < currentDate) {
            // If the check-in date is in the past, disable the book button
            bookButton.disabled = true;
            bookButton.value = "Check-in date is in the past, please correct";
        } else if (checkOut < currentDate) {
            // If the check-out date is in the past, disable the book button
            bookButton.disabled = true;
            bookButton.value = "Check-out date is in the past, please correct";
        } else {
            // If the check-in and check-out dates are in the future, enable the book button
            bookButton.disabled = false;
            bookButton.value = "Book"
        }
    }
}

 

// a go back one page function

$(document).ready(function() {
    $('.btn-back').click(function() {
        window.history.back();
    })
})

const price = document.getElementById("price");
if(price) {
    function calculateTotalPrice() {
        let checkInDate = new Date(document.getElementById("id_checkin").value);
        let checkOutDate = new Date(document.getElementById("id_checkout").value);
        let housePrice = price.innerHTML;
        let oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
        let diffDays = Math.round(Math.abs((checkOutDate.getTime() - checkInDate.getTime())/(oneDay)));
        let totalCost = diffDays * housePrice;
        document.getElementById("total_cost").innerHTML = totalCost;
    }

    document.getElementById("id_checkin").addEventListener("change", calculateTotalPrice);
    document.getElementById("id_checkout").addEventListener("change", calculateTotalPrice);
}