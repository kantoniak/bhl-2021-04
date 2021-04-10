const baseUrl = 'https://bhl-counter.herokuapp.com'
const baseUUID = 'bhl-tpp'

const decreaseButton = document.getElementById('decrease');
const resetButton = document.getElementById('reset');
const increaseButton = document.getElementById('increase');

const counter = document.getElementById('counter');

const sync = new Event('sync');

function time() {
    return Date.now();
}

async function post(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'no-cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response;
}

async function decrease() {
    const exit = await post(`${baseUrl}/exit`, { conveyUUID: baseUUID, timestamp: time()});
    counter.dispatchEvent(sync);
    return exit;
}

async function reset() {
    const reset = await post(`${baseUrl}/reset`, { conveyUUID: baseUUID, timestamp: time()});
    counter.dispatchEvent(sync);
    return reset;
}

async function increase() {
    const enter = await post(`${baseUrl}/enter`, { conveyUUID: baseUUID, timestamp: time()});
    counter.dispatchEvent(sync);
    return enter;
}

async function updateCounter() {
    fetch(`${baseUrl}/stats/${baseUUID}`)
        .then(response => response.json())
        .then(data => counter.textContent = `Counter: ${data.current}`);
}

decreaseButton.addEventListener('click', decrease);
resetButton.addEventListener('click', reset);
increaseButton.addEventListener('click', increase);

updateCounter();
setInterval(() => updateCounter(), 500);

counter.addEventListener('sync', updateCounter);