<div id="threejs-container"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

<script>
    // Select the correct container for MkDocs
    let container = document.getElementById("threejs-container");

    // Create the Three.js scene
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / 400, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setSize(container.clientWidth, 400);
    container.appendChild(renderer.domElement);

    // Create a rotating cube
    const geometry = new THREE.BoxGeometry();
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // Create a "button" as a 3D plane
    const buttonGeometry = new THREE.PlaneGeometry(1, 0.5);
    const buttonMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000, side: THREE.DoubleSide });
    const button = new THREE.Mesh(buttonGeometry, buttonMaterial);
    button.position.set(0, -2, 0); // Position the button below the cube
    scene.add(button);

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

    // Raycaster for detecting clicks
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    function onMouseClick(event) {
        const rect = renderer.domElement.getBoundingClientRect();

        // Convert mouse coordinates to normalized device coordinates
        mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObject(button);

        if (intersects.length > 0) {
            // Change the cube color on button click
            const randomColor = Math.floor(Math.random() * 16777215);
            cube.material.color.set(randomColor);
        }
    }

    // Add event listener for mouse clicks
    renderer.domElement.addEventListener("click", onMouseClick);
</script>

<style>
    #threejs-container {
        width: 100%;
        max-width: 800px;  /* Adjust this based on MkDocs layout */
        margin: auto;
    }
</style>
