from IPython.display import HTML
from google.colab.output import eval_js

canvas_html = """
<canvas width=%d height=%d style="border:2px solid #000000"></canvas>
<button>GET</button>

<button onclick="add_click()">add</button>
<button onclick="del_click()">del</button>
<script>
var canvas = document.querySelector('canvas')
var ctx = canvas.getContext('2d')
ctx.lineWidth = %d

var i = 0;
var j = 0;
ctx.lineWidth = 1;
ctx.font = "20px Arial";

while (i < 8) {
    ctx.fillText(i++, i*40+10, 30);
}
while (j < 8) {
    ctx.fillText(j++, 15, j*40+30);
}

var matrix = [ 
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0], 
];

var i = 1;
var j = 1;
while (i < 9) {
    j = 1;
    while (j < 9) {
        ctx.strokeRect(j*40, i*40, 40, 40);
        j += 1;
    }
    i += 1;
}

ctx.fillStyle = "rgba(0, 255, 0, 0.3)";

var button = document.querySelector("button")


var state = 1;

function add_click() {
  state = 1;
}

function del_click() {
  state = 0;
}

var mouse = {x: 0, y: 0}
canvas.addEventListener('mousemove', function(e) {
  mouse.x = e.pageX - this.offsetLeft
  mouse.y = e.pageY - this.offsetTop
})

canvas.onmousedown = ()=>{
  ctx.beginPath()
  ctx.moveTo(mouse.x, mouse.y)
  canvas.addEventListener('mousemove', onPaint)
}

canvas.onmouseup = ()=>{
  canvas.removeEventListener('mousemove', onPaint)
}


var onPaint = ()=>{
  var m = Math.floor(mouse.x/40);
  var n = Math.floor(mouse.y/40);
  if (state == 1 && matrix[n-1][m-1] == 0) { 
    ctx.fillStyle = "rgba(0, 255, 0, 0.3)";
    ctx.fillRect(m*40+1, n*40+1, 38, 38);
    matrix[n-1][m-1] = 1;
  }
  if (state == 0 && matrix[n-1][m-1] == 1) { 
    ctx.fillStyle = "rgba(255, 255, 255, 1.0)";
    ctx.fillRect(m*40+1, n*40+1, 38, 38);
    matrix[n-1][m-1] = 0;
  }

}


var data = new Promise(resolve=>{
  button.onclick = ()=>{
    resolve(matrix)
  }
});

</script>
"""

def draw(w=400, h=400, line_width=1):
  display(HTML(canvas_html % (w, h, line_width)))
  data = eval_js("data")

  return data
