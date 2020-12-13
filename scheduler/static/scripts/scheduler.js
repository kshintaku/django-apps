
var months = {
    'January' : 1,
    'February' : 2,
    'March' : 3,
    'April' : 4,
    'May' : 5,
    'June' : 6,
    'July' : 7,
    'August' : 8,
    'September' : 9,
    'October' : 10,
    'November' : 11,
    'December' : 12,
}
document.querySelectorAll('.day').forEach(item => {
    item.addEventListener('click', event => {
        if (Number(item.innerHTML) > 0 && Number(item.innerHTML) < 32) {
            var month = document.querySelector('.month').innerHTML.split(" ");
            var yr = month[1]
            month = month[0]
            month = months[month]
            location.href="?year=" + yr + '&month=' + month + '&day=' + item.innerHTML
            // console.log(yr + ' ' + month + ' ' + item.innerHTML + ' was clicked')
        }
    })
})
