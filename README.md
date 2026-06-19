# C++ CPU Ray Tracer: Ray Tracing in One Weekend & The Next Week

A high-performance, header-only CPU Ray Tracer written in C++ based on Peter Shirley's acclaimed books: *Ray Tracing in One Weekend* and *Ray Tracing: The Next Week*. This project implements a fully functional ray tracer from scratch, demonstrating core computer graphics principles, vector mathematics, physical material behaviors, camera optics, and spatial optimization structures.

---

## 🚀 Key Features

- **Vector Mathematics Library (`vec3.h`, `color.h`, `ray.h`)**: Fully customized 3D vector, point, and color math implementation supporting addition, dot product, cross product, unit vectors, and ray reflection/refraction math.
- **Bounding Volume Hierarchy (`aabb.h`, `bvh.h`)**: Advanced spatial acceleration using Axis-Aligned Bounding Boxes (AABB) and a BVH tree structure, reducing rendering time from $O(N)$ to $O(\log N)$ for scene intersections.
- **Physical Materials (`material.h`)**:
  - **Lambertian (Diffuse)**: Realistic matte surfaces with cosine-weighted hemisphere sampling.
  - **Metal (Specular)**: Smooth mirror-like reflections with adjustable fuzziness.
  - **Dielectric (Glass)**: Refraction using Snell's Law and total internal reflection (TIR) using Schlick's approximation for Fresnel reflectivity.
- **Positionable Camera (`camera.h`)**: Supports adjustable field-of-view (FOV), look-at orientation controls, custom aspect ratios, and simulated physical lens settings like defocus blur (depth of field).
- **Anti-aliasing (`camera.h`)**: Built-in multi-sample anti-aliasing (MSAA) per pixel to remove jagged edges.
- **Interval Class (`interval.h`)**: Utility class to manage range tracking for ray intersections.

---

## 📂 Project Structure

```bash
├── main.cpp            # Application entry point (sets up scene, camera, and triggers render)
├── camera.h            # Camera class, MSAA sampling, viewport math, and render execution loop
├── material.h          # Abstract material class and its derivatives (Lambertian, Metal, Dielectric)
├── sphere.h            # Hittable spherical primitive
├── hittable.h          # Base abstract class for interceptable objects
├── hittable_list.h     # Container class for scene objects
├── aabb.h              # Axis-Aligned Bounding Box (AABB) representation for BVH
├── bvh.h               # BVH acceleration node tree
├── vec3.h              # Core 3D math wrapper for coordinates, directions, and color operations
├── ray.h               # Ray model representation (Origin + Direction * t)
├── color.h             # Color utilities and PPM formatting output
├── interval.h          # Min/max utility ranges for ray calculations
└── rtweekend.h         # Common constants, utility functions, and random number generators
```

---

## 🛠️ Compilation & Execution

This project is header-only and requires a C++ compiler supporting C++11 or higher.

### Compile
Compile the application with optimization flags (`-O3`) for fast performance:

```bash
g++ -O3 main.cpp -o raytracer.exe
```

### Run
The main program redirects output directly to generate a PPM image file using `freopen`. Simply execute the compiled binary:

```bash
./raytracer.exe
```

This will output `Final_scene.ppm` in the root directory.

---

## 🖼️ Render Gallery (Milestones)

This repository includes several pre-rendered visual milestones showing progress through the ray tracer's development:

* **`Final_scene.ppm`**: The final output featuring a large collection of random glass, metal, and diffuse spheres on a grass ground, with depth-of-field defocus blur.
* **`Defocus_Blur.ppm`**: Demonstrating physical camera lens effects (depth of field) focusing on three main spheres.
* **`refraction.ppm` & `TIR.ppm`**: Showcasing dielectric materials, total internal reflection, and light refraction.
* **`hollow_glass_sphere.ppm`**: A hollow glass bubble rendered using a sphere with negative radius nested inside another dielectric sphere.
* **`Metals.ppm` & `fuzzed_Metals.ppm`**: Highlighting reflective metal materials with varying degrees of surface roughness (fuzz).
* **`Antialiasing.ppm`**: Smooth render highlighting pixel MSAA supersampling.
- Other intermediate test steps such as `blue_white.ppm`, `first_diffuse_sphere.ppm`, `vfov.ppm`, and camera positioning files.
