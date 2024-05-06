from pgpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariaableElimination
data=pd.DataFrame(data={'Rain':['No','No','Yes','Yes','No','Yes','Yes','No'],'TrafficJam':['Yes','No','Yes','No','Yes','Yes','No','No'],'ArriveLate':['Yes','No','Yes','No','No','Yes','Yes','No']
model=BayesianModel([('Rain',"TrafficJam'),('TrafficJam','ArriveLate')])
model.fit(data,estimator=ParameterEstimator)
print(model.get_cpds())
inference=VariableElimination(model)
query_result=inference.query(variables=['ArriveLate'],evidence={'Rain':'Yes'})
print(query_result)
