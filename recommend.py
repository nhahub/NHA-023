import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from langchain_google_genai import ChatGoogleGenerativeAI

# Load your data
df = pd.read_csv(r"D:\data engineer\depi project\airbnb data\Albany.csv")

app = Dash(__name__)
genders = ["Male", "Female"]
cities = sorted(df["city"].unique()) if "city" in df.columns else ["Albany"]

# Gemini API setup
GEMINI_API_KEY = "AIzaSyAVQi4iWkFfqxGwNND_xvrL2qQDLN53djk"


def get_gemini_recommendation(prompt: str) -> str:
    """Use LangChain ChatGoogleGenerativeAI (gemini-2.5-flash)."""
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=GEMINI_API_KEY,
        )
        res = llm.invoke(prompt)
        return str(res.content)
    except Exception as e:
        return "AI recommendation error: " + str(e)


app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "🏠 Airbnb Data Analytics Dashboard",
                    style={
                        "color": "#2058b4",
                        "margin-bottom": "10px",
                        "text-align": "center",
                        "font-size": "2.5em",
                    },
                ),
                html.P(
                    "Comprehensive market analysis with interactive visualizations and AI-powered recommendations",
                    style={
                        "color": "#666",
                        "font-size": "1.2em",
                        "text-align": "center",
                        "margin-bottom": "30px",
                    },
                ),
                # City Selector
                html.Div(
                    [
                        html.Label(
                            "Select City for Analysis:",
                            style={
                                "font-weight": "600",
                                "font-size": "1.1em",
                                "color": "#2058b4",
                            },
                        ),
                        dcc.Dropdown(
                            id="city-dropdown",
                            options=[{"label": c, "value": c} for c in cities],
                            value=cities[0],
                            style={"margin-top": "10px", "font-size": "1.1em"},
                        ),
                    ],
                    style={
                        "background": "#f8fbff",
                        "border-radius": "12px",
                        "padding": "20px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                html.Hr(
                    style={
                        "border": "none",
                        "border-top": "2px solid #e0e0e0",
                        "margin": "30px 0",
                    }
                ),
                # Map
                html.Div(
                    [
                        html.H2(
                            "🗺️ Geographic Distribution of Listings",
                            style={"color": "#2058b4", "font-size": "1.8em"},
                        ),
                        html.P(
                            "Map of listing locations with color and size indicating price levels.",
                            style={"line-height": "1.8", "color": "#555"},
                        ),
                        html.Div(id="map-div", style={"margin-top": "20px"}),
                    ],
                    style={
                        "background": "#fff",
                        "border-radius": "12px",
                        "padding": "30px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                # Price histogram
                html.Div(
                    [
                        html.H2(
                            "💰 Price Distribution Analysis",
                            style={"color": "#2058b4", "font-size": "1.8em"},
                        ),
                        html.P(
                            "Histogram of nightly prices to understand typical price ranges and outliers.",
                            style={"line-height": "1.8", "color": "#555"},
                        ),
                        html.Div(id="price-histogram", style={"margin-top": "20px"}),
                    ],
                    style={
                        "background": "#fff",
                        "border-radius": "12px",
                        "padding": "30px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                # Room type pie
                html.Div(
                    [
                        html.H2(
                            "🏘️ Property Type Market Composition",
                            style={"color": "#2058b4", "font-size": "1.8em"},
                        ),
                        html.P(
                            "Pie chart of room types (entire home, private room, shared room).",
                            style={"line-height": "1.8", "color": "#555"},
                        ),
                        html.Div(id="room-type-chart", style={"margin-top": "20px"}),
                    ],
                    style={
                        "background": "#fff",
                        "border-radius": "12px",
                        "padding": "30px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                # Reviews boxplot
                html.Div(
                    [
                        html.H2(
                            "⭐ Guest Activity & Booking Frequency",
                            style={"color": "#2058b4", "font-size": "1.8em"},
                        ),
                        html.P(
                            "Box plot of reviews per month as a proxy for booking activity.",
                            style={"line-height": "1.8", "color": "#555"},
                        ),
                        html.Div(id="reviews-chart", style={"margin-top": "20px"}),
                    ],
                    style={
                        "background": "#fff",
                        "border-radius": "12px",
                        "padding": "30px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                # City metrics
                html.Div(
                    [
                        html.H2(
                            "📊 Quick Market Summary",
                            style={"color": "#2058b4", "font-size": "1.8em"},
                        ),
                        html.P(
                            "Average price and average reviews/month for the selected city.",
                            style={"line-height": "1.8", "color": "#555"},
                        ),
                        html.Div(id="chart-div", style={"margin-top": "20px"}),
                        html.Div(
                            id="chart-desc",
                            style={
                                "margin-top": "20px",
                                "font-size": "1.15em",
                                "color": "#333",
                                "background": "#f9f9f9",
                                "padding": "16px",
                                "border-radius": "8px",
                            },
                        ),
                    ],
                    style={
                        "background": "#fff",
                        "border-radius": "12px",
                        "padding": "30px",
                        "box-shadow": "0 2px 8px rgba(0,0,0,0.08)",
                        "margin-bottom": "30px",
                    },
                ),
                html.Hr(
                    style={
                        "border": "none",
                        "border-top": "3px solid #2058b4",
                        "margin": "40px 0",
                    }
                ),
                # Recommendation section
                html.Div(
                    [
                        html.H2(
                            "🤖 Get Your Personalized AI Recommendation",
                            style={
                                "color": "#2058b4",
                                "font-size": "2em",
                                "text-align": "center",
                                "margin-bottom": "20px",
                            },
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Label(
                                            "Gender:", style={"font-weight": "600"}
                                        ),
                                        dcc.Dropdown(
                                            id="gender-dropdown",
                                            options=[
                                                {"label": g, "value": g}
                                                for g in genders
                                            ],
                                            value=genders[0],
                                            style={"margin-bottom": "12px"},
                                        ),
                                    ],
                                    style={
                                        "width": "48%",
                                        "display": "inline-block",
                                        "padding-right": "2%",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Label(
                                            "Age:", style={"font-weight": "600"}
                                        ),
                                        dcc.Input(
                                            id="age-input",
                                            type="number",
                                            min=16,
                                            max=100,
                                            value=30,
                                            style={
                                                "width": "100%",
                                                "padding": "8px",
                                                "border-radius": "4px",
                                                "border": "1px solid ",  # ddd"",
                                            },
                                        ),
                                    ],
                                    style={"width": "48%", "display": "inline-block"},
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label(
                                    "Number of Hosts (experience level):",
                                    style={"font-weight": "600", "margin-top": "12px"},
                                ),
                                dcc.Input(
                                    id="hosts-input",
                                    type="number",
                                    min=1,
                                    max=99,
                                    value=1,
                                    style={
                                        "width": "100%",
                                        "padding": "8px",
                                        "border-radius": "4px",
                                        "border": "1px solid #ddd",
                                    },
                                ),
                            ],
                            style={"margin-top": "12px"},
                        ),
                        html.Div(
                            [
                                html.Button(
                                    "Generate My Personalized Recommendation",
                                    id="recommend-btn",
                                    n_clicks=0,
                                    style={
                                        "background": "#2058b4",
                                        "color": "white",
                                        "border": "none",
                                        "padding": "15px 40px",
                                        "border-radius": "8px",
                                        "cursor": "pointer",
                                        "font-size": "1.1em",
                                        "font-weight": "600",
                                        "margin-top": "20px",
                                        "display": "block",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                    },
                                )
                            ],
                            style={"text-align": "center"},
                        ),
                        html.Div(
                            id="recommendation-output",
                            style={
                                "margin-top": "30px",
                                "background": "#eef2ff",
                                "padding": "25px",
                                "border-radius": "12px",
                                "border-left": "6px solid #2058b4",
                            },
                        ),
                    ],
                    style={
                        "background": "#f8fbff",
                        "border-radius": "12px",
                        "padding": "40px",
                        "box-shadow": "0 4px 12px rgba(0,0,0,0.1)",
                        "margin-bottom": "40px",
                    },
                ),
            ],
            style={
                "max-width": "1200px",
                "margin": "40px auto",
                "background": "#ffffff",
                "border-radius": "16px",
                "padding": "40px",
                "box-shadow": "0 4px 16px rgba(0,0,0,0.1)",
            },
        )
    ],
    style={"background": "#f6faff", "min-height": "100vh", "padding": "20px"},
)


# Map
@app.callback(Output("map-div", "children"), Input("city-dropdown", "value"))
def update_map(city):
    try:
        city_df = df[df["city"] == city].copy() if "city" in df.columns else df.copy()
        if (
            not city_df.empty
            and "latitude" in city_df.columns
            and "longitude" in city_df.columns
            and "price" in city_df.columns
        ):
            if city_df["price"].dtype == "object":
                city_df["price"] = (
                    city_df["price"]
                    .astype(str)
                    .str.replace("$", "")
                    .str.replace(",", "")
                )
                city_df["price"] = pd.to_numeric(city_df["price"], errors="coerce")

            city_df = city_df[
                (city_df["latitude"].notna())
                & (city_df["longitude"].notna())
                & (city_df["price"].notna())
                & (city_df["price"] > 0)
            ]
            if city_df.empty:
                return html.Div("No valid location data.", style={"padding": "20px"})

            if len(city_df) > 1000:
                city_df = city_df.sample(1000)

            fig = px.scatter_mapbox(
                city_df,
                lat="latitude",
                lon="longitude",
                color="price",
                size="price",
                hover_data={"price": True},
                title=f"Listing Locations in {city}",
                color_continuous_scale="Viridis",
                zoom=11,
                height=600,
            )
            fig.update_layout(
                mapbox_style="open-street-map", margin={"r": 0, "t": 40, "l": 0, "b": 0}
            )
            return dcc.Graph(figure=fig)
        return html.Div("Map data not available.", style={"padding": "20px"})
    except Exception as e:
        return html.Div(f"Error loading map: {str(e)}", style={"color": "red"})


# Price histogram
@app.callback(Output("price-histogram", "children"), Input("city-dropdown", "value"))
def update_price_histogram(city):
    try:
        city_df = df[df["city"] == city].copy() if "city" in df.columns else df.copy()
        if not city_df.empty and "price" in city_df.columns:
            if city_df["price"].dtype == "object":
                city_df["price"] = (
                    city_df["price"]
                    .astype(str)
                    .str.replace("$", "")
                    .str.replace(",", "")
                )
                city_df["price"] = pd.to_numeric(city_df["price"], errors="coerce")
            city_df = city_df[(city_df["price"].notna()) & (city_df["price"] > 0)]
            if city_df.empty:
                return html.Div("No valid price data.", style={"padding": "20px"})
            fig = px.histogram(
                city_df,
                x="price",
                nbins=50,
                title=f"Price Distribution in {city}",
                labels={"price": "Nightly Price (USD)", "count": "Number of Listings"},
                color_discrete_sequence=["#2058b4"],
            )
            fig.update_layout(showlegend=False, height=500)
            return dcc.Graph(figure=fig)
        return html.Div("Price data not available.", style={"padding": "20px"})
    except Exception as e:
        return html.Div(f"Error: {str(e)}", style={"color": "red"})


# Room type
@app.callback(Output("room-type-chart", "children"), Input("city-dropdown", "value"))
def update_room_type(city):
    try:
        city_df = df[df["city"] == city] if "city" in df.columns else df
        if not city_df.empty and "room_type" in city_df.columns:
            room_counts = city_df["room_type"].value_counts()
            fig = px.pie(
                values=room_counts.values,
                names=room_counts.index,
                title=f"Room Type Distribution in {city}",
                color_discrete_sequence=px.colors.sequential.Blues_r,
            )
            fig.update_layout(height=500)
            return dcc.Graph(figure=fig)
        return html.Div("Room type data not available.", style={"padding": "20px"})
    except Exception as e:
        return html.Div(f"Error: {str(e)}", style={"color": "red"})


# Reviews
@app.callback(Output("reviews-chart", "children"), Input("city-dropdown", "value"))
def update_reviews(city):
    try:
        city_df = df[df["city"] == city] if "city" in df.columns else df
        if not city_df.empty and "reviews_per_month" in city_df.columns:
            city_df = city_df[city_df["reviews_per_month"].notna()]
            fig = px.box(
                city_df,
                y="reviews_per_month",
                title=f"Monthly Reviews Distribution in {city}",
                labels={"reviews_per_month": "Reviews Per Month"},
                color_discrete_sequence=["#7694ce"],
            )
            fig.update_layout(height=500)
            return dcc.Graph(figure=fig)
        return html.Div("Review data not available.", style={"padding": "20px"})
    except Exception as e:
        return html.Div(f"Error: {str(e)}", style={"color": "red"})


# City metrics
@app.callback(
    Output("chart-div", "children"),
    Output("chart-desc", "children"),
    Input("city-dropdown", "value"),
)
def update_chart(city):
    try:
        city_df = df[df["city"] == city].copy() if "city" in df.columns else df.copy()
        price = None
        reviews = None
        desc_parts = []

        if not city_df.empty:
            if "price" in city_df.columns:
                if city_df["price"].dtype == "object":
                    city_df["price"] = (
                        city_df["price"]
                        .astype(str)
                        .str.replace("$", "")
                        .str.replace(",", "")
                    )
                    city_df["price"] = pd.to_numeric(city_df["price"], errors="coerce")
                price = city_df["price"].mean()
                if pd.notna(price):
                    desc_parts.append(
                        html.Div(
                            [
                                "💰 ",
                                html.B("Average listing price: "),
                                "$" + str(round(price, 2)) + " USD per night",
                            ],
                            style={"margin-bottom": "10px"},
                        )
                    )
            if "reviews_per_month" in city_df.columns:
                reviews = city_df["reviews_per_month"].mean()
                if pd.notna(reviews):
                    desc_parts.append(
                        html.Div(
                            [
                                "⭐ ",
                                html.B("Average reviews per month: "),
                                str(round(reviews, 2)),
                            ]
                        )
                    )

        metrics = []
        if price is not None and pd.notna(price):
            metrics.append({"Metric": "Avg Price ($)", "Value": price})
        if reviews is not None and pd.notna(reviews):
            metrics.append({"Metric": "Reviews/Month", "Value": reviews})

        if metrics:
            plot_df = pd.DataFrame(metrics)
            fig = px.bar(
                plot_df,
                x="Metric",
                y="Value",
                title=f"Key Metrics for {city}",
                color="Metric",
                color_discrete_sequence=["#2058b4", "#7694ce"],
            )
            fig.update_layout(showlegend=False, height=450)
            chart = dcc.Graph(figure=fig)
        else:
            chart = html.Div("No data available.", style={"padding": "20px"})

        desc_div = (
            html.Div(desc_parts, style={"line-height": "2"})
            if desc_parts
            else html.Div("")
        )
        return chart, desc_div
    except Exception as e:
        return html.Div(f"Error: {str(e)}", style={"color": "red"}), html.Div("")


# Recommendation
@app.callback(
    Output("recommendation-output", "children"),
    Input("recommend-btn", "n_clicks"),
    Input("gender-dropdown", "value"),
    Input("city-dropdown", "value"),
    Input("age-input", "value"),
    Input("hosts-input", "value"),
)
def get_recommendation(n_clicks, gender, city, age, hosts):
    if n_clicks == 0:
        return ""

    try:
        gender_str = str(gender) if gender else "Not specified"
        city_str = str(city) if city else "Not specified"
        age_str = str(age) if age else "N/A"
        hosts_str = str(hosts) if hosts else "N/A"

        city_df = (
            df[df["city"] == city_str].copy() if "city" in df.columns else df.copy()
        )

        price_str = "N/A"
        reviews_str = "N/A"

        if not city_df.empty:
            if "price" in city_df.columns:
                if city_df["price"].dtype == "object":
                    city_df["price"] = (
                        city_df["price"]
                        .astype(str)
                        .str.replace("$", "")
                        .str.replace(",", "")
                    )
                    city_df["price"] = pd.to_numeric(city_df["price"], errors="coerce")
                price_val = city_df["price"].mean()
                if pd.notna(price_val):
                    price_str = "$" + str(round(price_val, 2))

            if "reviews_per_month" in city_df.columns:
                reviews_val = city_df["reviews_per_month"].mean()
                if pd.notna(reviews_val):
                    reviews_str = str(round(reviews_val, 2))

        prompt = (
            "User profile:\n"
            f"Gender: {gender_str}\n"
            f"City: {city_str}\n"
            f"Age: {age_str}\n"
            f"Number of Hosts they want: {hosts_str}\n"
            f"Average listing price in {city_str}: {price_str}\n"
            f"Average reviews per month: {reviews_str}\n\n"
            "Based on this profile and market data, provide a detailed personalized Airbnb recommendation "
            "with concrete tips for choosing listings, budgeting, and maximizing satisfaction."
        )

        recommendation = get_gemini_recommendation(prompt)

        return html.Div(
            [
                html.H4(
                    "🤖 AI Recommendation:",
                    style={"color": "#2058b4", "margin-bottom": "12px"},
                ),
                html.Div(
                    str(recommendation),
                    style={"white-space": "pre-wrap", "line-height": "1.6"},
                ),
            ]
        )
    except Exception as e:
        return html.Div(
            f"Error generating recommendation: {str(e)}", style={"color": "red"}
        )


if __name__ == "__main__":
    app.run(debug=True)
