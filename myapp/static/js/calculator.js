
let display = document.getElementById('display');
function press(value) {
  if (value === '=') {
    try { display.value = eval(display.value); } catch { display.value = 'Error'; }
  } else if (value === 'C') {
    display.value = '';
  } else {
    display.value += value;
  }
}
