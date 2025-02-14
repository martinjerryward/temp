# p5 Example

<div id="p5-container"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.5.0/p5.min.js"></script>
<script>
    function setup() {
        let container = document.getElementById("p5-container");
        let canvas = createCanvas(container.clientWidth, 400);
        canvas.parent("p5-container");
        background(200);
    }

    function draw() {
        fill(255, 0, 0);
        ellipse(mouseX, mouseY, 50, 50);
    }

    function windowResized() {
        let container = document.getElementById("p5-container");
        resizeCanvas(container.clientWidth, 400);
    }
</script>

<style>
    #p5-container {
        width: 100%;
        max-width: 800px;  /* Adjust this based on MkDocs layout */
        margin: auto;
    }
</style>
