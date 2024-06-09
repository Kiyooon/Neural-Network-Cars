# Neural-Network-Cars

This project demonstrates a car simulation using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to evolve neural networks that control the behavior of autonomous cars. The goal is for the cars to navigate through a track without colliding with the borders. In the first iteration, the cars in the simulation operate randomly. Each action a car takes results in either a reward or a penalty, forming the basis of a fitness metric used in the simulation. The fitness of a car increases based on the distance it travels without crashing. After each generation, the cars evolve, with those having the highest fitness values likely to survive and reproduce, while those performing poorly may go extinct. When a car reproduces, its offspring is not an exact copy but rather similar to its parent, with a chance to improve. Similar cars form species, and if a species fails to see improvement over several generations, it goes extinct. By implementing these principles, the program creates an environment where the best cars thrive and reproduce, while the worst cars are phased out, allowing the model to experiment and evolve over time.

## How To Use

1. Launch the program.
2. Click and drag to draw the road on the screen.
3. Press the spacebar to start the simulation.
4. Cars will appear at the starting line (red line) and navigate the road.

## Dependencies

- Python 3.x
- Pygame
- NEAT-Python


