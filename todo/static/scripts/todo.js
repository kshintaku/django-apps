let today = new Date();

/**
* Converts a day number to a string.
*
* @param {Number} dayIndex
* @return {String} Returns day as string
*/
function dayOfWeekAsString(dayIndex) {
    return ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][dayIndex] || '';
}

/**
* Converts a month number to a string.
*
* @param {Number} monthIndex
* @return {String} Returns month as string
*/
function monthOfYearAsString(monthIndex) {
    return ["January","February","March","April","May","June","July","August","September","October","November","December"][monthIndex] || '';
}

document.getElementById("date").innerHTML = today.getDate();
document.getElementById("year").innerHTML = today.getFullYear();
document.getElementById("day").innerHTML = dayOfWeekAsString(today.getDay());
document.getElementById("month").innerHTML = monthOfYearAsString(today.getMonth());

document.getElementById("paused-tasks").style.maxHeight = document.getElementById("paused-tasks").scrollHeight + 'px';

function toggleComplete() {
    completeContainer = document.getElementById("completed-tasks")
    if(completeContainer.style.maxHeight) {
        completeContainer.style.maxHeight = null;
        document.getElementById("click-complete").innerHTML = '+'
    }
    else {
        completeContainer.style.maxHeight = completeContainer.scrollHeight + 'px';
        document.getElementById("click-complete").innerHTML = '-'
    }
}

function togglePause() {
    pauseContainer = document.getElementById("paused-tasks")
    if(pauseContainer.style.maxHeight != '0px') {
        pauseContainer.style.maxHeight = '0px';
        document.getElementById("click-pause").innerHTML = '+'
    }
    else {
        pauseContainer.style.maxHeight = pauseContainer.scrollHeight + 'px';
        document.getElementById("click-pause").innerHTML = '-'
    }
}