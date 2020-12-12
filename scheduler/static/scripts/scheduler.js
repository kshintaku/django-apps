document.querySelectorAll('.day').forEach(item => {
    item.addEventListener('click', event => {
        if (Number(item.innerHTML) > 0 && Number(item.innerHTML) < 32) {
            console.log(item.innerHTML + ' was clicked')
        }
    })
})
