import pandas as pd


def add_income_credit_ratio(X: pd.DataFrame) -> pd.DataFrame:
    ratio = X["A8"] / X["A2"].replace(0, np.nan)
    return ratio.to_frame("A8_to_A2_ratio").fillna(0.0)

def ratio_feature_names_out(transformer, input_features): #functiontransformer의 출력 컬럼명을 지정하는 콜백 함수
    return np.array(["A8_to_A2_ratio"])