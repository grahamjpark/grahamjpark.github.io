// From: https://codepen.io/chrisgannon/pen/VapQoG
// TODO: Update to use

var xmlns = "http://www.w3.org/2000/svg",
  xlinkns = "http://www.w3.org/1999/xlink",
  select = function(s) {
    return document.querySelector(s);
  },
  selectAll = function(s) {
    return document.querySelectorAll(s);
  },
  pContainer = select('.pContainer'),
  heart = select('.heart'),
  heartSVG = select('.heartSVG'),
//   heartLines = select('.heartLines'),
//   allHeartLines = selectAll('.heartLines line'),
  maxParticlePool = 100,
  particleArr = [],
  heartArr = [],
  heartTl = new TimelineMax({paused:true, onComplete:function(){
    this.seek(0);
    this.pause();
  }}),
  heartTimelineArr = [],
  heartLineClonesTl = new TimelineMax({paused:true}),
  heartCount = 0,
  particleType = [
    {element:'#paper', weight:1.8},
    {element:'#star', weight:2.1}, 
    {element:'#diamond', weight:1.7},
    {element:'#ring', weight:2.3}
  ],
particleColorArray = ['#34A3F2','#B400AC', '#88E259','#F75E19', '#39C5C0', '#E3004D'],
  myDataObj = {

    gravity: 60,
    gravityMax: 100,

    velocity: 230,
    velocityMax: 800,

    alpha: 1,
    alphaMax: 1,

    angle: 0,
    angleMax: 360,

    rotation: 720,
    rotationMax: 1000,

    particles: 20,
    particlesMax: 500,

    duration: 2.7,
    durationMax: 10,

    skewx: 0,
    skewxMax: 2280,

    skewy: 360,
    skewyMax: 2280,
    
    time: 3,
    timeMax: 4
  },
  tl = new TimelineMax({
  repeat: 0
});


// TweenMax.set('svg', {
//   visibility: 'visible'
// })
// TweenMax.set(heart, {
//   transformOrigin:'50% 50%',
//   scale:0.8
// })
// TweenMax.set(heartLines, {
//   transformOrigin:'50% 50%',
//   x:230,
//   y:230
// })
// TweenMax.set(allHeartLines, {
//   drawSVG:'0% 35%'
// })

function createHeartLinePool(){
  
  for(var i = 0; i < 5; i++){
    
    var hl = heartLines.cloneNode(true);
    var lines = hl.querySelectorAll('line');
    pContainer.appendChild(hl);
    TweenMax.set(hl, {
      x:randomBetween(190,280),
      y:randomBetween(100,190),
      scale:0.5,
      transformOrigin:'50% 50%'
    })
    TweenMax.set(lines, {
      drawSVG:'0% 0%',
      immediateRender:true
    })    
    var tl = new TimelineMax({paused:true});
    tl.to(lines, 0.2, {
      drawSVG:'10% 30%',
      ease:Linear.easeNone
    })
    .to(lines, 0.4, {
      drawSVG:'100% 100%',
      ease:Linear.easeNone
    })
    heartLineClonesTl.add(tl, i/8)
    
  }
}

function createParticlePool() {
  var i = maxParticlePool, p, tl;
  while (--i > -1) {
    p = document.createElementNS(xmlns, 'use');
    heartSVG.appendChild(p);
    p.setAttributeNS(null, 'fill', particleColorArray[randomBetween(0, particleColorArray.length - 1)]);
    //p.setAttributeNS(null, 'stroke', '#FFF');
    p.setAttributeNS(xlinkns, "xlink:href", particleType[randomBetween(0, particleType.length-1)].element);
    TweenMax.set(p, {
      scale:0,
      transformOrigin: '50% 50%'
    })   
   
  }//end while
  
    heartTl.to(heart, 0.2, {
      y:-100,
      ease:Power1.easeOut
    })
    .to(heart, 0.2, {
      fill:'#E00050',
      ease:Power1.easeIn
    },'-=0.2')
    .to(allHeartLines, 0.6, {
      drawSVG:'100% 100%'
    },'-=0.2')
    .to(heart, 0.4, {
      y:0,
      ease:Back.easeOut
    },'-=0.4')
    .addPause()
    .to(heart, 0.2, {
      fill:'#ABB9C2'
    }) 
}


function createParticles() {

  var i = myDataObj.particles, p, particleObj;
  while (--i > -1) {
    
    particleObj = particleType[randomBetween(0, particleType.length-1)];
    p = document.createElementNS(xmlns, 'use');
    pContainer.appendChild(p);

    p.setAttributeNS(null, 'fill', particleColorArray[randomBetween(0, particleColorArray.length - 1)])
    p.setAttributeNS(xlinkns, "xlink:href", particleObj.element);
    p.setAttribute('scale', randomBetween(3, 8) / 10)
    p.setAttribute('weight', particleObj.weight);
    particleArr.push(p);
    TweenMax.set(p, {
      transformOrigin: '50% 50%',
      y:-40 
    })  
  }
}

function createExplosion() {

  if (myDataObj.duration < 0.5) {

    myDataObj.duration = 0.5;
  }

  var i = myDataObj.particles,
    p, pCount = 0;
  tl.clear();

  while (--i > -1) {
    p = particleArr[i];
    TweenMax.set(p, {
      scale: p.getAttribute('scale'),
      x: 310,
      y: 220,
      alpha: myDataObj.alpha
    })
    var t = TweenMax.to(p, randomBetween(0.1, myDataObj.duration), {
      physics2D: {
        velocity: randomBetween(myDataObj.velocity/2, myDataObj.velocity),
        angle: randomBetween(-110, -80),
        gravity: p.getAttribute('weight') * myDataObj.gravity
        
      },
      //alpha: 0,
      rotation: randomBetween(0, myDataObj.rotationMax),
      skewX: randomBetween(0, myDataObj.skewx),
      skewY: randomBetween(0, myDataObj.skewy),
      //scale:0.5,
      //ease: Expo.easeOut,
      ease: Sine.easeInOut,
      //ease:SlowMo.ease.config(0., 1, false),
      onComplete: function(p) {
      
        TweenMax.set(p, {
          x:-20,
          y:-20
        })

      },
      onCompleteParams: [p]
    });

    tl.add(t, 0)
  } //end while
  
  tl.timeScale(myDataObj.time);
  

}

function resetHeartLineClones(){
  
  for(var i = 0; i < heartLineClonesTl.getChildren(true, false, true).length; i++){
    var tl = heartLineClonesTl.getChildren(true, false, true)[i];
    tl.restart()
  }
}

function randomBetween(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

createParticlePool();
createParticles();
createHeartLinePool();
heart.onclick = function(){
  heartTl.play();
  

  if(heartTl.time() > 0){
    return;
  }
  TweenMax.delayedCall(0.3, function(){
    resetHeartLineClones();
    heartLineClonesTl.restart();
  })  
  createExplosion();
}
