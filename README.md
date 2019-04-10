# FrameDevelopment
#### FSAE Space-Frame Optimization and Development Software  

Optimizes a tubular space-frame for a variety of load cases inputted by the user.
The program uses the direct stiffness method to calculate the displacements of frame nodes,
as well as the resultant forces in tube members. The displacements at nodes relative to each load case
are then used to calculate a "score" for the frame using an objective function. Tube thickness and
geometry changes are made at random via a genetic algorithm, and only the frames with the best scores
survive for use as the "seed" frames in the next generation.

I eventually hope to implement generative design.

**MaRGolIn iS bIG W A C K**