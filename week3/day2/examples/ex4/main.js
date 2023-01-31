const getvalue = () => {
    // get form first
    const form = document.forms
    // use const form = document.getElementById('forms')

    // target element
    const fname = form.elements.fname.value
    const lname = form.elements.lname.value
    alert (`${fname}-${lname}`)
}

// to bind and avoid refresh
// form.onsubmit = getvalue;


// object restructuring
