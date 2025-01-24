## Team Name and Members
Team: **The Innovators**  
Members:  
- **Viney Jain**  
- **Wahiq Iqbal**

## Course and Project Details
**Course:** COMP 312 - Principles of Computer Systems  
**Instructor:** Prof. Chiranjib Sur  
**Date:** 24th January 2025  

## Overview
This repository contains our final project submission in two parts:

1. **Part 1** focuses on applying systems thinking concepts and the software development life cycle (SDLC) principles to document and plan a Library Management software.  
2. **Part 2** covers implementing numerical methods (Euler’s Method and Runge-Kutta Method) in Python to compute the first and second derivatives of the function f(x) = x·e^x for x ranging from 1.5 to 2.5 with a step size of 0.1, followed by performance comparisons, memory profiling, and code optimizations.

---

## Part 1: System Thinking and SDLC
We have developed a Library Management Software plan integrating the methods learned from the workshops:

### Software Requirement Specification (SRS)
- **End-User Version:** Describes key features such as user registration, catalog management, search functionality, transaction management, membership management, and reporting.  
- **Developer Version:** Outlines functional requirements (comprehensive database schema, RESTful APIs) and non-functional requirements (scalability, performance, security, maintainability).  
- **Acceptance Document:** Lists acceptance criteria ensuring user-friendly design, robust notifications, report generation, and basic security compliance.

### Project Planning
Our plan is divided into multiple phases—Requirement Analysis, Design, Development, Testing, and Deployment—each with timelines and clear deliverables. A Gantt chart outlines these phases visually, and an activity planner tabulates the responsibilities for each team role.

### Knowledge from Workshops
Using systems thinking, we identified the elements, interconnections, and purpose of the library system. We employed SDLC principles, including iterative development, continuous integration, and continuous deployment practices, to ensure frequent user feedback and smooth delivery of updates.

---

## Part 2: Numerical Methods Implementation

### Function and Derivatives
- Function: f(x) = x·e^x  
- First Derivative: f′(x) = (1 + x)·e^x  
- Second Derivative: f′′(x) = (2 + x)·e^x  

### Euler’s Method
We implemented a Python script to approximate f′(x) and f′′(x) over x = 1.5 to x = 2.5 with step size 0.1. The code includes:  
- Iterative updates of the derivative values  
- Memory profiling to evaluate performance  
- Initial (unoptimized) version and a refined optimized version

### Runge-Kutta Method
Similarly, we used a fourth-order Runge-Kutta approach (RK4) to achieve higher accuracy in approximating the same derivatives for the same range. We:  
- Calculated intermediate slopes (k1, k2, k3, k4)  
- Computed f′(x) and f′′(x) at each step  
- Analyzed memory usage and compared performance against Euler’s Method

### Memory Footprint and Cache Behaviors
We profiled both methods to compare memory usage and cache efficiency. This helped us identify spots for improvement, such as pre-allocation of arrays and reducing repetitive computations.

### Code Optimizations
After reviewing performance and profiling data, we introduced:  
- Pre-allocated arrays (NumPy) for storing results  
- Reduced redundant calculations  
- Cleaner boundary checks within loops  

These optimizations improved computational efficiency and minimized memory overhead.

---

## How to Run the Code
1. **Clone or download** this repository.  
2. **Install dependencies** if required (e.g., NumPy, memory_profiler).  
3. **Open the relevant Python scripts**, which contain:  
   - Euler’s Method (unoptimized and optimized)  
   - Runge-Kutta Method (unoptimized and optimized)  
4. **Run each script** from the command line or any Python IDE.  
5. **Review output** for computed derivatives, profiling results, and coverage statistics.

---
We hope this README gives a clear overview of our project scope, system documentation, implementation details, and optimizations. If you have any questions or feedback, feel free to reach out to our team!
