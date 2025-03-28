# test_loading.py
import joblib
import pandas as pd

print("=== Pipeline Test ===")
try:
    pipeline = joblib.load('preprocessing_pipeline.pkl')
    print("✓ Pipeline loaded")
    print("Features:", pipeline.get_feature_names_out())
    
    # Test with sample data
    test_data = pd.DataFrame([[
        25, 3.2, 2.8, 0.75, 15, 1, 0  # Sample values
    ]], columns=[
        'age', 'attention_score', 'hyperactivity_score',
        'academic_index', 'bai1_total', 'sex_female', 'sex_male'
    ])
    
    transformed = pipeline.transform(test_data)
    print("✓ Transformation successful")
    print("Output shape:", transformed.shape)
    
except Exception as e:
    print("✗ Pipeline failed:", str(e))

print("\n=== Model Test ===")
try:
    model = joblib.load('adhd_model_v1.pkl')
    print("✓ Model loaded")
    print("Classes:", model.classes_)
    
    # Use the transformed data from above
    if 'transformed' in locals():
        proba = model.predict_proba(transformed[:1])
        print("✓ Prediction successful")
        print("Probabilities:", proba)
        
except Exception as e:
    print("✗ Model failed:", str(e))