let mytime = document.getElementById("mytime");
let mylabel = document.getElementById("timelabel");
let birthday = new Date(1992, 9, 3);
let preend = new Date(2064, 9, 4);
let now_dt = new Date();

let passed = (now_dt - birthday)/(1000 * 3600 * 24);
let left = (preend - now_dt)/(1000 * 3600 * 24);

mytime.max = passed + left;
mytime.value = left;

mylabel.textContent = left.toFixed(0) + " | " + passed.toFixed(0) + " ";
