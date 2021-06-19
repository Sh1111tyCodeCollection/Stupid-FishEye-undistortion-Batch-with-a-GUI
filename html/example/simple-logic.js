var distorter = FisheyeGl({
  image: 'images/grid.png',
  selector: '#canvas', // a canvas element to work with
  lens: {
    a: 1,    // 0 to 4;  default 1
    b: 1,    // 0 to 4;  default 1
    Fx: 0.0, // 0 to 4;  default 0.0
    Fy: 0.0, // 0 to 4;  default 0.0
   scale: 1.5 // 0 to 20; default 1.5
  },
  fov: {
    x: 1, // 0 to 2; default 1
    y: 1  // 0 to 2; default 1
  },
  fragmentSrc: "../shaders/fragment.glfs", // optional, defaults to an inbuilt fragment shader 
  vertexSrc:   "../shaders/vertex.glvs" // optional, defaults to an inbuilt vertex shader
});

distorter.getImage('image/png'); // <= format can be specified

//distorter.setImage('path/to/image.jpg'); // <= load a new image with the same distortion settings