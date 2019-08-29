let left_wall;
let right_wall;
let ball;
let bridges = []
const barColor = '#623D0B';
const ballColor = 'yellow';
const X = 95; const Y = 70;
const radius = 18;
const ballStart = 'L';
const bridgeWidth = 130;
const firstBridgeY = 112;

const current = new Date();
current.setSeconds(current.getSeconds()-12)
let val = (current.getMinutes()%3)*60+ current.getSeconds();


function startGame(n, side) {
    bridges = [];
    myGameArea.clear();
    left_wall.update();right_wall.update();

    for (var i = 0; i < n; i++) {
        let _firstY = firstBridgeY;
        if(n===3) _firstY += radius;

        bridges.push(new component(bridgeWidth, radius, barColor, X+radius, _firstY+radius*i*2));
        bridges[i].update()
    }
    if (side === 'L') {
        ball = new component(radius, radius, ballColor, X, Y);
    }else{
        ball = new component(radius, radius, ballColor, X+radius+bridgeWidth, Y);
    }
    myGameArea.run();
}

let myGameArea = {
    canvas : document.createElement("canvas"),
    init: function(){
        this.canvas.width = 360;
        this.canvas.height = 360;
        this.context = this.canvas.getContext("2d");
        document.querySelector('#container').insertBefore(this.canvas, document.querySelector('#container').childNodes[1]);
        left_wall  = new component(radius, 225, barColor, X, Y);
        right_wall  = new component(radius, 225, barColor, X+radius+bridgeWidth, Y);
        left_wall.update();
        right_wall.update()
    },
    run : function() {
        this.interval = setInterval(updateGameArea, 10);
    },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    stop : function() {
        clearInterval(this.interval);
    }
}

function component(width, height, color, x, y) {
    this.width = width;
    this.height = height;
    this.speedX = 0;
    this.speedY = 1;    
    this.x = x;
    this.y = y;
    this.wasLeft = 0;
    if (x < 100) this.wasLeft = 1
    
    this.update = function() {
        ctx = myGameArea.context;
        ctx.fillStyle = color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
        ctx.globalCompositeOperation='srouce-over';
    }
    this.crashRight = function(otherobj) {
        let myleft = this.x;
        let otherleft = otherobj.x;
        let crash = true;
        if (myleft < otherleft) {
            crash = false;
        }
        return crash
    }
    this.crashLeft = function(otherobj) {
        let myleft = this.x;
        let otherleft = otherobj.x;
        let crash = true;
        if (myleft > otherleft) {
            crash = false;
        }
        return crash
    }
    this.crashBridge = function(){
        let mytop = this.y;
        for(b of bridges){
            if(mytop === b.y) return true
        }
        return false
    }
}

function updateGameArea() {
    if ((ball.crashRight(right_wall) && ball.wasLeft===1) || (ball.crashLeft(left_wall)) && ball.wasLeft===0) {
        if(ball.speedX !==0 ) ball.y += 1
        if (ball.x>X+radius) {
            ball.wasLeft = 0
        }else{
            ball.wasLeft = 1
        }
        ball.speedY = 1
        ball.speedX = 0
    }
    
    if (ball.crashBridge() && ball.speedY===1) {
        ball.speedY = 0
        if (ball.x>X+radius) {
            ball.speedX = -2
        }else{
            ball.speedX = 2
        }
        // console.log(`x:${ball.x}, speedX:${ball.speedX}, wasLeft:${ball.wasLeft}`)
    }
    if (ball.y > left_wall.y + left_wall.height-ball.height){
        ball.speedX;ball.speedY;
        myGameArea.stop();
        setTimeout(function(){
            location.reload()
        }, 4000)
    } 
    
    ball.update();
    ball.x += ball.speedX;
    ball.y += ball.speedY;    
}

let myVar = setInterval(refreshGame, 1000);

function refreshGame() {
  if (document.referrer.includes('jtg-7979.com')) {
      let d = new Date();
      d.setSeconds(d.getSeconds()-12)
      // const id = '{{next_id}}'==481 ? 1 : parseInt('{{next_id}}')
      val += 1
      let secs = 180 - val;
      document.querySelector("#timer span").innerHTML = parseInt(secs/60)+'분 '+ secs%60+'초 후 '+ id +'회차 시작';
      document.querySelector("progress").value = val
      if (d.getMinutes()%3===0 && d.getSeconds()===0) {
        val = 0
        $.get(`/select/${id}`, function(res){
            const data = JSON.parse(res)
            console.log(data, id)
            startGame(data.bridges, data.start)
            $('.progress-container').toggle()
        })
      }
    }
}

myGameArea.init();