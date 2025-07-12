const board = document.getElementById('sudoku-board');

// Cargar tablero vacío
function createBoard() {
  board.innerHTML = '';
  for (let i = 0; i < 81; i++) {
    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('maxlength', '1');
    input.dataset.index = i;
    input.oninput = () => {
      const val = input.value;
      if (val && (!/^[1-9]$/.test(val))) {
        input.value = '';
      }
    };
    board.appendChild(input);
  }
}

// Validar el tablero actual
function checkBoard() {
  const inputs = [...board.querySelectorAll('input')];
  const values = inputs.map(i => i.value);

  const getRow = (i) => Math.floor(i / 9);
  const getCol = (i) => i % 9;
  const getBox = (i) => Math.floor(getRow(i) / 3) * 3 + Math.floor(getCol(i) / 3);

  const rows = Array(9).fill().map(() => []);
  const cols = Array(9).fill().map(() => []);
  const boxes = Array(9).fill().map(() => []);

  let valid = true;

  values.forEach((val, i) => {
    if (!val) return;
    const r = getRow(i);
    const c = getCol(i);
    const b = getBox(i);
    if (rows[r].includes(val) || cols[c].includes(val) || boxes[b].includes(val)) {
      inputs[i].style.backgroundColor = '#f88';
      valid = false;
    } else {
      inputs[i].style.backgroundColor = '';
      rows[r].push(val);
      cols[c].push(val);
      boxes[b].push(val);
    }
  });

  if (valid) {
    alert('¡Correcto hasta ahora!');
  } else {
    alert('Hay errores en el tablero.');
  }
}

// Reiniciar tablero
function resetBoard() {
  const inputs = board.querySelectorAll('input');
  inputs.forEach(input => {
    input.value = '';
    input.style.backgroundColor = '';
  });
}

createBoard();
