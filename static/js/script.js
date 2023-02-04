// Get the check-in date input element and the book button
const checkInDate = document.getElementById("id_checkin");
const checkOutDate = document.getElementById("id_checkout");
const bookButton = document.getElementById("book");

if(checkInDate && checkOutDate && bookButton){
    checkInDate.addEventListener("change", checkDates);
    checkOutDate.addEventListener("change", checkDates);
    checkDates();
}
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
            bookButton.value = "Book";
        }
    }


// A funcktion to make sure the user wont be able to change to check in and out in the past
if(document.getElementById('update_booking')) {
    const checkInDate = document.getElementById("id_checkin");
    const checkOutDate = document.getElementById("id_checkout");
    const bookButton = document.getElementById("update");
    if(checkInDate && checkOutDate && bookButton){
        checkInDate.addEventListener("change", checkDates);
        checkOutDate.addEventListener("change", checkDates);
        checkDates();
        (function checkDates() {
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
                bookButton.value = "Update";
            }
        })();        
    }
}

// a go back one page function
$(document).ready(function() {
    $('.btn-back').click(function() {
        window.history.back();
    });
});

// add a function to calculate the price in real time
function calculateTotalPrice() {
    let checkInDate = new Date(document.getElementById("id_checkin").value);
    let checkOutDate = new Date(document.getElementById("id_checkout").value);
    let housePrice = parseFloat(document.getElementById("price").innerHTML);
    let oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
    let diffDays = Math.round(Math.abs((checkOutDate.getTime() - checkInDate.getTime())/(oneDay)));
    let totalCost = diffDays * housePrice;
    document.getElementById("total_cost").innerHTML = totalCost;
  }
  
  if(document.getElementById('price')){
    calculateTotalPrice();
  
    document.getElementById("id_checkin").addEventListener("change", calculateTotalPrice);
    document.getElementById("id_checkout").addEventListener("change", calculateTotalPrice);
  }
  


// add a span to the ranges so you can see what value they have
if(document.getElementById('add_house')) {
    const rangeInputBeds = document.getElementById("beds");
    const valueDisplayBeds = document.createElement("bed");

    valueDisplayBeds.classList.add("range-value");
    rangeInputBeds.parentNode.insertBefore(valueDisplayBeds, rangeInputBeds);

    rangeInputBeds.addEventListener("input", function() {
        valueDisplayBeds.innerHTML = rangeInputBeds.value;
        valueDisplayBeds.style.left = rangeInputBeds.value + "%";
    });

    const rangeInputCapacity = document.getElementById("capacity");
    const valueDisplayCapacity = document.createElement("guests");

    valueDisplayCapacity.classList.add("range-value");
    rangeInputCapacity.parentNode.insertBefore(valueDisplayCapacity, rangeInputCapacity);

    rangeInputCapacity.addEventListener("input", function() {
        valueDisplayCapacity.innerHTML = rangeInputCapacity.value;
        valueDisplayCapacity.style.left = rangeInputCapacity.value + "%";
    });
}
// add a value to the range in the filter house section so you can get a value from the range slider
if(document.getElementById('filter_house')){
    const rangeInputCapacity = document.getElementById("capacity");
    const valueDisplayCapacity = document.createElement("guests");

    valueDisplayCapacity.classList.add("range-value");
    rangeInputCapacity.parentNode.insertBefore(valueDisplayCapacity, rangeInputCapacity);

    rangeInputCapacity.addEventListener("input", function() {
        valueDisplayCapacity.innerHTML = rangeInputCapacity.value;
        valueDisplayCapacity.style.left = rangeInputCapacity.value + "%";
    });
}

$('#confirmDeleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var id = button.data('id');
    var modal = $(this);
    modal.find('.modal-footer #confirmDeleteButton').attr("href", 'delete_view/' + id);
  });

// Adds the the parallax efect of the hero image
if(document.getElementById('index')){
    let bg = document.getElementById('bg');
    let water = document.getElementById('water');
    let text = document.getElementById('text');

    window.addEventListener('scroll', function() {
        let value = window.scrollY;
        bg.style.top = value * 0.4 + 'px';
        water.style.top = value * 0.1 + 'px';
        text.style.top = value * 0.7 + 'px';
    });
}
// Help the fade in class in the list house page and lets houses slide in
if(document.getElementById('list_house')) {
    const faders = document.querySelectorAll('.fade-in');
    const apperOptions = {
    threshold: 1,
    rootMargin: '0px 0px -10px 0px'
    };
    const apperOnScroll = new IntersectionObserver(
    function(
        entries,
        apperOnScroll
        ){
            entries.forEach(entries => {
                if (!entries.isIntersecting) {
                    return;
                } else{
                    entries.target.classList.add('appear');
                    apperOnScroll.unobserve(entries.target);
                }
            });
        },
        apperOptions);

        faders.forEach(fader => {
            apperOnScroll.observe(fader);
        });
    }

// function to reset the filter function
function resetForm(){
    document.getElementById("beds").value="";
    document.getElementById("capacity").value="";
    document.getElementById("has_wifi").checked = false;
    document.getElementById("has_tv").checked = false;
    document.getElementById("has_bbq").checked = false;
    document.getElementById("has_shower").checked = false;
    document.getElementById("has_bath").checked = false;
    document.getElementById("filterForm").submit();
  }