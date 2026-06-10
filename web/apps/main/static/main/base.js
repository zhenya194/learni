const now = new Date();
const hours = now.getHours();
const minutes = now.getMinutes();
const time_element = document.getElementById("time_element");
const timezone_element = document.getElementById("timezone_element");

function getUTCtime() {
    const offset = -new Date().getTimezoneOffset() / 60;

    const sign = offset >= 0 ? "+" : "-";
    const absOffset = Math.abs(offset);

    return `UTC${sign}${absOffset}`;
}

timezone_element.innerHTML = `Server timezone: ${getUTCtime()}`;
time_element.innerHTML = `Server time: ${hours}:${minutes}`;
