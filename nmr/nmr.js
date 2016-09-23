var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
var renderer = new THREE.WebGLRenderer();
//renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setSize( 400, 300 );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( .1, 5, .1 );
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 5;
cube.rotation.x += 0//.01//Math.PI;

var freq = 1;

var slider = function(event){
  console.log(event)
  if(event.target.id == "freq"){
  freq  = event.target.value;
}
else if(event.target.id == "Bx")
  Bx = event.target.value
  console.log(event.target.value);
}

var By = 1.
var Bx =0.1
var B = new THREE.Vector3( 1, 0, 0 );

var t = 0
var dt = 0.1

var render = function () {
	requestAnimationFrame( render );
  t += dt
  B.set( Bx * Math.cos( freq * t)  , By , Bx * Math.sin( freq* t) )
  var Bmag = B.length()
	//cube.rotation.x += Bx * Math.cos(t) * dt //.01//Math.PI;
	//cube.rotation.y += By * dt//.01;
  //cube.rotation.z += Bx * Math.sin(t)  * dt
  cube.rotateOnAxis(B , Bmag*dt);

	renderer.render(scene, camera);
};

render();


/*

var ctx;
var canvas;

var time; // keeps track of current time to find dt interval
var start;
var xpos = 0;
var ypos = 0;
var vx = 50;
var B = 10;
var vy = 0;
var Ex = -500;
var Ey = 0;
var pos = [100,100];
var vel = [100,0];
var particlenum = 10;


function main() {

	canvas = document.querySelector('nmrcanvas');

	ctx = canvas.getContext('2d');
	console.log("Running buddo");
	canvas.width = 400;
	canvas.height = 300;



	start = new Date().getTime()
	console.log("Running buddo");
	canvas.addEventListener('click', myclick, false);
	loop()
}

function myclick(e) {
	 pos = [e.clientX, e.clientY];
}
function loop() {
  clear();
  update();
  draw();
  queue();
}

function clear() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

//Returns the vector of derivtives of y with respect to x
function EqMot(x,state){
	temp = state2vec(state);
	position = temp[0];
	velocity = temp[1];
	//the derivative of position is velocity
	derivpos = velocity;
	var derivvel = [0, 0];
	//Use force law to find acceleration
	derivvel[0] =Ex + B * velocity[1];
	derivvel[1] =Ey - B * velocity[0];

	return vec2state(derivpos,derivvel);


}

function update() {
	var now = new Date().getTime(),
    dt = (now - (time || now))/1000;
	//console.log(position);
	t = (now-start)/1000;
    time = now;
	state = vec2state(pos,vel);
	sol = numeric.dopri(t,t+dt,state,EqMot);
	//currentstate = sol.at(t+dt);
	currentstate = sol.y[sol.y.length-1];
	//console.log(currentstate);
	temp = state2vec(currentstate);

	pos = temp[0];
	vel = temp[1];
	//xpos = xpos + dt*vx;
	//ypos = ypos + dt*vy;

	//vx = vx + Ex*dt + B*vy*dt;
	//vy = vy + Ey*dt-B*vx*dt;
// stub
}

function draw() {
// stub
	ctx.font = "20pt Arial";
	ctx.fillStyle = 'rgb(0,0,255)';
	//console.log(pos);
	//ctx.fillRect(xpos%canvas.width, ypos%canvas.height, 30, 30);
	ctx.fillRect(pos[0]%canvas.width, pos[1]%canvas.height, 30, 30);
	ctx.fillStyle = 'rgb(255,0,0)'
	ctx.fillText("B = " + B.toString(), 10, 50);
	ctx.fillText("Ex = " + Ex.toString(), 10, 90);
	ctx.fillText("Ey = " + Ey.toString(), 10, 130);

}

function queue() {
  window.requestAnimationFrame(loop);
}
*/
