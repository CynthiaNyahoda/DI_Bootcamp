const yelloBox = document.getElementById('target')

function dragStart(event){
    console.log('dragStart:');
}

function allowDrop(event){
    event.preventDefault();
    console.log('event', event);
    yelloBox.classList.add("is-hovered");
}

function handleDrop(event){
    console.log("handleDrop:");
    yellowBox.classList.remove{'is-hovered'}
}