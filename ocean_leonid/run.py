from src import viz

if __name__ == "__main__":
    app = viz()
    app.run_server(debug=True, host="0.0.0.0", port=8050)
