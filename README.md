# DataProject2
🌍 World Trends Dashboard
An interactive web dashboard built using Dash and Plotly Express to explore global trends in Life Expectancy, GDP per Capita, and Population over time using the Gapminder dataset.

🚀 Features
Select one or multiple countries to visualize.

Filter data by year range using a range slider.

Toggle between three data metrics:

Life Expectancy

GDP per Capita

Population

Optional Dark Mode toggle for visual theme preference.

Responsive and interactive Plotly graphs.

📊 Data Source
Gapminder Five-Year Data

🛠️ Built With
Dash

Plotly Express

Pandas

💻 How to Run
Install dependencies (if you haven’t already):

bash
Copy
Edit
pip install dash pandas plotly
Run the app:

bash
Copy
Edit
python app.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8050/
📁 File Structure
bash
Copy
Edit
.
├── app.py          # Main Dash application file
└── README.md       # Project documentation (this file)
🧠 App Preview
The dashboard includes:

Dropdown for selecting countries

Year range slider

Tabs for switching between metrics

Toggle for enabling dark mode

Interactive line charts that update based on selections

🔧 Customization
You can customize:

Default countries (value in dcc.Dropdown)

Default year range (value in dcc.RangeSlider)

Add more data tabs or metrics

Extend UI with new controls like bar charts or histograms

📄 License
This project uses data under the Gapminder license and is intended for educational and demonstration purposes.