from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Cloudy': [True, True, False, False],
    'Sprinkler': [True, False, True, False]
})

# Define the Bayesian Network structure
model = BayesianNetwork([('Cloudy', 'Sprinkler')])

# Fit the model using Maximum Likelihood Estimation
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Perform inference
inference = VariableElimination(model)

# Query the model
print("Inferencing P(Sprinkler=True | Cloudy=False):")
result = inference.query(variables=['Sprinkler'], evidence={'Cloudy': False})
print(result)
