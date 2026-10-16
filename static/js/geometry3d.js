/**
 * 3D Geometry Interactive Viewer for Math 11
 * Uses Three.js & OrbitControls
 * Author: Antigravity AI
 */

document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById('geometry3dCanvas');
    if (!canvas) return;

    // 1. Setup Three.js Scene, Camera, Renderer
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0f172a); // Slate 900

    const width = canvas.parentElement.clientWidth || 640;
    const height = 480;
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(5, 4, 6);

    const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(5, 10, 7);
    scene.add(dirLight);

    // OrbitControls & Interaction
    let controls = null;
    let fallbackActive = false;
    const target = new THREE.Vector3(0, 1, 0);

    if (typeof THREE.OrbitControls !== 'undefined') {
        controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxDistance = 25;
        controls.minDistance = 2;
        controls.enableRotate = true;
        controls.enableZoom = true;
        controls.enablePan = true;
        controls.target.copy(target);
        controls.update();
    } else {
        fallbackActive = true;
        let isPointerDown = false;
        let prevPointer = { x: 0, y: 0 };
        let radius = camera.position.distanceTo(target);
        let theta = Math.atan2(camera.position.x - target.x, camera.position.z - target.z);
        let phi = Math.acos(Math.max(-1, Math.min(1, (camera.position.y - target.y) / radius)));

        function updateCameraFromAngles() {
            camera.position.x = target.x + radius * Math.sin(phi) * Math.sin(theta);
            camera.position.y = target.y + radius * Math.cos(phi);
            camera.position.z = target.z + radius * Math.sin(phi) * Math.cos(theta);
            camera.lookAt(target);
        }

        canvas.addEventListener('pointerdown', (e) => {
            isPointerDown = true;
            try { canvas.setPointerCapture(e.pointerId); } catch(_) {}
            prevPointer = { x: e.clientX, y: e.clientY };
        });

        window.addEventListener('pointermove', (e) => {
            if (!isPointerDown) return;
            const deltaX = e.clientX - prevPointer.x;
            const deltaY = e.clientY - prevPointer.y;
            prevPointer = { x: e.clientX, y: e.clientY };

            theta -= deltaX * 0.008;
            phi -= deltaY * 0.008;
            const eps = 0.05;
            phi = Math.max(eps, Math.min(Math.PI - eps, phi));
            updateCameraFromAngles();
        });

        const stopDrag = (e) => {
            if (isPointerDown) {
                isPointerDown = false;
                try { canvas.releasePointerCapture(e.pointerId); } catch(_) {}
            }
        };
        window.addEventListener('pointerup', stopDrag);
        window.addEventListener('pointercancel', stopDrag);

        canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            radius += e.deltaY * 0.006;
            radius = Math.max(2, Math.min(25, radius));
            updateCameraFromAngles();
        }, { passive: false });
    }

    // Grid Floor Helper (subtle)
    const gridHelper = new THREE.GridHelper(10, 10, 0x334155, 0x1e293b);
    gridHelper.position.y = -0.01;
    scene.add(gridHelper);

    // Current Objects Group
    let currentShapeGroup = new THREE.Group();
    scene.add(currentShapeGroup);

    // Materials
    const solidLineMaterial = new THREE.LineBasicMaterial({ color: 0x38bdf8, linewidth: 2 }); // Light Blue
    const dashedLineMaterial = new THREE.LineDashedMaterial({ color: 0x94a3b8, dashSize: 0.15, gapSize: 0.1, linewidth: 1.5 }); // Muted dashed
    const heightLineMaterial = new THREE.LineDashedMaterial({ color: 0xef4444, dashSize: 0.15, gapSize: 0.08, linewidth: 2.5 }); // Red height
    const angleLineMaterial = new THREE.LineBasicMaterial({ color: 0x06b6d4, linewidth: 2 }); // Cyan angle
    const sectionMaterial = new THREE.MeshBasicMaterial({ color: 0xf59e0b, transparent: true, opacity: 0.35, side: THREE.DoubleSide }); // Yellow Plane

    // 2. Vertex Label Helper using 2D Canvas Sprite
    function makeTextSprite(message, color = "#ffffff") {
        const fontface = "Plus Jakarta Sans, sans-serif";
        const fontsize = 48;
        const borderThickness = 4;
        const canvasSprite = document.createElement('canvas');
        canvasSprite.width = 160;
        canvasSprite.height = 80;
        const context = canvasSprite.getContext('2d');
        context.font = "Bold " + fontsize + "px " + fontface;
        context.fillStyle = color;
        context.textAlign = "center";
        context.textBaseline = "middle";
        context.fillText(message, 80, 40);

        const texture = new THREE.Texture(canvasSprite);
        texture.needsUpdate = true;
        const spriteMaterial = new THREE.SpriteMaterial({ map: texture });
        const sprite = new THREE.Sprite(spriteMaterial);
        sprite.scale.set(0.6, 0.3, 1.0);
        return sprite;
    }

    // Helper: Add Segment
    function createSegment(p1, p2, isDashed = false, isHeight = false, forceDashedOption = true) {
        const geometry = new THREE.BufferGeometry().setFromPoints([p1, p2]);
        let mat = solidLineMaterial;

        const dashedEnabled = document.getElementById('chkDashed')?.checked ?? true;
        if (isHeight) {
            mat = heightLineMaterial;
        } else if (isDashed && dashedEnabled && forceDashedOption) {
            mat = dashedLineMaterial;
        }

        const line = new THREE.Line(geometry, mat);
        if (mat.isLineDashedMaterial) {
            line.computeLineDistances();
        }
        return line;
    }

    // 3. Shape Builders
    function buildPyramidRegular() {
        const group = new THREE.Group();
        const a = 1.6;
        const h = 2.6;

        // Points
        const S = new THREE.Vector3(0, h, 0);
        const A = new THREE.Vector3(-a, 0, -a);
        const B = new THREE.Vector3(-a, 0, a);
        const C = new THREE.Vector3(a, 0, a);
        const D = new THREE.Vector3(a, 0, -a);
        const O = new THREE.Vector3(0, 0, 0);

        // Solid Edges
        group.add(createSegment(S, B));
        group.add(createSegment(S, C));
        group.add(createSegment(B, C));
        group.add(createSegment(C, D));
        group.add(createSegment(S, D));

        // Dashed Edges (Back/Bottom)
        group.add(createSegment(S, A, true));
        group.add(createSegment(A, B, true));
        group.add(createSegment(A, D, true));
        group.add(createSegment(A, C, true));
        group.add(createSegment(B, D, true));

        // Height SO
        if (document.getElementById('chkHeight')?.checked) {
            group.add(createSegment(S, O, true, true));
        }

        // Cross section (Midpoints)
        if (document.getElementById('chkCrossSection')?.checked) {
            const M1 = new THREE.Vector3().lerpVectors(S, A, 0.5);
            const M2 = new THREE.Vector3().lerpVectors(S, B, 0.5);
            const M3 = new THREE.Vector3().lerpVectors(S, C, 0.5);
            const M4 = new THREE.Vector3().lerpVectors(S, D, 0.5);

            const sectionGeo = new THREE.BufferGeometry();
            const vertices = new Float32Array([
                M1.x, M1.y, M1.z,  M2.x, M2.y, M2.z,  M3.x, M3.y, M3.z,
                M1.x, M1.y, M1.z,  M3.x, M3.y, M3.z,  M4.x, M4.y, M4.z
            ]);
            sectionGeo.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
            const sectionMesh = new THREE.Mesh(sectionGeo, sectionMaterial);
            group.add(sectionMesh);

            // Border of cross section
            group.add(createSegment(M1, M2));
            group.add(createSegment(M2, M3));
            group.add(createSegment(M3, M4));
            group.add(createSegment(M4, M1));
        }

        // Angle Between Line SC and bottom (ABCD)
        if (document.getElementById('chkAngle')?.checked) {
            group.add(createSegment(O, C, true));
        }

        // Labels
        addLabel(group, "S", S, 0, 0.25, 0, "#f87171");
        addLabel(group, "A", A, -0.2, 0, -0.2);
        addLabel(group, "B", B, -0.2, 0, 0.2);
        addLabel(group, "C", C, 0.2, 0, 0.2);
        addLabel(group, "D", D, 0.2, 0, -0.2);
        addLabel(group, "O", O, 0, -0.25, 0, "#38bdf8");

        return group;
    }

    function buildPyramidSABottom() {
        const group = new THREE.Group();
        const w = 1.8;
        const d = 1.5;
        const h = 2.8;

        const A = new THREE.Vector3(-w/2, 0, -d/2);
        const B = new THREE.Vector3(-w/2, 0, d/2);
        const C = new THREE.Vector3(w/2, 0, d/2);
        const D = new THREE.Vector3(w/2, 0, -d/2);
        const S = new THREE.Vector3(-w/2, h, -d/2); // SA perpendicular to base

        // Solid Edges
        group.add(createSegment(S, B));
        group.add(createSegment(S, C));
        group.add(createSegment(S, D));
        group.add(createSegment(B, C));
        group.add(createSegment(C, D));

        // Dashed Edges
        group.add(createSegment(A, B, true));
        group.add(createSegment(A, D, true));
        group.add(createSegment(A, C, true));

        // Height SA
        const showHeight = document.getElementById('chkHeight')?.checked ?? true;
        group.add(createSegment(S, A, true, showHeight));

        // Cross Section Plane
        if (document.getElementById('chkCrossSection')?.checked) {
            const P1 = new THREE.Vector3().lerpVectors(S, B, 0.5);
            const P2 = new THREE.Vector3().lerpVectors(S, C, 0.5);
            const P3 = new THREE.Vector3().lerpVectors(S, D, 0.5);

            const geo = new THREE.BufferGeometry();
            const verts = new Float32Array([
                P1.x, P1.y, P1.z,  P2.x, P2.y, P2.z,  P3.x, P3.y, P3.z
            ]);
            geo.setAttribute('position', new THREE.BufferAttribute(verts, 3));
            group.add(new THREE.Mesh(geo, sectionMaterial));
            group.add(createSegment(P1, P2));
            group.add(createSegment(P2, P3));
            group.add(createSegment(P3, P1));
        }

        // Angle Line SC and base (AC is projection)
        if (document.getElementById('chkAngle')?.checked) {
            group.add(createSegment(A, C, true));
        }

        addLabel(group, "S", S, 0, 0.25, 0, "#f87171");
        addLabel(group, "A", A, -0.2, -0.1, -0.2);
        addLabel(group, "B", B, -0.2, -0.1, 0.2);
        addLabel(group, "C", C, 0.2, -0.1, 0.2);
        addLabel(group, "D", D, 0.2, -0.1, -0.2);

        return group;
    }

    function buildPyramidTriangle() {
        const group = new THREE.Group();
        const r = 1.7;
        const h = 2.5;

        const A = new THREE.Vector3(-r * 0.8, 0, -r * 0.5);
        const B = new THREE.Vector3(-r * 0.4, 0, r * 0.8);
        const C = new THREE.Vector3(r * 0.9, 0, 0.1);
        const H = new THREE.Vector3(-r * 0.4, 0, 0); // Projection point
        const S = new THREE.Vector3(-r * 0.4, h, 0);

        group.add(createSegment(S, B));
        group.add(createSegment(S, C));
        group.add(createSegment(B, C));

        group.add(createSegment(S, A, true));
        group.add(createSegment(A, B, true));
        group.add(createSegment(A, C, true));

        if (document.getElementById('chkHeight')?.checked) {
            group.add(createSegment(S, H, true, true));
        }

        if (document.getElementById('chkCrossSection')?.checked) {
            const M = new THREE.Vector3().lerpVectors(S, A, 0.5);
            const N = new THREE.Vector3().lerpVectors(S, B, 0.5);
            const P = new THREE.Vector3().lerpVectors(S, C, 0.5);
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array([
                M.x, M.y, M.z,  N.x, N.y, N.z,  P.x, P.y, P.z
            ]), 3));
            group.add(new THREE.Mesh(geo, sectionMaterial));
            group.add(createSegment(M, N));
            group.add(createSegment(N, P));
            group.add(createSegment(P, M));
        }

        addLabel(group, "S", S, 0, 0.25, 0, "#f87171");
        addLabel(group, "A", A, -0.2, 0, -0.2);
        addLabel(group, "B", B, -0.2, 0, 0.2);
        addLabel(group, "C", C, 0.2, 0, 0.1);
        addLabel(group, "H", H, 0, -0.2, 0, "#38bdf8");

        return group;
    }

    function buildPrismTriangle() {
        const group = new THREE.Group();
        const r = 1.4;
        const h = 2.4;

        // Bottom base
        const A = new THREE.Vector3(-r * 0.7, 0, -r * 0.6);
        const B = new THREE.Vector3(-r * 0.5, 0, r * 0.7);
        const C = new THREE.Vector3(r * 0.8, 0, 0);

        // Top base
        const A1 = new THREE.Vector3(A.x, h, A.z);
        const B1 = new THREE.Vector3(B.x, h, B.z);
        const C1 = new THREE.Vector3(C.x, h, C.z);

        // Top Base Edges (all visible)
        group.add(createSegment(A1, B1));
        group.add(createSegment(B1, C1));
        group.add(createSegment(C1, A1));

        // Side Edges
        group.add(createSegment(B, B1));
        group.add(createSegment(C, C1));
        group.add(createSegment(A, A1, true)); // Behind

        // Bottom Base Edges
        group.add(createSegment(B, C));
        group.add(createSegment(A, B, true));
        group.add(createSegment(A, C, true));

        // Cross Section Plane
        if (document.getElementById('chkCrossSection')?.checked) {
            const hMid = h * 0.5;
            const M = new THREE.Vector3(A.x, hMid, A.z);
            const N = new THREE.Vector3(B.x, hMid, B.z);
            const P = new THREE.Vector3(C.x, hMid, C.z);
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.BufferAttribute(new Float32Array([
                M.x, M.y, M.z,  N.x, N.y, N.z,  P.x, P.y, P.z
            ]), 3));
            group.add(new THREE.Mesh(geo, sectionMaterial));
            group.add(createSegment(M, N));
            group.add(createSegment(N, P));
            group.add(createSegment(P, M));
        }

        addLabel(group, "A'", A1, -0.2, 0.2, -0.2);
        addLabel(group, "B'", B1, -0.2, 0.2, 0.2);
        addLabel(group, "C'", C1, 0.2, 0.2, 0);
        addLabel(group, "A", A, -0.2, -0.15, -0.2);
        addLabel(group, "B", B, -0.2, -0.15, 0.2);
        addLabel(group, "C", C, 0.2, -0.15, 0);

        return group;
    }

    function addLabel(group, text, pos, ox = 0, oy = 0, oz = 0, color = "#f1f5f9") {
        const sprite = makeTextSprite(text, color);
        sprite.position.set(pos.x + ox, pos.y + oy, pos.z + oz);
        group.add(sprite);
    }

    // 4. Update Current Shape
    const explanations = {
        'pyramid_regular': {
            title: "Chóp Tứ Giác Đều S.ABCD",
            body: "• Đáy $ABCD$ là hình vuông tâm $O$.<br>• $SO \\perp (ABCD)$ là đường cao.<br>• Các cạnh bên bằng nhau: $SA = SB = SC = SD$.<br>• Góc giữa cạnh bên $SC$ và đáy là góc $\\widehat{SCO}$."
        },
        'pyramid_sa_bottom': {
            title: "Chóp S.ABCD (SA ⊥ đáy)",
            body: "• $SA \\perp (ABCD)$ nên $SA$ chính là đường cao khối chóp.<br>• Hình chiếu vuông góc của $SC$ lên đáy $(ABCD)$ là $AC$.<br>• Do đó: $(SC, (ABCD)) = \\widehat{SCA}$."
        },
        'pyramid_triangle': {
            title: "Chóp Tam Giác S.ABC",
            body: "• Khối chóp có đáy là tam giác $ABC$, đỉnh $S$.<br>• Mặt phẳng thiết diện $(MNP)$ song song với đáy $(ABC)$ theo định lí Talet trong không gian."
        },
        'prism_triangle': {
            title: "Lăng Trụ Tam Giác ABC.A'B'C'",
            body: "• Hai đáy $(ABC)$ và $(A'B'C')$ song song và bằng nhau.<br>• Các mặt bên là hình bình hành.<br>• Các cạnh bên $AA' // BB' // CC'$ và bằng nhau."
        }
    };

    // Shared materials that should not be disposed per shape toggle
    const SHARED_MATERIALS = new Set([
        solidLineMaterial,
        dashedLineMaterial,
        heightLineMaterial,
        angleLineMaterial,
        sectionMaterial
    ]);

    // Free GPU buffers, materials and sprite canvas textures to prevent memory leaks
    function disposeHierarchy(obj) {
        if (!obj) return;
        obj.traverse((child) => {
            if (child.geometry) {
                child.geometry.dispose();
            }
            if (child.material) {
                if (Array.isArray(child.material)) {
                    child.material.forEach(mat => {
                        if (!SHARED_MATERIALS.has(mat)) {
                            if (mat.map) mat.map.dispose();
                            mat.dispose();
                        }
                    });
                } else {
                    if (!SHARED_MATERIALS.has(child.material)) {
                        if (child.material.map) child.material.map.dispose();
                        child.material.dispose();
                    }
                }
            }
        });
    }

    function renderActiveShape() {
        if (currentShapeGroup) {
            scene.remove(currentShapeGroup);
            disposeHierarchy(currentShapeGroup);
            currentShapeGroup.clear();
        }

        const shapeType = document.getElementById('selectShape')?.value || 'pyramid_regular';
        let newGroup;

        if (shapeType === 'pyramid_sa_bottom') {
            newGroup = buildPyramidSABottom();
        } else if (shapeType === 'pyramid_triangle') {
            newGroup = buildPyramidTriangle();
        } else if (shapeType === 'prism_triangle') {
            newGroup = buildPrismTriangle();
        } else {
            newGroup = buildPyramidRegular();
        }

        currentShapeGroup = newGroup;
        scene.add(currentShapeGroup);

        // Update Explanations
        const exp = explanations[shapeType] || explanations['pyramid_regular'];
        const titleEl = document.getElementById('shapeTitleLabel');
        const explainTitle = document.getElementById('shapeExplainTitle');
        const explainBody = document.getElementById('shapeExplainBody');

        if (titleEl) titleEl.innerText = exp.title;
        if (explainBody) {
            explainBody.innerHTML = exp.body;
            if (window.MathJax && MathJax.typesetPromise) {
                MathJax.typesetPromise([explainBody]).catch(() => {});
            }
        }
    }

    // Event Listeners for UI
    document.getElementById('selectShape')?.addEventListener('change', renderActiveShape);
    document.getElementById('chkHeight')?.addEventListener('change', renderActiveShape);
    document.getElementById('chkCrossSection')?.addEventListener('change', renderActiveShape);
    document.getElementById('chkAngle')?.addEventListener('change', renderActiveShape);
    document.getElementById('chkDashed')?.addEventListener('change', renderActiveShape);

    // Reset Camera
    document.getElementById('btnResetView')?.addEventListener('click', () => {
        camera.position.set(5, 4, 6);
        target.set(0, 1, 0);
        camera.lookAt(target);
        if (controls) {
            controls.target.copy(target);
            controls.update();
        }
    });

    document.getElementById('btnTopView')?.addEventListener('click', () => {
        camera.position.set(0.01, 7, 0.01);
        target.set(0, 0, 0);
        camera.lookAt(target);
        if (controls) {
            controls.target.copy(target);
            controls.update();
        }
    });

    // Resize Handler
    window.addEventListener('resize', () => {
        if (!canvas.parentElement) return;
        const newWidth = canvas.parentElement.clientWidth;
        camera.aspect = newWidth / height;
        camera.updateProjectionMatrix();
        renderer.setSize(newWidth, height);
    });

    // Animation Loop with Visibility & Intersection Pausing
    let isRenderingActive = true;
    let animId = null;

    function animate() {
        if (!isRenderingActive) return;
        animId = requestAnimationFrame(animate);
        if (controls) controls.update();
        renderer.render(scene, camera);
    }

    function resumeRendering() {
        if (!isRenderingActive) {
            isRenderingActive = true;
            if (animId) cancelAnimationFrame(animId);
            animate();
        }
    }

    function pauseRendering() {
        isRenderingActive = false;
        if (animId) {
            cancelAnimationFrame(animId);
            animId = null;
        }
    }

    // Tab Visibility API: pause when user switches browser tabs
    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            pauseRendering();
        } else {
            resumeRendering();
        }
    });

    // IntersectionObserver: pause rendering if 3D canvas is scrolled out of viewport
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    resumeRendering();
                } else {
                    pauseRendering();
                }
            });
        }, { threshold: 0.05 });
        observer.observe(canvas);
    }

    // Clean up on beforeunload
    window.addEventListener('beforeunload', () => {
        pauseRendering();
        disposeHierarchy(scene);
        renderer.dispose();
    });

    renderActiveShape();
    animate();
});
