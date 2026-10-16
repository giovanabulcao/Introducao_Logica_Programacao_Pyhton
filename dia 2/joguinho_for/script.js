/* ==========================================================
   Herói vs Slime — lógica
   Índice:
     1. Utilitários e código inicial
     2. Pixel art (desenho dos personagens)
     3. Estado do jogo (vida, dano, morte)
     4. Editor com cores (destaque de sintaxe)
     5. Parser   (texto -> árvore de comandos)
     6. Avaliador de expressões (vida - ataque, vida > 0...)
     7. Executor (roda o código passo a passo)
     8. Controle (botões, execução, digitação da demo)
   ========================================================== */


/* ---------- 1. Utilitários e código inicial ---------- */

const $ = (selector) => document.querySelector(selector);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const fmt = (n) => String(+(+n).toFixed(2));   // 70.0000001 -> "70"

// Código que aparece quando a página abre (e que o botão "Digitar demo" escreve)
const DEFAULT_CODE = `vida = 100
ataque = 30
while vida > 0:
    vida = vida - ataque
    if vida < 0:
        vida = 0
print("GAME OVER")`;

// Atalhos para os elementos da tela
const editor    = $('#editor');
const highlight = $('#highlight');
const arrow     = $('#arrow');


/* ---------- 2. Pixel art ----------
   Cada personagem é uma grade de letras; cada letra é uma cor da paleta.
   "." = pixel vazio. O contorno preto é adicionado automaticamente. */

function drawSprite(canvas, rows, palette, scale) {
  const h = rows.length;
  const w = rows[0].length;
  const ctx = canvas.getContext('2d');

  // +2 deixa uma borda de 1 pixel para o contorno
  canvas.width = w + 2;
  canvas.height = h + 2;
  canvas.style.width = (w + 2) * scale + 'px';
  canvas.style.height = (h + 2) * scale + 'px';

  const filled = (x, y) => x >= 0 && y >= 0 && x < w && y < h && rows[y][x] !== '.';

  for (let y = -1; y <= h; y++) {
    for (let x = -1; x <= w; x++) {
      if (filled(x, y)) {
        ctx.fillStyle = palette[rows[y][x]];
      } else if ([-1, 0, 1].some((dx) => [-1, 0, 1].some((dy) => filled(x + dx, y + dy)))) {
        ctx.fillStyle = '#0a0b0a';   // vizinho de um pixel colorido = contorno
      } else {
        continue;
      }
      ctx.fillRect(x + 1, y + 1, 1, 1);
    }
  }
}

// Herói (h=cabelo s=pele e=olho m=boca c=camisa b=cinto g=fivela p=calça o=bota)
drawSprite($('#hero'), [
  '..hhhhhh..',
  '.hhhhhhhh.',
  '.hhsssshh.',
  '.sesssses.',
  '.ssssssss.',
  '.sssmmsss.',
  '..ssssss..',
  '.cccccccc.',
  'sccccccccs',
  'sccccccccs',
  'bbbbggbbbb',
  '.pppppppp.',
  '.ppp..ppp.',
  '.ppp..ppp.',
  '.ppp..ppp.',
  '.ooo..ooo.',
  '.ooo..ooo.',
], {
  h: '#6b4430', s: '#f4cba4', e: '#222222', m: '#d98a7a', c: '#6ee0d2',
  b: '#85623a', g: '#e9c04a', p: '#3d4166', o: '#5c3b25',
}, 8);

// Slime (g=corpo d=sombra w=brilho e=olhos e boca)
const slimeRows = [
  '....gggggg....',
  '..gggggggggg..',
  '.gggggggggggg.',
  '.gggggggggggg.',
  'gggggggggggggg',
  'gggggggggggggg',
  'gggggggggggggg',
  '.dddddddddddd.',
].map((row) => row.split(''));

[[3, 1], [4, 1], [3, 2]].forEach(([x, y]) => (slimeRows[y][x] = 'w'));  // brilho
[[4, 4], [9, 4]].forEach(([x, y]) => (slimeRows[y][x] = 'e'));          // olhos
[5, 6, 7, 8].forEach((x) => (slimeRows[6][x] = 'e'));                   // boca

