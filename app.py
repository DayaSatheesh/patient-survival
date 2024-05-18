import gradio as gr
import joblib
import numpy as np
import pandas as pd

model=joblib.load('xgboost-model.pkl')

def predict_death_event(age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time):

    input_df = pd.DataFrame({"age": [float(age)],
                             "anaemia": [int(anaemia)],
                             "creatinine_phosphokinase": [int(creatinine_phosphokinase)],
                             "diabetes": [int(diabetes)],
                             "ejection_fraction": [int(ejection_fraction)],
                             "high_blood_pressure": [int(high_blood_pressure)],
                             "platelets": [float(platelets)],
                             "serum_creatinine": [float(serum_creatinine)],
                             "serum_sodium": [int(serum_sodium)],
                             "sex": [int(sex)],
                             "smoking": [int(smoking)],
                             "time": [int(time)]
                             })

   # result = model.predict(input_data=input_df.replace({np.nan: None}))["predictions"]
   # label = "Survive" if result[0]==1 else "Not Survive"
    result = model.predict(input_df)
    return result
    
inputs1= [gr.Slider(20, 90, value=4, label="age", info="Choose age between 20 and 90"),
          gr.Radio(["0", "1"], label="anaemia", info="does the person have anaemia?"),
          gr.Slider(100, 10000, value=4, label="creatinine_phosphokinase", info="Choose between 100 and 10000"),
          gr.Radio(["0", "1"], label="diabetes", info="does the person have diabetes?"),
           gr.Slider(100, 10000, value=4, label="ejection_fraction", info="Choose between 100 and 10000"),
           gr.Radio(["0", "1"], label="high_blood_pressure", info="does the person have diabetes?"),
           gr.Slider(10000, 500000, value=4, label="platelets", info="Choose between 100 and 10000"),
           gr.Slider(1, 4, value=4, label="serum_creatinine", info="Choose between 1 and 4"),
           gr.Slider(100, 200, value=4, label="serum_sodium", info="Choose between 100 and 200"),
           gr.Radio(["0", "1"], label="sex", info="does the person have diabetes?"),
           gr.Radio(["0", "1"], label="smoking", info="does the person have smoking?"),
           gr.Slider(1, 100, value=4, label="time", info="Choose between 1 and 100")
           ]

title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gr.Interface(fn = predict_death_event,
                         inputs = inputs1,
                         outputs ='textbox',
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(server_name="0.0.0.0", server_port = 8001)   # Ref: https://www.gradio.app/docs/interface

