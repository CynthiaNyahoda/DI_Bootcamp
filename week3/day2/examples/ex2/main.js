const insertRow =() =>{
    const table = document.querySelector('table')

    const trs = table.querySelectorAll('tr')
    const tr = document.createElement('tr')
    tr.innerHTML = `<td> Row${trs.length+1} cell1</td>Row${trs.length+1}`

    table.appendChild(tr)
}


// to clear a specific row

const clearRows = () => {
    const row3 = document.querySelector('table tr:nth-of-type(3)')

    row3.remove()
}

// to remove all