drawSprite($('#slime'), slimeRows.map((r) => r.join('')), {
  g: '#8be05a', d: '#68b948', w: '#eaffd8', e: '#1e2a18',
}, 8);


/* ---------- 3. Estado do jogo ----------
   Sempre que o código muda a variável "vida" ou "ataque",
   a função setVar() decide o que mostrar na tela. */

let hp = 100;           // vida atual
let maxHp = 100;        // vida máxima (= primeiro valor atribuído a "vida")
let hpStarted = false;  // já recebemos o primeiro "vida = ..."?

// Atualiza texto, barra e estado de morte do herói
function paintHp() {
  const bar = $('#hpBar');
  const negative = hp < 0;
  const pct = maxHp ? Math.min(1, Math.abs(hp) / maxHp) : 0;

  $('#hpText').textContent = fmt(hp) + '/' + fmt(maxHp);
  bar.style.width = (hp <= 0 && !negative ? 0 : pct * 100) + '%';
  bar.className = negative ? 'neg' : pct > 0.5 ? '' : pct > 0.25 ? 'y' : 'r';

  $('#hero').classList.toggle('dead', hp <= 0);
}

// Número flutuante de dano (-30) ou cura (+20)
function showPop(text, extraClass) {
  const el = document.createElement('div');
  el.className = 'pop ' + (extraClass || '');
  el.textContent = text;
  $('#heroWrap').appendChild(el);
  el.onanimationend = () => el.remove();
}

// Reinicia uma animação CSS (remove e adiciona a classe de novo)
function replayAnimation(el, className) {
  el.classList.remove(className);
  void el.offsetWidth;   // força o navegador a "esquecer" a classe anterior
  el.classList.add(className);
  setTimeout(() => el.classList.remove(className), 450);
}

// Chamada toda vez que o código atribui um valor a uma variável
function setVar(name, value) {
  if (name === 'ataque' && typeof value === 'number') {
    $('#attackText').textContent = fmt(value);
    return;
  }
  if (name !== 'vida' || typeof value !== 'number') return;

  // Primeira atribuição: define a vida máxima, sem mostrar dano
  if (!hpStarted) {
    hpStarted = true;
    maxHp = value > 0 ? value : 100;
    hp = value;
    paintHp();
    return;
  }

  const diff = value - hp;
  hp = value;
  paintHp();

  if (diff < 0) {
    showPop('-' + fmt(-diff));
    if (hp > 0) replayAnimation($('#hero'), 'hit');
    replayAnimation($('#slime'), 'lunge');
  } else if (diff > 0) {
    showPop('+' + fmt(diff), 'up');
  }
}

// Volta tudo ao estado inicial antes de cada execução
function resetGame() {
  hp = 100;
  maxHp = 100;
  hpStarted = false;
  $('#attackText').textContent = '30';
  $('#gameOver').className = '';
  $('#gameOver').textContent = '';
  paintHp();
}


/* ---------- 4. Editor com cores ----------
   O <pre> mostra o mesmo texto do <textarea>, mas colorido. */

const KEYWORDS = new Set(['while', 'if', 'elif', 'else', 'for', 'in', 'and', 'or', 'not', 'pass']);
const BUILTINS = new Set(['print', 'range', 'True', 'False']);

const escapeHtml = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');

