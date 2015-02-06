import learning_linear_and_rbf.experiments.kmeans.learning_kmeans

options.dataset.name= 'abalone'
options.dataset.dataset= 'data'
options.dataset.labels= 'labels'

options.epocs = 30

options.preprocessing='normalize_by_range'

options.algorithm.reorder=true;
options.algorithm.algorithm='nmfrule';
options.algorithm.iterations=3000;
options.algorithm.iter=3000;
options.algorithm.distance = 'ls';
options.algorithm.initialization = 'kmeans';

learning_kmeans(options)
