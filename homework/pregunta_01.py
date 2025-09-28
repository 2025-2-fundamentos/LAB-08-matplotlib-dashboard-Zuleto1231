# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    import matplotlib.pyplot as plt
    import pandas as pd

    def load_data():
        """
        Carga los datos del archivo CSV y devuelve un DataFrame de pandas.
        """
        df = pd.read_csv("files/input/shipping-data.csv")
        return df

    def create_visual_for_shipping_per_warehouse(df):
        df = df.copy()
        plt.figure()
        counts = df["Warehouse_block"].value_counts()
        counts.plot.bar(
            title="Shipping per Warehouse",
            xlabel="Warehouse block",
            ylabel="Record Count",
            color="tab:blue",
            fontsize=8,
        )

        plt.gca().spines[["top", "right"]].set_visible(False)

        plt.savefig("docs/shipping_per_warehouse.png")
        plt.close()

    def create_visual_for_mode_of_shipment(df):
        df = df.copy()
        plt.figure()
        counts = df["Mode_of_Shipment"].value_counts()
        counts.plot.pie(
            title="Mode of Shipment",
            wedgeprops=dict(width=0.35),
            ylabel="",
            colors=["tab:blue", "tab:orange", "tab:green"],
        )

        plt.savefig("docs/mode_of_shipment.png")

    def create_visual_for_average_customer_rating(df):
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel(0)
        df = df[["mean", "min", "max"]]

        colors = [
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]
        plt.barh(
            y=df.index,
            width=df["max"].values - 1,
            left=df["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )

        plt.barh(
            y=df.index.values,
            width=df["mean"].values - 1,
            left=df["min"].values,
            color=colors,
            height=0.5,
            alpha=1.0,
        )
        plt.title("Average Customer Rating")

        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")

        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.savefig("docs/average_customer_rating.png")

    def create_visual_for_weight_distribution(df):
        df = df.copy()
        plt.figure()
        df["Weight_in_gms"].plot.hist(
            title="Shipped Weight Distribution",
            color="tab:orange",
            edgecolor="white",
        )
        plt.title("Weight Distribution")
        plt.xlabel("Weight in gms")
        plt.ylabel("Frequency")

        plt.gca().spines[["top", "right"]].set_visible(False)

        plt.savefig("docs/weight_distribution.png")
        plt.close()

    def create_dashboard():
        html_content = """
        <!DOCTYPE html>
        <html>
        <body>
            <h1>Shipping Dashboard Example</h1>
            <div style="width:45%;float:left">
            <img src="shipping_per_warehouse.png" alt="Fig 1">
            <img src="mode_of_shipment.png" alt="Fig 2">
            </div>
            <div style="width:45%;float:left">
            <img src="average_customer_rating.png" alt="Fig 3">
            <img src="weight_distribution.png" alt="Fig 4">
            </div>
        </body>
        </html>
        """

        with open("docs/index.html", "w") as f:
            f.write(html_content)

    create_visual_for_shipping_per_warehouse(load_data())
    create_visual_for_mode_of_shipment(load_data())
    create_visual_for_average_customer_rating(load_data())
    create_visual_for_weight_distribution(load_data())
    create_dashboard()


if __name__ == "__main__":
    import os

    # Crear la carpeta docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")

    pregunta_01()
