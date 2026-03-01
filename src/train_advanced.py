import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

df = pd.read_csv("data/feature_data.csv")

FEATURES = [
    'hour_sin','hour_cos','dayofweek','month',
    'lag_1','lag_3','lag_6',
    'rolling_mean_6','rolling_std_6',
    'market_index','economic_index',
    'cloud_price_index','network_latency_ms',
    'request_count','scaling_events','temperature_c'
]

X = df[FEATURES]
y = df['usage_units']

tscv = TimeSeriesSplit(n_splits=5)

# ---------------- Random Forest ----------------
rf = RandomForestRegressor(random_state=42)

rf_params = {
    'n_estimators':[100,200],
    'max_depth':[8,12]
}

rf_grid = GridSearchCV(rf, rf_params, cv=tscv, scoring='neg_mean_absolute_error')
rf_grid.fit(X,y)

rf_best = rf_grid.best_estimator_

# ---------------- XGBoost ----------------
xgb = XGBRegressor(objective='reg:squarederror')

xgb_params = {
    'n_estimators':[100,200],
    'max_depth':[3,5],
    'learning_rate':[0.05,0.1]
}

xgb_grid = GridSearchCV(xgb, xgb_params, cv=tscv, scoring='neg_mean_absolute_error')
xgb_grid.fit(X,y)

xgb_best = xgb_grid.best_estimator_

# Evaluate on final 20%
split = int(len(df)*0.8)

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

rf_best.fit(X_train,y_train)
xgb_best.fit(X_train,y_train)

rf_preds = rf_best.predict(X_test)
xgb_preds = xgb_best.predict(X_test)

def evaluate(name, y_true, preds):
    mae = mean_absolute_error(y_true,preds)
    rmse = np.sqrt(mean_squared_error(y_true,preds))
    r2 = r2_score(y_true,preds)

    print(f"\n{name}")
    print("MAE:", round(mae,2))
    print("RMSE:", round(rmse,2))
    print("R2:", round(r2,3))

evaluate("Random Forest", y_test, rf_preds)
evaluate("XGBoost", y_test, xgb_preds)

# Save best model
best_model = xgb_best if mean_absolute_error(y_test,xgb_preds) < mean_absolute_error(y_test,rf_preds) else rf_best

joblib.dump(best_model, "best_model.pkl")

print("\nBest model saved as best_model.pkl")