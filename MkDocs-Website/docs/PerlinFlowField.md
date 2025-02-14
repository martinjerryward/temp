# PerlinFlowField

<div id="p5-container"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.5.0/p5.min.js"></script>
<script>
    let cols, rows;
    let flowField;
    let particles = [];
    let scl = 20; // Scale of the grid
    let inc = 0.1; // Increment for Perlin noise
    let zoff = 0;  // Z offset for noise evolution

    function setup() {
        let container = document.getElementById("p5-container");
        let canvas = createCanvas(container.clientWidth, 400);
        canvas.parent("p5-container");

        cols = floor(width / scl);
        rows = floor(height / scl);

        flowField = new Array(cols * rows);

        // Create particles
        for (let i = 0; i < 500; i++) {
            particles.push(new Particle());
        }
    }

    function draw() {
        background(0);
        let yoff = 0;

        // Generate flow field using Perlin noise
        for (let y = 0; y < rows; y++) {
            let xoff = 0;
            for (let x = 0; x < cols; x++) {
                let index = x + y * cols;
                let angle = noise(xoff, yoff, zoff) * TWO_PI * 4; // Map Perlin noise to an angle
                let v = p5.Vector.fromAngle(angle);
                v.setMag(1); // Normalize the vector
                flowField[index] = v;
                xoff += inc;
            }
            yoff += inc;
        }
        zoff += 0.01; // Animate noise over time

        // Update and draw particles
        for (let particle of particles) {
            particle.follow(flowField);
            particle.update();
            particle.edges();
            particle.show();
        }
    }

    function windowResized() {
        let container = document.getElementById("p5-container");
        resizeCanvas(container.clientWidth, 400);
    }

    // Particle class
    class Particle {
        constructor() {
            this.pos = createVector(random(width), random(height));
            this.vel = createVector(0, 0);
            this.acc = createVector(0, 0);
            this.maxSpeed = 2;
        }

        follow(flowField) {
            let x = floor(this.pos.x / scl);
            let y = floor(this.pos.y / scl);
            let index = x + y * cols;
            let force = flowField[index];
            if (force) this.applyForce(force);
        }

        applyForce(force) {
            this.acc.add(force);
        }

        update() {
            this.vel.add(this.acc);
            this.vel.limit(this.maxSpeed);
            this.pos.add(this.vel);
            this.acc.mult(0);
        }

        edges() {
            if (this.pos.x > width) this.pos.x = 0;
            if (this.pos.x < 0) this.pos.x = width;
            if (this.pos.y > height) this.pos.y = 0;
            if (this.pos.y < 0) this.pos.y = height;
        }

        show() {
            stroke(255, 50);
            strokeWeight(2);
            point(this.pos.x, this.pos.y);
        }
    }
</script>

<style>
    #p5-container {
        width: 100%;
        max-width: 800px;  /* Adjust this based on MkDocs layout */
        margin: auto;
    }
</style>

https://sighack.com/post/getting-creative-with-perlin-noise-fields

