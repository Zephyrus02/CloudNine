const names = document.getElementById('name');
const calamity = document.getElementById('calamit');
const FW = document.getElementById('F/W');
const Med = document.getElementById('Med');
const Cloth = document.getElementById('Cloth');
const note = document.getElementById('note');
const form = document.getElementById('sos');
form.addEventListener('submit', (e) => {
    let messages = []
    if(names.value == '' || names.value == null){
        messages.push('Enter Valid Name')
    }
    if (messages.length>0)
    {
        e.preventDefault()
    }
})