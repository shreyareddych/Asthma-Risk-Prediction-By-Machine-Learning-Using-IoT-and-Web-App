import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

data = pd.read_csv("Asthma dataset.csv")
X = data[['Gender', 'PM25', 'PM10', 'Outdoor Temperature', 'Humidity']]
y = data['PEFR']

model = DecisionTreeClassifier()
model.fit(X, y)

class AsthmaApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.label = MDLabel(text="Asthma Risk Prediction", halign="center", theme_text_color='Custom',
                             text_color=(0, 1, 0, 1), font_style='H4', pos_hint={'center_x': 0.5, 'center_y': 0.9})

        self.pm25_input = MDTextField(hint_text="PM2.5 Concentration", pos_hint={'center_x': 0.5, 'center_y': 0.8},
                                      size_hint_x=0.7, multiline=False)
        self.pm10_input = MDTextField(hint_text="PM10 Concentration", pos_hint={'center_x': 0.5, 'center_y': 0.7},
                                      size_hint_x=0.7, multiline=False)
        self.temp_input = MDTextField(hint_text="Outdoor Temperature (°C)", pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                      size_hint_x=0.7, multiline=False)
        self.humidity_input = MDTextField(hint_text="Humidity (%)", pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                          size_hint_x=0.7, multiline=False)
        self.gender_input = MDTextField(hint_text="Gender (1-Male/0-Female)", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                        size_hint_x=0.7, multiline=False)
        self.actual_pefr_input = MDTextField(hint_text="Actual PEFR", pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                             size_hint_x=0.7, multiline=False)

        self.btn = MDRaisedButton(text='Predict', pos_hint={'center_x': 0.5, 'center_y': 0.2}, on_release=self.predict_risk)
        self.output_label = MDLabel(text="", halign="center", theme_text_color='Custom', text_color=(0, 0, 1, 1),
                                    font_style='H5', pos_hint={'center_x': 0.5, 'center_y': 0.1})

        self.screen.add_widget(self.label)
        self.screen.add_widget(self.pm25_input)
        self.screen.add_widget(self.pm10_input)
        self.screen.add_widget(self.temp_input)
        self.screen.add_widget(self.humidity_input)
        self.screen.add_widget(self.gender_input)
        self.screen.add_widget(self.actual_pefr_input)
        self.screen.add_widget(self.btn)
        self.screen.add_widget(self.output_label)

        return self.screen

    def predict_risk(self, obj):
        try:
            pm25_concentration = float(self.pm25_input.text)
            pm10_concentration = float(self.pm10_input.text)
            outdoor_temp = float(self.temp_input.text)
            humidity = float(self.humidity_input.text)
            gender = int(self.gender_input.text)
            actual_pefr = float(self.actual_pefr_input.text)

            feature_values = [gender, pm25_concentration, pm10_concentration, outdoor_temp, humidity]
            predicted_pefr = model.predict([feature_values])[0]

            per_pefr = (actual_pefr / predicted_pefr) * 100

            if per_pefr >= 80:
                self.output_label.text = "SAFE"
            elif 50 <= per_pefr < 80:
                self.output_label.text = "MODERATE"
            else:
                self.output_label.text = "RISK"

        except Exception as e:
            self.output_label.text = f"Error: {e}"

if __name__ == '__main__':
    AsthmaApp().run()
