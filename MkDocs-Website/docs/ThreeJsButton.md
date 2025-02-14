# Three.js Button Example

<div id="threejs-container"></div>
<button id="change-color-btn">Change Cube Color</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    // Select the correct container for MkDocs
    let container = document.getElementById("threejs-container");

    // Create the Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / 400, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();

    renderer.setSize(container.clientWidth, 400);
    container.appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry();
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }
    animate();

    // Handle window resizing
    window.addEventListener("resize", () => {
        const newWidth = container.clientWidth;
        renderer.setSize(newWidth, 400);
        camera.aspect = newWidth / 400;
        camera.updateProjectionMatrix();
    });

    // Change cube color on button click
    document.getElementById("change-color-btn").addEventListener("click", () => {
        const randomColor = Math.floor(Math.random() * 16777215); // Generate a random hex color
        cube.material.color.set(randomColor);
    });
</script>

<style>
    #threejs-container {
        width: 100%;
        max-width: 800px;  /* Adjust this based on MkDocs layout */
        margin: auto;
    }

    button#change-color-btn {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #007bff;
        color: white;
        border: none;
        cursor: pointer;
        border-radius: 5px;
    }

    button#change-color-btn:hover {
        background-color: #0056b3;
    }
</style>