// Devolve uma classe de cor para cada caractere da linha
function colorClasses(line) {
  const classes = new Array(line.length).fill('');
  const tokens = /(#.*)|("[^"]*"|'[^']*')|(\d+\.?\d*)|([A-Za-z_]\w*)|([-+*\/%<>=!]+)/g;
  let m;

  while ((m = tokens.exec(line))) {
    const cls = m[1] ? 'c'                                   // comentário
              : m[2] ? 's'                                   // texto
              : m[3] ? 'n'                                   // número
              : m[4] ? (KEYWORDS.has(m[4]) ? 'k' : BUILTINS.has(m[4]) ? 'f' : 'v')
              : 'o';                                         // operador
    for (let i = m.index; i < m.index + m[0].length; i++) classes[i] = cls;
  }
  return classes;
}

/* Desenha o código colorido.
   "mark" (opcional) = { line, c0, c1, cls } -> trecho a destacar */
function render(mark) {
  highlight.innerHTML = editor.value.split('\n').map((text, lineIndex) => {
    const classes = colorClasses(text);
    let html = '', currentClass = null, buffer = '';

    const flush = () => {
      if (buffer) html += `<span class="${currentClass}">${escapeHtml(buffer)}</span>`;
      buffer = '';
    };

    for (let col = 0; col < text.length; col++) {
      const marked = mark && mark.line === lineIndex && col >= mark.c0 && col < mark.c1;
      const cls = classes[col] + (marked ? ' mk-' + mark.cls : '');
      if (cls !== currentClass) { flush(); currentClass = cls; }
      buffer += text[col];
    }
    flush();
    return html || ' ';
  }).join('\n');
}

// Seta ▶ que acompanha a linha em execução
let arrowLine = null;
function positionArrow() {
  if (arrowLine === null) { arrow.style.opacity = 0; return; }
  arrow.style.opacity = 1;
  arrow.style.transform = `translateY(${arrowLine * 22 - editor.scrollTop}px)`;
}

// Mantém o texto colorido alinhado quando o editor rola
editor.addEventListener('scroll', () => {
  highlight.scrollTop = editor.scrollTop;
  highlight.scrollLeft = editor.scrollLeft;
  positionArrow();
});


/* ---------- 5. Parser ----------
   Transforma o texto em uma árvore. Tipos de nó:
     set    -> vida = 10        while -> while cond:
     if     -> if/elif/else     for   -> for i in range(n):
     print  -> print("...")
   A indentação define quais comandos ficam dentro de qual bloco. */

function parse(source) {
  const lines = source.split('\n');
  const root = [];
  const stack = [{ indent: -1, body: root }];  // blocos abertos
  let pending = null;                          // bloco que acabou de abrir (linha terminada em ":")

  for (let i = 0; i < lines.length; i++) {
    const code = lines[i].replace(/\t/g, '    ').replace(/#.*$/, '');
    if (!code.trim()) continue;                // ignora linhas vazias e comentários

    const indent = code.match(/^ */)[0].length;
    const text = code.trim();
    const fail = (msg) => { throw { line: i, msg }; };

    // Depois de um ":" a próxima linha precisa estar mais indentada
    if (pending) {
      if (indent <= pending.indent) fail('falta código indentado depois dos ":"');
      stack.push(pending);
      pending = null;
    }
    // Linha menos indentada = fecha blocos
    while (stack.length > 1 && indent <= stack[stack.length - 1].indent) stack.pop();

    const body = stack[stack.length - 1].body;

    // Guarda o texto e a posição (coluna) de uma expressão, para poder destacá-la depois
    const expr = (str, from) => {
      str = str.trim();
      const c0 = code.indexOf(str, from || indent);
      return { src: str, c0, c1: c0 + str.length };
    };

    let m;
    if ((m = text.match(/^(while|if|elif)\s+(.+):$/))) {
      const cond = expr(m[2], indent + m[1].length);
      const inner = [];
      if (m[1] === 'while') {
        body.push({ t: 'while', line: i, cond, body: inner });
      } else if (m[1] === 'if') {
        body.push({ t: 'if', line: i, branches: [{ line: i, cond, body: inner }] });
      } else {
        const prev = body[body.length - 1];
        if (!prev || prev.t !== 'if') fail('"elif" sem "if" antes');
        prev.branches.push({ line: i, cond, body: inner });
      }
      pending = { indent, body: inner };

    } else if (/^else\s*:$/.test(text)) {
      const prev = body[body.length - 1];
      if (!prev || prev.t !== 'if') fail('"else" sem "if" antes');
      const inner = [];
      prev.branches.push({ line: i, cond: null, body: inner });
      pending = { indent, body: inner };

    } else if ((m = text.match(/^for\s+([A-Za-z_]\w*)\s+in\s+range\((.+)\):$/))) {
      const inner = [];
      body.push({ t: 'for', line: i, v: m[1], n: expr(m[2], indent + 4), body: inner });
      pending = { indent, body: inner };

    } else if ((m = text.match(/^print\((.*)\)$/))) {
      body.push({ t: 'print', line: i, e: expr(m[1], indent + 5) });

    } else if ((m = text.match(/^([A-Za-z_]\w*)\s*([-+*\/%])?=(?!=)\s*(.+)$/))) {
      body.push({ t: 'set', line: i, name: m[1], op: m[2], e: expr(m[3], code.indexOf('=', indent) + 1) });

    } else if (text !== 'pass') {
      fail('não entendi esta linha');
    }
  }

  if (pending) throw { line: lines.length - 1, msg: 'falta código indentado depois dos ":"' };
  return root;
}


/* ---------- 6. Avaliador de expressões ----------
   Calcula coisas como "vida - ataque" ou "vida > 0".
   Só aceita números, textos, variáveis conhecidas e operadores
   permitidos; qualquer outra coisa gera erro (por segurança). */

function evaluate(expression, vars) {
  const parts = expression.src.match(
    /"[^"\\]*"|'[^'\\]*'|\d+\.?\d*|[A-Za-z_]\w*|\*\*|==|!=|<=|>=|[-+*\/%()<>]|\s+|./g
  ) || [];
  let js = '';

  for (const part of parts) {
    if (/^\s+$/.test(part)) continue;

    if (/^["'\d]/.test(part) || /^(\*\*|==|!=|<=|>=|[-+*\/%()<>])$/.test(part)) js += part;
    else if (part === 'and') js += '&&';
    else if (part === 'or') js += '||';
    else if (part === 'not') js += '!';
    else if (part === 'True') js += 'true';
    else if (part === 'False') js += 'false';
    else if (/^[A-Za-z_]/.test(part)) {
      if (!(part in vars)) throw new Error(`"${part}" ainda não foi definida`);
      js += 'vars.' + part;
    } else {
      throw new Error(`símbolo "${part}" não suportado`);
    }
    js += ' ';
  }

  try {
    return new Function('vars', 'return (' + js + ')')(vars);
  } catch (e) {
    throw new Error('expressão inválida: ' + expression.src);
  }
}


/* ---------- 7. Executor ----------
   É um "generator": a cada "yield" ele entrega um passo
   (linha atual, trecho a destacar, variável alterada ou texto
   impresso) e pausa. Assim a tela pode animar passo a passo. */

let currentLine = 0;  // usada para indicar em qual linha ocorreu um erro
const markOf = (line, e, cls) => ({ line, c0: e.c0, c1: e.c1, cls });

function* execute(body, vars) {
  for (const node of body) {
    currentLine = node.line;

    if (node.t === 'set') {
      yield { line: node.line, mark: markOf(node.line, node.e, 'ev') };   // destaca o cálculo
      const value = node.op
        ? evaluate({ src: `${node.name} ${node.op} (${node.e.src})` }, vars)  // vida -= 10
        : evaluate(node.e, vars);
      vars[node.name] = value;
      yield { line: node.line, set: [node.name, value] };                 // aplica no jogo

    } else if (node.t === 'while') {
      for (let loops = 0; ; loops++) {
        currentLine = node.line;
        const ok = !!evaluate(node.cond, vars);
        yield { line: node.line, mark: markOf(node.line, node.cond, ok ? 'ev' : 'no') };
        if (!ok) break;
        if (loops > 300) throw new Error('laço infinito? (mais de 300 voltas)');
        yield* execute(node.body, vars);
      }

    } else if (node.t === 'if') {
      for (const branch of node.branches) {
        currentLine = branch.line;
        let ok = true;
        if (branch.cond) {
          ok = !!evaluate(branch.cond, vars);
          yield { line: branch.line, mark: markOf(branch.line, branch.cond, ok ? 'ev' : 'no') };
        }
        if (ok) { yield* execute(branch.body, vars); break; }
      }

    } else if (node.t === 'for') {
      const times = Math.min(300, evaluate(node.n, vars));
      yield { line: node.line, mark: markOf(node.line, node.n, 'ev') };
      for (let i = 0; i < times; i++) {
        vars[node.v] = i;
        yield { line: node.line };
        yield* execute(node.body, vars);
      }

    } else if (node.t === 'print') {
      yield { line: node.line, print: String(evaluate(node.e, vars)) };
    }
  }
}


/* ---------- 8. Controle ---------- */

let runId = 0;       // cada execução tem um número; editar o código invalida a anterior
let typing = false;  // true enquanto a demo está digitando
let autoTimer;       // espera depois de digitar, antes de rodar sozinho

function showMessage(text, isError) {
  const el = $('#message');
  el.textContent = text;
  el.className = isError ? 'err' : '';
}

// Mostra o erro na tela e destaca a linha problemática
function showError(e) {
  const line = e.line !== undefined ? e.line : currentLine;
  const lineText = editor.value.split('\n')[line] || '';
  render({ line, c0: 0, c1: lineText.length, cls: 'no' });
  arrowLine = line;
  positionArrow();
  showMessage(`Erro na linha ${line + 1}: ${e.msg || e.message}`, true);
}

// Executa o código do editor, um passo de cada vez
async function run() {
  const myRun = ++runId;
  clearTimeout(autoTimer);
  resetGame();
  arrowLine = null;
  positionArrow();
  render();

  let tree;
  try { tree = parse(editor.value); } catch (e) { return showError(e); }

  showMessage('Executando…');
  try {
    for (const step of execute(tree, Object.create(null))) {
      if (myRun !== runId) return;            // código foi editado: para esta execução

      render(step.mark);
      arrowLine = step.line;
      positionArrow();

      if (step.set) setVar(...step.set);
      if (step.print != null) {
        $('#gameOver').textContent = step.print.toUpperCase();
        $('#gameOver').className = 'on';
      }
      await sleep(1520 - +$('#speed').value); // pausa entre passos (controle de velocidade)
    }
  } catch (e) {
    if (myRun === runId) showError(e);
    return;
  }

  if (myRun === runId) {
    render();
    arrowLine = null;
    positionArrow();
    showMessage('Fim: o laço terminou.');
  }
}

// Digita o código de exemplo letra por letra e depois executa
async function typeDemo() {
  const myRun = ++runId;
  typing = true;
  clearTimeout(autoTimer);
  editor.value = '';
  resetGame();
  arrowLine = null;
  positionArrow();
  render();
  showMessage('Digitando…');

  for (const ch of DEFAULT_CODE) {
    if (myRun !== runId) { typing = false; return; }
    editor.value += ch;
    editor.scrollTop = 1e5;
    render();
    await sleep(ch === '\n' ? 260 : 42);
  }
  typing = false;
  run();
}

// Quando você edita o código: cancela a execução atual e (se "auto") roda de novo
editor.addEventListener('input', () => {
  runId++;
  render();
  arrowLine = null;
  positionArrow();
  if (typing) return;

  showMessage('Editando…');
  clearTimeout(autoTimer);
  if ($('#autoRun').checked) autoTimer = setTimeout(run, 900);
});

// Facilidades de digitação: Tab insere 4 espaços; Enter mantém a indentação
function insertText(text) {
  editor.setRangeText(text, editor.selectionStart, editor.selectionEnd, 'end');
  editor.dispatchEvent(new Event('input'));
}
editor.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    e.preventDefault();
    insertText('    ');
  } else if (e.key === 'Enter') {
    e.preventDefault();
    const line = editor.value.slice(0, editor.selectionStart).split('\n').pop();
    const indent = line.match(/^ */)[0];
    insertText('\n' + indent + (line.trimEnd().endsWith(':') ? '    ' : ''));
  }
});

// Botões
$('#runBtn').onclick = run;
$('#demoBtn').onclick = typeDemo;

// Início
editor.value = DEFAULT_CODE;
paintHp();
run();
