import numpy as np
import dimod

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


J = {(0,1):1,(0,2):1,(1,3):1,(1,4):1,(2,3):1,(3,4):1}
h = {}
model = dimod.BinaryQuadraticModel( h, J, 0.0, dimod.SPIN)
print("Le model résolu est le suivant:")
print(model)
print()

from dimod.reference.samplers import ExactSolver
sampler = ExactSolver()
solution = sampler.sample(model)
print("Résultat de la résolution exacte (solution optimale)")
print(solution)
print()

sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(model, num_reads=10)
print("The solution with simulated annealing is")
print(response)
print()

sampler = EmbeddingComposite(DWaveSampler(Solver='Advantage_system1.1'))
sampler_name = sampler.properties['child_properties']['chip_id']
response = sampler.sample(model, num_reads = 10000)
print("The solution obtained by D-Wave's quantum annealer", sampler_name, "is")
print(response)
print()