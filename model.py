import pickle
from sklearn.linear_model import LinearRegression

class Model:

    def __init__(self, model_location):
        # we initialize the model twice so that type will be properly assigned on unpickling.
        self._model = LinearRegression()
        self._model = pickle.load(open(model_location, 'rb'))

    def apply_model(self, input_matrix):
        """
        input_vector is a matrix of dimension N x M,
        where N is the number of samples/cases,
        and M is the number of features.
        """
        return self._model.predict(input_matrix)
