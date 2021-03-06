__authors__ = "Joseph Gallego"
__email__ = "jagallegom@unal.edu.co"

import semantic_methods_toolkit.python.utils.dataset_factory as dataset_factory
from semantic_methods_toolkit.python.unsupervised_technique.cnmf_experiment \
    import CnmfExperiment
from semantic_methods_toolkit.python.utils.generate_logarithm_vector_kernel \
    import generate_logarithm_vector_kernel
from semantic_methods_toolkit.python.preprocess_data.normalize_by_range \
    import normalize_by_range
from semantic_methods_toolkit.python.contamination_experiment \
    import contamination_experiment


data, labels = dataset_factory.dataset_factory('../../../../dataset/jaffe_occlusion_contamination.mat',
                                               options={'data': 'data_real', 'labels': 'labels'})
contamination_data, labels = dataset_factory.dataset_factory(
    '../../../../dataset/jaffe_occlusion_contamination.mat',
    options={'data': 'data_contamination', 'labels': 'labels'})

import numpy as np

print data
k = np.unique(labels).size

data, contamination_data = normalize_by_range(data, 0, contamination_data)
vect_to_prove = [2**x for x in np.arange(-20, 20)]
vector = generate_logarithm_vector_kernel(data, vect_to_prove, percentage=0.5)

dt = [('key', 'S100'), ('value', 'S100')]
arr = np.zeros((10,), dtype=dt)

arr[0]['value'] = str(k)
arr[0]['key'] = 'k'
arr[1]['value'] = "iter: " + str(3000)
arr[1]['key'] = 'termination_criterion'
arr[2]['value'] = 'random'
arr[2]['key'] = 'initialization'
arr[3]['value'] = '10'
arr[3]['key'] = 'epocs'
arr[4]['value'] = '1'
arr[4]['key'] = 'clustering_accuracy'
arr[5]['value'] = '1'
arr[5]['key'] = 'purity'
arr[6]['value'] = 'rbf'
arr[6]['key'] = 'kernel'
arr[7]['value'] = '1'
arr[7]['key'] = 'param'
arr[8]['value'] = str(vector)
arr[8]['key'] = 'vect'
arr[9]['value'] = '50'
arr[9]['key'] = 'percentage_contamination'


def options(vect):

    option = {arr[0]['key']: int(arr[0]['value']),
              arr[1]['key']: {'iter': 1000},
              arr[2]['key']: arr[2]['value'],
              arr[3]['key']: int(arr[3]['value']),
              arr[4]['key']: int(arr[4]['value']),
              arr[5]['key']: int(arr[5]['value']),
              arr[6]['key']: arr[6]['value'],
              arr[7]['key']: int(arr[7]['value']),
              arr[8]['key']:  vector,
              arr[9]['key']: int(arr[9]['value'])}
    for i in vect:
        #define sigma
        option['param'] = i
        yield option

option = {arr[0]['key']: int(arr[0]['value']),
          arr[1]['key']: {'iter': 1000},
          arr[2]['key']: arr[2]['value'],
          arr[3]['key']: int(arr[3]['value']),
          arr[4]['key']: int(arr[4]['value']),
          arr[5]['key']: int(arr[5]['value']),
          arr[6]['key']: arr[6]['value'],
          arr[7]['key']: int(arr[7]['value']),
          arr[8]['key']: vector,
          arr[9]['key']: int(arr[9]['value'])}

cnmf_experiment = CnmfExperiment(data, option)

results_performance, last_results_performance, options_results_performance, \
    results_performance_tunning = contamination_experiment(
    data, contamination_data, labels, cnmf_experiment, options([1, 2, 3]), option)

import time
## dd/mm/yyyy format
date = (time.strftime("%d%m%Y_%H:%M_"))

np.save(str(date) + 'linear_cnmf', {'last_results_performance': last_results_performance,
                    'results_performance': results_performance, 'results_performance_tunning': results_performance_tunning,
                    'options_results_performance': options_results_performance, 'options': arr})
