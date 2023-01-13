// Function do prevent user from checking out befor checking in
    
document.getElementById('book').addEventListener('mouseover', mouseIn);
    function mouseIn()
{
    let Dateone=new Date(document.getElementById('id_checkin').value);
    let Datetwo=new Date(document.getElementById('id_checkout').value);
    let result;

    if(Dateone>Datetwo)
    {
        result='<p>You cant check out before you check in.</p>';
        document.getElementById('display').style.color='red';
        document.getElementById('book').classList.add('disabled');
        document.getElementById('display').innerHTML=result;
    }
};
// Removing the blocked button when mouse pointer moves out
document.getElementById('book').addEventListener('mouseout', mouseOut);

function mouseOut()
{   
    result=''
    document.getElementById('book').classList.remove('disabled');
    document.getElementById('display').innerHTML=result;
}

// a go back function in cancel page

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

console.log('hello')