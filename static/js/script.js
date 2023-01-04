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

document.getElementById('book').addEventListener('mouseout', mouseOut);

function mouseOut()
{   
    result=''
    document.getElementById('book').classList.remove('disabled');
    document.getElementById('display').innerHTML=result;
}