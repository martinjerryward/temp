import dash
from dash import dcc, html, dash_table
import requests
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("📊 Network Traffic Dashboard"),

    # Live Packet Table
    html.H3("Live Packet Capture"),
    dash_table.DataTable(id='packet-table',
                         columns=[
                             {"name": "Source IP", "id": "src_ip"},
                             {"name": "Destination IP", "id": "dst_ip"},
                             {"name": "Protocol", "id": "protocol"},
                             {"name": "Packet Size", "id": "packet_size"}
                         ],
                         style_table={'height': '300px', 'overflowY': 'auto'}),

    # Line chart for packet size over time
    html.H3("Packet Size Over Time"),
    dcc.Graph(id='packet-size-chart'),

    # Pie chart for protocol distribution
    html.H3("Protocol Distribution"),
    dcc.Graph(id='protocol-chart'),

    # New metrics
    html.H3("Packets Per Second"),
    dcc.Graph(id="packets-per-second"),

    html.H3("Top 5 Source IPs"),
    dcc.Graph(id="top-source-ips"),

    html.H3("Top 5 Destination IPs"),
    dcc.Graph(id="top-dest-ips"),

    html.H3("Most Used Ports"),
    dcc.Graph(id="top-ports"),

    # Auto refresh
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0)
])

# Update dashboard
@app.callback(
    [Output('packet-table', 'data'),
     Output('packet-size-chart', 'figure'),
     Output('protocol-chart', 'figure'),
     Output('packets-per-second', 'figure'),
     Output('top-source-ips', 'figure'),
     Output('top-dest-ips', 'figure'),
     Output('top-ports', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    # Fetch packets
    response = requests.get("http://127.0.0.1:5000/packets")
    data = response.json()
    df = pd.DataFrame(data) if data else pd.DataFrame(columns=["src_ip", "dst_ip", "protocol", "packet_size"])

    # Fetch metrics
    metrics_response = requests.get("http://127.0.0.1:5000/metrics")
    metrics = metrics_response.json()

    # Charts
    fig_line = px.line(df, x=df.index, y="packet_size", title="Packet Size Over Time") if not df.empty else px.line()
    fig_pie = px.pie(df, names="protocol", title="Protocol Distribution") if not df.empty else px.pie()
    fig_packets_per_sec = px.bar(x=["Packets Per Second"], y=[metrics["packets_per_second"]], title="Packets Per Second")
    fig_top_src = px.bar(x=list(metrics["top_source_ips"].keys()), y=list(metrics["top_source_ips"].values()), title="Top Source IPs")
    fig_top_dst = px.bar(x=list(metrics["top_dest_ips"].keys()), y=list(metrics["top_dest_ips"].values()), title="Top Destination IPs")
    fig_ports = px.bar(x=list(metrics["most_used_ports"].keys()), y=list(metrics["most_used_ports"].values()), title="Most Used Ports")

    return df.to_dict('records'), fig_line, fig_pie, fig_packets_per_sec, fig_top_src, fig_top_dst, fig_ports

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
