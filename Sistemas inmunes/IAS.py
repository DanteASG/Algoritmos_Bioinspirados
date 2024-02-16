import numpy as np
import matplotlib.pyplot as plt

class ImmuneSystem:
    def __init__(self, antigen, num_cells=100, num_generations=100):
        self.antigen = antigen
        self.num_cells = num_cells
        self.num_generations = num_generations
        self.cells = np.random.rand(num_cells, len(antigen))  # Randomly initialize cells

    def distance(self, cell):
        return np.linalg.norm(cell - self.antigen)

    def select_cells(self, threshold):
        return [cell for cell in self.cells if self.distance(cell) < threshold]

    def mutate(self, cells):
        mutated_cells = []
        for cell in cells:
            mutation = np.random.normal(0, 0.1, size=cell.shape)  # Gaussian mutation
            mutated_cell = np.clip(cell + mutation, 0, 1)  # Ensure values are in [0, 1] range
            mutated_cells.append(mutated_cell)
        return mutated_cells

    def run(self):
        for generation in range(self.num_generations):
            selected_cells = self.select_cells(threshold=0.1)
            if len(selected_cells) == 0:
                print("No cells selected, antigen not recognized.")
                break
            print(f"Generation {generation}: {len(selected_cells)} cells selected.")
            self.cells = self.mutate(selected_cells)

        # Plot final state of cells
        plt.scatter(*zip(*self.cells), label='Cells')
        plt.scatter(*self.antigen, color='red', label='Antigen')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Final State of Cells and Antigen')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    antigen = np.array([0.8, 0.8])  # Antigen to be recognized by the immune system
    immune_system = ImmuneSystem(antigen)
    immune_system.run()
