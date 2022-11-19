 const socket = io();
function forward() {
    console.log('left')
  socket.emit('forward', {data: 'going forward'});
};
function left(){
    //console.log('left')
    socket.emit('left', {data: 'going left'});
}
function right(){
    socket.emit('right', {data: 'going right'});
}
function stop(){
    socket.emit('stop', {data: 'stop the car'});
}
function backward(){
    socket.emit('backward', {data: 'going backward'});
}

function look_up(){
    socket.emit('up', {data: 'look up'});
}

function look_left(){
        socket.emit('look_left', {data: 'look left'});
}

function look_right(){
        socket.emit('look_right', {data: 'look right'});
}

function nature(){
        socket.emit('nature', {data: 'look nature'});
}

function look_down(){
        socket.emit('down', {data: 'look nature'});
}

function cute(){
        socket.emit('cute', {data: 'look cute'});
}

function uncute(){
        socket.emit('uncute', {data: 'look uncute'});
}

function browse_up(){
        socket.emit('browse_up', {data: 'Browse up'});
}

function browse_down(){
        socket.emit('browse_down', {data: 'Browse down'});
}

function home(){
        socket.emit('home', {data: 'Home'});
}

function pick(){
        socket.emit('pick', {data: 'pick'});
}

function sing(){
        socket.emit('sing', {data: 'sing'});
}
