from enmapboxprocessing.algorithm.fitregressoralgorithmbase import FitRegressorAlgorithmBase
from enmapbox.typeguard import typechecked


@typechecked
class FitGenericRegressorAlgorithm(FitRegressorAlgorithmBase):

    def displayName(self) -> str:
        return 'Fit generic regressor'

    def shortDescription(self) -> str:
        return 'A generic regressor.'

    def helpParameterCode(self) -> str:
        return 'Scikit-learn python code.'

    def code(cls):
        from sklearn.dummy import DummyRegressor

        regressor = DummyRegressor()
        return regressor
